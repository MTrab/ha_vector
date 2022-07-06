"""Connection control module rewritten for Home Assistant."""
from __future__ import annotations

import asyncio
import functools
import inspect
import logging
import platform
import sys
import threading
from asyncio import AbstractEventLoop
from concurrent import futures
from enum import Enum
from typing import Any, Awaitable, Callable, Coroutine, Dict, List

import aiogrpc
import grpc
from google.protobuf.text_format import MessageToString

from . import util
from .exceptions import (
    VectorAsyncException,
    VectorBehaviorControlException,
    VectorConfigurationException,
    VectorControlException,
    VectorControlTimeoutException,
    VectorInvalidVersionException,
    VectorNotFoundException,
    connection_error,
)
from .messaging import client, protocol
from .version import __version__


class CancelType(Enum):
    """Enum used to specify cancellation options for behaviors -- internal use only"""

    #: Cancellable as an 'Action'
    CANCELLABLE_ACTION = 0
    #: Cancellable as a 'Behavior'
    CANCELLABLE_BEHAVIOR = 1


class ControlPriorityLevel(Enum):
    """Enum used to specify the priority level for the program."""

    #: Runs above mandatory physical reactions, will drive off table, perform while on a slope,
    #: ignore low battery state, work in the dark, etc.
    OVERRIDE_BEHAVIORS_PRIORITY = (
        protocol.ControlRequest.OVERRIDE_BEHAVIORS
    )  # pylint: disable=no-member
    #: Runs below Mandatory Physical Reactions such as tucking Vector's head and arms during a fall,
    #: yet above Trigger-Word Detection.  Default for normal operation.
    DEFAULT_PRIORITY = protocol.ControlRequest.DEFAULT  # pylint: disable=no-member
    #: Holds control of robot before/after other SDK connections
    #: Used to disable idle behaviors.  Not to be used for regular behavior control.
    RESERVE_CONTROL = (
        protocol.ControlRequest.RESERVE_CONTROL
    )  # pylint: disable=no-member
    #: No control priority needed
    NONE = None


class _ControlEventManager:
    """This manages every :class:`asyncio.Event` that handles the behavior control
    system.

    These include three events: granted, lost, and request.

    :class:`granted_event` represents the behavior system handing control to the SDK.

    :class:`lost_event` represents a higher priority behavior taking control away from the SDK.

    :class:`request_event` Is a way of alerting :class:`Connection` to request control.
    """

    def __init__(
        self,
        loop: AbstractEventLoop,
        priority: ControlPriorityLevel = ControlPriorityLevel.NONE,
    ):
        self._granted_event = asyncio.Event()
        self._lost_event = asyncio.Event()
        self._request_event = asyncio.Event()
        self._has_control = False
        self._priority = priority
        self._is_shutdown = False

    @property
    def granted_event(self) -> asyncio.Event:
        """This event is used to notify listeners that control has been granted to the SDK."""
        return self._granted_event

    @property
    def lost_event(self) -> asyncio.Event:
        """Represents a higher priority behavior taking control away from the SDK."""
        return self._lost_event

    @property
    def request_event(self) -> asyncio.Event:
        """Used to alert :class:`Connection` to request control."""
        return self._request_event

    @property
    def has_control(self) -> bool:
        """Check to see that the behavior system has control (without blocking by checking :class:`granted_event`)"""
        return self._has_control

    @property
    def priority(self) -> ControlPriorityLevel:
        """The currently desired priority for the SDK."""
        return self._priority

    @property
    def is_shutdown(self) -> bool:
        """Detect if the behavior control stream is supposed to shut down."""
        return self._is_shutdown

    def request(
        self, priority: ControlPriorityLevel = ControlPriorityLevel.DEFAULT_PRIORITY
    ) -> None:
        """Tell the behavior stream to request control via setting the :class:`request_event`.

        This will signal Connection's :func:`_request_handler` generator to send a request control message on the BehaviorControl stream.
        This signal happens asynchronously, and can be tracked using the :class:`granted_event` parameter.

        :param priority: The level of control in the behavior system. This determines which actions are allowed to
            interrupt the SDK execution. See :class:`ControlPriorityLevel` for more information.
        """
        if priority is None:
            raise VectorBehaviorControlException(
                "Must provide a priority level to request. To disable control, use {}.release().",
                self.__class__.__name__,
            )
        self._priority = priority
        self._request_event.set()

    def release(self) -> None:
        """Tell the behavior stream to release control via setting the :class:`request_event` while priority is ``None``.

        This will signal Connection's :func:`_request_handler` generator to send a release control message on the BehaviorControl stream.
        This signal happens asynchronously, and can be tracked using the :class:`lost_event` parameter.
        """
        self._priority = None
        self._request_event.set()

    def update(self, enabled: bool) -> None:
        """Update the current state of control (either enabled or disabled)

        :param enabled: Used to enable/disable behavior control
        """
        self._has_control = enabled
        if enabled:
            self._granted_event.set()
            self._lost_event.clear()
        else:
            self._lost_event.set()
            self._granted_event.clear()

    def shutdown(self) -> None:
        """Tells the control stream to shut down.

        This will return control to the rest of the behavior system.
        """
        self._has_control = False
        self._granted_event.set()
        self._lost_event.set()
        self._is_shutdown = True
        self._request_event.set()


class Connection:
    """Connection class customized for Home Assistant usage."""

    def __init__(
        self,
        name: str,
        host: str,
        cert_file: str,
        guid: str,
        loop: AbstractEventLoop,
        escape_pod: bool = False,
        behavior_control_level: ControlPriorityLevel = ControlPriorityLevel.NONE,
        logger: Any | None = None,
    ):
        self._loop = loop
        self.name = name
        self.host = host
        self.cert_file = cert_file
        self._escape_pod = escape_pod
        self._interface = None
        self._channel = None
        self._has_control = False
        self._control_stream_task = None
        self._control_events: _ControlEventManager = None
        self._guid = guid
        self._thread: threading.Thread = None
        self._ready_signal: threading.Event = threading.Event()
        self._done_signal: asyncio.Event = None
        self._conn_exception = False
        self._behavior_control_level = behavior_control_level
        self.active_commands = []
        self._logger = logger

    @property
    def loop(self) -> AbstractEventLoop:
        """Returns the loop running inside the connection thread."""
        if self._loop is None:
            raise VectorAsyncException(
                "Attempted to access the connection loop before it was ready"
            )
        return self._loop

    @property
    def thread(self) -> threading.Thread:
        """Returns the connection thread where all of the grpc messages are being processed."""
        if self._thread is None:
            raise VectorAsyncException(
                "Attempted to access the connection loop before it was ready"
            )
        return self._thread

    @property
    def grpc_interface(self) -> client.ExternalInterfaceStub:
        """A direct reference to the connected aiogrpc interface."""
        return self._interface

    @property
    def behavior_control_level(self) -> ControlPriorityLevel:
        """Returns the specific `ControlPriorityLevel` requested for behavior control."""
        return self._behavior_control_level

    @property
    def requires_behavior_control(self) -> bool:
        """True if the `Connection` requires behavior control."""
        return self._behavior_control_level is not None

    @property
    def control_lost_event(self) -> asyncio.Event:
        """This provides an `asyncio.Event` that a user may `wait()` upon to
        detect when Vector has taken control of the behavior system at a higher priority."""
        return self._control_events.lost_event

    @property
    def control_granted_event(self) -> asyncio.Event:
        """This provides an `asyncio.Event` that a user may `wait()` upon to
        detect when Vector has given control of the behavior system to the SDK program."""
        return self._control_events.granted_event

    def request_control(
        self,
        behavior_control_level: ControlPriorityLevel = ControlPriorityLevel.DEFAULT_PRIORITY,
        timeout: float = 10.0,
    ):
        """Explicitly request behavior control. Typically used after detecting
        `control_lost_event` or when behavior control is required."""
        if not isinstance(behavior_control_level, ControlPriorityLevel):
            raise TypeError(
                "behavior_control_level must be of type ControlPriorityLevel"
            )
        if self._thread is threading.current_thread():
            return asyncio.ensure_future(
                self._request_control(
                    behavior_control_level=behavior_control_level, timeout=timeout
                )
            )
        return self.run_coroutine(
            self._request_control(
                behavior_control_level=behavior_control_level, timeout=timeout
            )
        )

    async def _request_control(
        self,
        behavior_control_level: ControlPriorityLevel = ControlPriorityLevel.DEFAULT_PRIORITY,
        timeout: float = 10.0,
    ):
        self._behavior_control_level = behavior_control_level
        self._control_events.request(self._behavior_control_level)
        try:
            self._has_control = await asyncio.wait_for(
                self.control_granted_event.wait(), timeout
            )
        except futures.TimeoutError as e:
            raise VectorControlTimeoutException(
                f"Surpassed timeout of {timeout}s"
            ) from e

    def release_control(self, timeout: float = 10.0):
        """Explicitly release control. Typically used after detecting `control_lost_event`."""
        if self._thread is threading.current_thread():
            return asyncio.ensure_future(self._release_control(timeout=timeout))
        return self.run_coroutine(self._release_control(timeout=timeout))

    async def _release_control(self, timeout: float = 10.0):
        self._behavior_control_level = None
        self._control_events.release()
        try:
            self._has_control = await asyncio.wait_for(
                self.control_lost_event.wait(), timeout
            )
        except futures.TimeoutError as e:
            raise VectorControlTimeoutException(
                f"Surpassed timeout of {timeout}s"
            ) from e

    def connect(self, timeout: float = 10.0) -> None:
        """Connect to Vector. This will start the connection thread which handles all messages
        between Vector and this module."""
        if self._thread:
            raise VectorAsyncException(
                "\n\nRepeated connections made to open Connection."
            )

        self._ready_signal.clear()
        self._thread = threading.Thread(
            target=self._connect,
            args=(timeout,),
            daemon=True,
            name="gRPC Connection Handler Thread",
        )
        self._thread.start()
        ready = self._ready_signal.wait(timeout=4 * timeout)

        if not ready:
            raise VectorNotFoundException()

        if hasattr(self._ready_signal, "exception"):
            e = getattr(self._ready_signal, "exception")
            delattr(self._ready_signal, "exception")
            raise e

    def _connect(self, timeout: float) -> None:
        """The function that runs on the connection thread. This will connect to Vector,
        and establish the BehaviorControl stream.
        """
        try:
            if threading.main_thread() is threading.current_thread():
                raise VectorAsyncException(
                    "\n\nConnection._connect must be run outside of the main thread."
                )
            self._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._loop)
            self._done_signal = asyncio.Event()
            if not self._behavior_control_level:
                self._control_events = _ControlEventManager(self._loop)
            else:
                self._control_events = _ControlEventManager(
                    self._loop, priority=self._behavior_control_level
                )

            trusted_certs = None
            if not self.cert_file is None:
                with open(self.cert_file, "rb") as cert:
                    trusted_certs = cert.read()
            else:
                if not self._escape_pod:
                    raise VectorConfigurationException(
                        "Must provide a cert file to authenticate to Vector."
                    )

            # Not ready for implementation yet
            # if self._escape_pod:
            #     if not EscapePod.validate_certificate_name(self.cert_file, self.name):
            #         trusted_certs = EscapePod.get_authentication_certificate(self.host)
            #         self.name = EscapePod.get_certificate_name(trusted_certs)
            #     self._guid = EscapePod.authenticate_escape_pod(self.host, self.name, trusted_certs)

            # Pin the robot certificate for opening the channel
            channel_credentials = aiogrpc.ssl_channel_credentials(
                root_certificates=trusted_certs
            )
            # Add authorization header for all the calls
            call_credentials = aiogrpc.access_token_call_credentials(self._guid)

            credentials = aiogrpc.composite_channel_credentials(
                channel_credentials, call_credentials
            )

            self._logger.debug(
                f"Connecting to {self.host} for {self.name} using {self.cert_file}"
            )
            self._channel = aiogrpc.secure_channel(
                self.host,
                credentials,
                options=(
                    (
                        "grpc.ssl_target_name_override",
                        self.name,
                    ),
                ),
            )

            # Verify the connection to Vector is able to be established (client-side)
            try:
                # Explicitly grab _channel._channel to test the underlying grpc channel directly
                grpc.channel_ready_future(self._channel._channel).result(
                    timeout=timeout
                )  # pylint: disable=protected-access
            except grpc.FutureTimeoutError as e:
                raise VectorNotFoundException() from e

            self._interface = client.ExternalInterfaceStub(self._channel)

            # Verify Vector and the SDK have compatible protocol versions
            version = protocol.ProtocolVersionRequest(
                client_version=protocol.PROTOCOL_VERSION_CURRENT,
                min_host_version=protocol.PROTOCOL_VERSION_MINIMUM,
            )
            protocol_version = self._loop.run_until_complete(
                self._interface.ProtocolVersion(version)
            )
            if (
                protocol_version.result != protocol.ProtocolVersionResponse.SUCCESS
                or protocol.PROTOCOL_VERSION_MINIMUM > protocol_version.host_version
            ):  # pylint: disable=no-member
                raise VectorInvalidVersionException(protocol_version)

            self._control_stream_task = self._loop.create_task(self._open_connections())

            # Initialze SDK
            sdk_module_version = __version__
            python_version = platform.python_version()
            python_implementation = platform.python_implementation()
            os_version = platform.platform()
            cpu_version = platform.machine()
            initialize = protocol.SDKInitializationRequest(
                sdk_module_version=sdk_module_version,
                python_version=python_version,
                python_implementation=python_implementation,
                os_version=os_version,
                cpu_version=cpu_version,
            )
            self._loop.run_until_complete(self._interface.SDKInitialization(initialize))

            if self._behavior_control_level:
                self._loop.run_until_complete(
                    self._request_control(
                        behavior_control_level=self._behavior_control_level,
                        timeout=timeout,
                    )
                )
        except grpc.RpcError as rpc_error:  # pylint: disable=broad-except
            setattr(self._ready_signal, "exception", connection_error(rpc_error))
            self._loop.close()
            return
        except Exception as e:  # pylint: disable=broad-except
            # Propagate the errors to the calling thread
            setattr(self._ready_signal, "exception", e)
            self._loop.close()
            return
        finally:
            self._ready_signal.set()

        try:

            async def wait_until_done():
                return await self._done_signal.wait()

            self._loop.run_until_complete(wait_until_done())
        finally:
            self._loop.close()

    async def _request_handler(self):
        """Handles generating messages for the BehaviorControl stream."""
        while await self._control_events.request_event.wait():
            self._control_events.request_event.clear()
            if self._control_events.is_shutdown:
                return
            priority = self._control_events.priority
            if priority is None:
                msg = protocol.ControlRelease()
                msg = protocol.BehaviorControlRequest(control_release=msg)
            else:
                msg = protocol.ControlRequest(priority=priority.value)
                msg = protocol.BehaviorControlRequest(control_request=msg)
            self._logger.debug(
                f"BehaviorControl {MessageToString(msg, as_one_line=True)}"
            )
            yield msg

    async def _open_connections(self):
        """Starts the BehaviorControl stream, and handles the messages coming back from the robot."""
        try:
            async for response in self._interface.BehaviorControl(
                self._request_handler()
            ):
                response_type = response.WhichOneof("response_type")
                if response_type == "control_granted_response":
                    self._logger.info(
                        f"BehaviorControl {MessageToString(response, as_one_line=True)}"
                    )
                    self._control_events.update(True)
                elif response_type == "control_lost_event":
                    self._cancel_active()
                    self._logger.info(
                        f"BehaviorControl {MessageToString(response, as_one_line=True)}"
                    )
                    self._control_events.update(False)
        except futures.CancelledError:
            self._logger.debug(
                "Behavior handler task was cancelled. This is expected during disconnection."
            )

    def _cancel_active(self):
        for fut in self.active_commands:
            if not fut.done():
                fut.cancel()
        self.active_commands = []

    def close(self):
        """Cleanup the connection, and shutdown all the event handlers."""
        try:
            if self._control_events:
                self._control_events.shutdown()
            if self._control_stream_task:
                self._control_stream_task.cancel()
                self.run_coroutine(self._control_stream_task).result()
            self._cancel_active()
            if self._channel:
                self.run_coroutine(self._channel.close()).result()
            self.run_coroutine(self._done_signal.set)
            self._thread.join(timeout=5)
        except:
            pass
        finally:
            self._thread = None

    def run_soon(self, coro: Awaitable) -> None:
        """Schedules the given awaitable to run on the event loop for the connection thread."""
        if coro is None or not inspect.isawaitable(coro):
            raise VectorAsyncException(
                f"\n\n{coro.__name__ if hasattr(coro, '__name__') else coro} is not awaitable, so cannot be ran with run_soon.\n"
            )

        def soon():
            try:
                asyncio.ensure_future(coro)
            except TypeError as e:
                raise VectorAsyncException(
                    f"\n\n{coro.__name__ if hasattr(coro, '__name__') else coro} could not be ensured as a future.\n"
                ) from e

        if threading.current_thread() is self._thread:
            self._loop.call_soon(soon)
        else:
            self._loop.call_soon_threadsafe(soon)

    def run_coroutine(self, coro: Awaitable) -> Any:
        """Runs a given awaitable on the connection thread's event loop.
        Cannot be called from within the connection thread."""
        if threading.current_thread() is self._thread:
            raise VectorAsyncException(
                "Attempting to invoke async from same thread."
                "Instead you may want to use 'run_soon'"
            )
        if asyncio.iscoroutinefunction(coro) or asyncio.iscoroutine(coro):
            return self._run_coroutine(coro)
        if asyncio.isfuture(coro):

            async def future_coro():
                return await coro

            return self._run_coroutine(future_coro())
        if callable(coro):

            async def wrapped_coro():
                return coro()

            return self._run_coroutine(wrapped_coro())
        raise VectorAsyncException(
            "\n\nInvalid parameter to run_coroutine: {}\n"
            "This function expects a coroutine, task, or awaitable.".format(type(coro))
        )

    def _run_coroutine(self, coro):
        return asyncio.run_coroutine_threadsafe(coro, self._loop)


def on_connection_thread(
    log_messaging: bool = True,
    requires_control: bool = True,
    is_cancellable: CancelType = None,
) -> Callable[[Coroutine[util.Component, Any, None]], Any]:
    """A decorator generator used internally to denote which functions will run on
    the connection thread. This unblocks the caller of the wrapped function
    and allows them to continue running while the messages are being processed.
    """

    def _on_connection_thread_decorator(func: Coroutine) -> Any:
        """A decorator which specifies a function to be executed on the connection thread

        :params func: The function to be decorated
        :returns: There are 3 possible returns based on context: the result of the decorated function,
            the :class:`concurrent.futures.Future` which points to the decorated function, or the
            :class:`asyncio.Future` which points to the decorated function.
            These contexts are: when the robot is a :class:`anki_vector.robot.Robot`,
            when the robot is an :class:`anki_vector.robot.AsyncRobot`, and when
            called from the connection thread respectively.
        """
        if not asyncio.iscoroutinefunction(func):
            raise VectorAsyncException(
                "\n\nCannot define non-coroutine function '{}' to run on connection thread.\n"
                "Make sure the function is defined using 'async def'.".format(
                    func.__name__ if hasattr(func, "__name__") else func
                )
            )

        @functools.wraps(func)
        async def log_handler(
            conn: Connection,
            func: Coroutine,
            logger: logging.Logger,
            *args: List[Any],
            **kwargs: Dict[str, Any],
        ) -> Coroutine:
            """Wrap the provided coroutine to better express exceptions as specific :class:`anki_vector.exceptions.VectorException`s, and
            adds logging to incoming (from the robot) and outgoing (to the robot) messages.
            """
            result = None
            # TODO: only have the request wait for control if we're not done. If done raise an exception.
            control = conn.control_granted_event
            if requires_control and not control.is_set():
                if not conn.requires_behavior_control:
                    raise VectorControlException(func.__name__)
                logger.info(
                    f"Delaying {func.__name__} until behavior control is granted"
                )
                await asyncio.wait([conn.control_granted_event.wait()], timeout=10)
            message = args[1:]
            outgoing = (
                message
                if log_messaging
                else "size = {} bytes".format(sys.getsizeof(message))
            )
            logger.debug(f"Outgoing {func.__name__}: {outgoing}")
            try:
                result = await func(*args, **kwargs)
            except grpc.RpcError as rpc_error:
                raise connection_error(rpc_error) from rpc_error
            incoming = (
                str(result).strip()
                if log_messaging
                else "size = {} bytes".format(sys.getsizeof(result))
            )
            logger.debug(
                f"Incoming {func.__name__}: {type(result).__name__}  {incoming}"
            )
            return result

        @functools.wraps(func)
        def result(*args: List[Any], **kwargs: Dict[str, Any]) -> Any:
            """The function that is the result of the decorator. Provides a wrapped function.

            :param _return_future: A hidden parameter which allows the wrapped function to explicitly
                return a future (default for AsyncRobot) or not (default for Robot).
            :returns: Based on context this can return the result of the decorated function,
                the :class:`concurrent.futures.Future` which points to the decorated function, or the
                :class:`asyncio.Future` which points to the decorated function.
                These contexts are: when the robot is a :class:`anki_vector.robot.Robot`,
                when the robot is an :class:`anki_vector.robot.AsyncRobot`, and when
                called from the connection thread respectively."""
            self = args[0]  # Get the self reference from the function call
            # if the call supplies a _return_future parameter then override force_async with that.
            _return_future = kwargs.pop("_return_future", self.force_async)

            action_id = None
            if is_cancellable == CancelType.CANCELLABLE_ACTION:
                action_id = self._get_next_action_id()
                kwargs["_action_id"] = action_id

            wrapped_coroutine = log_handler(
                self.conn, func, self.logger, *args, **kwargs
            )

            if threading.current_thread() == self.conn.thread:
                if self.conn.loop.is_running():
                    return asyncio.ensure_future(wrapped_coroutine)
                raise VectorAsyncException(
                    "\n\nThe connection thread loop is not running, but a "
                    "function '{}' is being invoked on that thread.\n".format(
                        func.__name__ if hasattr(func, "__name__") else func
                    )
                )
            future = asyncio.run_coroutine_threadsafe(wrapped_coroutine, self.conn.loop)

            if is_cancellable == CancelType.CANCELLABLE_ACTION:

                def user_cancelled_action(fut):
                    if action_id is None:
                        return

                    if fut.cancelled():
                        self._abort_action(action_id)

                future.add_done_callback(user_cancelled_action)

            if is_cancellable == CancelType.CANCELLABLE_BEHAVIOR:

                def user_cancelled_behavior(fut):
                    if fut.cancelled():
                        self._abort_behavior()

                future.add_done_callback(user_cancelled_behavior)

            if requires_control:
                self.conn.active_commands.append(future)

                def clear_when_done(fut):
                    if fut in self.conn.active_commands:
                        self.conn.active_commands.remove(fut)

                future.add_done_callback(clear_when_done)
            if _return_future:
                return future
            try:
                return future.result()
            except futures.CancelledError:
                self.logger.warning(
                    f"{func.__name__} cancelled because behavior control was lost"
                )
                return None

        return result

    return _on_connection_thread_decorator
