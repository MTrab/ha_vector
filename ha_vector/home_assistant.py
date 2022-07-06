"""Home Assistant specific calls."""
from __future__ import annotations

__all__ = ["API", "Robot"]

import functools
import logging
import os
import platform
import socket
from asyncio import AbstractEventLoop
from typing import Any

import concurrent
import grpc
from cryptography import x509
from cryptography.hazmat.backends import default_backend

from . import (
    animation,
    audio,
    behavior,
    camera,
    events,
    faces,
    messaging,
    motors,
    nav_map,
    photos,
    proximity,
    screen,
    status,
    touch,
    util,
    viewer,
    vision,
    world,
)
from .connection import Connection, ControlPriorityLevel, on_connection_thread
from .exceptions import (
    VectorHomeAssistantEscapepodException,
    VectorNotReadyException,
    VectorPropertyValueNotReadyException,
    VectorUnreliableEventStreamException,
)
from .mdns import VectorMdns
from .messaging import client, protocol
from .viewer import Viewer3DComponent, ViewerComponent
from .version import __version__

_LOGGER = logging.getLogger(__name__)

# API/SDK consts
ANKI_APP_KEY = "aung2ieCho3aiph7Een3Ei"
API_URL = "https://accounts.api.anki.com/1/sessions"
TOKEN_URL = "https://session-certs.token.global.anki-services.com/vic/"
USER_AGENT = f"Vector-sdk-HomeAssistant/{platform.python_implementation()}/{platform.python_version()}"


class APIHandler:
    """Define API handler."""

    def __init__(self, headers: dict, url: str):
        self._headers = headers
        self._url = url

    @property
    def headers(self):
        """Return headers."""
        return self._headers

    @property
    def url(self):
        """Return URL."""
        return self._url


class API:
    """Define API instance."""

    def __init__(
        self,
        email: str,
        password: str,
        name: str,
        serial: str,
        ipaddress: str,
        cert_path: str,
        client,
    ):
        """Initialize instance."""
        # Initializer info
        self._client = client
        self._email = email
        self._ip = ipaddress
        self._name = name
        self._password = password
        self._serial = serial
        self._cert_path = cert_path

        # Vars used in the API integration
        self._cert = None
        self._cert_file = None
        self._guid = None
        self._handler = APIHandler(
            headers={
                "User-Agent": USER_AGENT,
                "Anki-App-Key": ANKI_APP_KEY,
            },
            url=API_URL,
        )
        self._token = None

    @property
    def name(self):
        """Return name."""
        return "Anki Cloud"

    @property
    def handler(self):
        """Return handler."""
        return self._handler

    async def async_configure(self) -> None:
        """Do the required SDK configuration steps."""
        await self._async_get_cert()
        await self._async_save_cert()
        await self._async_validate_cert_name()
        await self._async_get_session_token()
        await self._async_user_authentication()

    async def _async_get_cert(self) -> bytes:
        """Get Vector certificate."""
        res = await self._client.get(f"{TOKEN_URL}{self._serial}")
        if res.status != 200:
            raise Exception("Could not get Vector certificate")

        self._cert = await res.read()

    async def _async_save_cert(self) -> str:
        """Write Vector's certificate to a file located in the user's home directory"""
        os.makedirs(str(self._cert_path), exist_ok=True)
        self._cert_file = str(
            self._cert_path + "/" + f"{self._name}-{self._serial}.cert"
        )
        with os.fdopen(
            os.open(self._cert_file, os.O_WRONLY | os.O_CREAT, 0o600), "wb"
        ) as file:
            file.write(self._cert)
        return self._cert_file

    async def _async_validate_cert_name(self):
        """Validate the name on Vector's certificate against the user-provided name"""
        with open(self._cert_file, "rb") as file:
            cert_file = file.read()
            cert = x509.load_pem_x509_certificate(cert_file, default_backend())
            for fields in cert.subject:
                current = str(fields.oid)
                if "commonName" in current:
                    common_name = fields.value
                    if common_name != self._name:
                        raise Exception(
                            f"The name of the certificate ({common_name}) does "
                            "not match the name provided ({self._name}).\n"
                            "Please verify the name, and try again."
                        )

    async def _async_get_session_token(self) -> str:
        """Get Vector session token."""
        payload = {"username": self._email, "password": self._password}

        res = await self._client.post(
            self._handler.url, data=payload, headers=self._handler.headers
        )
        if res.status != 200:
            raise Exception("Error fetching session token.")

        self._token = await res.json(content_type="text/json")

    async def _async_user_authentication(self) -> str:
        """Authenticate against the API."""
        # Pin the robot certificate for opening the channel
        creds = grpc.ssl_channel_credentials(root_certificates=self._cert)

        channel = grpc.secure_channel(
            f"{self._ip}:443",
            creds,
            options=(
                (
                    "grpc.ssl_target_name_override",
                    self._name,
                ),
            ),
        )

        # Verify the connection to Vector is able to be established (client-side)
        try:
            # Explicitly grab _channel._channel to test the underlying grpc channel directly
            grpc.channel_ready_future(channel).result(timeout=15)
        except grpc.FutureTimeoutError as err:
            raise Exception(
                "\nUnable to connect to Vector\n"
                "Please be sure to connect via the Vector companion app first, "
                "and connect your computer to the same network as your Vector."
            ) from err

        try:
            interface = messaging.client.ExternalInterfaceStub(channel)
            request = messaging.protocol.UserAuthenticationRequest(
                user_session_id=self._token["session"]["session_token"].encode("utf-8"),
                client_name=socket.gethostname().encode("utf-8"),
            )
            response = interface.UserAuthentication(request)
            if (
                response.code
                != messaging.protocol.UserAuthenticationResponse.AUTHORIZED  # pylint: disable=no-member
            ):
                raise Exception(
                    "\nFailed to authorize request:\n"
                    "Please be sure to first set up Vector using the companion app."
                )
        except grpc.RpcError as err:
            raise Exception(
                "\nFailed to authorize request:\n" "An unknown error occurred '{err}'"
            ) from err

        self._guid = response.client_token_guid

    @property
    def guid(self) -> str:
        """Return the GUID for this Vector."""
        return str(self._guid)

    @property
    def certificate(self) -> str:
        """Returns the certificate file and path for this Vector."""
        return str(self._cert_file)


### Home Assistant Rewrite


class Robot:
    """Vector Robot class customized for Home Assistant usage."""

    def __init__(
        self,
        serial: str,
        ip: str,
        name: str,
        config: dict,
        loop: AbstractEventLoop,
        escape_pod: bool = False,
        logger: Any | None = None,
        behavior_activation_timeout: int = 10,
        cache_animation_lists: bool = False,
        enable_face_detection: bool = True,
        estimate_facial_expression: bool = True,
        enable_audio_feed: bool = False,
        enable_custom_object_detection: bool = False,
        enable_nav_map_feed: bool | None = None,
        show_viewer: bool = False,
        show_3d_viewer: bool = False,
        behavior_control_level: ControlPriorityLevel | None = None,
    ):
        if not isinstance(logger, type(None)):
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)

        self._config = config
        self._loop = loop

        self._escape_pod = escape_pod
        self._name = self._config["name"] if "name" in self._config else name
        self._cert_file = self._config["cert"] if "cert" in self._config else None
        self._guid = self._config["guid"] if "guid" in self._config else None
        self._port = self._config["port"] if "port" in self._config else "443"
        self._ip = self._config["ip"] if "ip" in self._config else ip
        self._serial = self._config["serial"] if "serial" in self._config else serial

        if escape_pod:
            raise VectorHomeAssistantEscapepodException(
                "Escape Pod is currently not supported!"
            )

        self._conn = Connection(
            name=self._name,
            host=":".join([self._ip, self._port]),
            cert_file=self._cert_file,
            guid=self._guid,
            escape_pod=self._escape_pod,
            behavior_control_level=behavior_control_level,
            loop=self._loop,
            logger=self.logger,
        )

        self._events = events.EventHandler(self)

        # placeholders for components before they exist
        self._anim: animation.AnimationComponent = None
        self._audio: audio.AudioComponent = None
        self._behavior: behavior.BehaviorComponent = None
        self._camera: camera.CameraComponent = None
        self._faces: faces.FaceComponent = None
        self._motors: motors.MotorComponent = None
        self._nav_map: nav_map.NavMapComponent = None
        self._screen: screen.ScreenComponent = None
        self._photos: photos.PhotographComponent = None
        self._proximity: proximity.ProximityComponent = None
        self._touch: touch.TouchComponent = None
        self._viewer: viewer.ViewerComponent = None
        self._viewer_3d: viewer.Viewer3DComponent = None
        self._vision: vision.VisionComponent = None
        self._world: world.World = None

        self.behavior_activation_timeout = behavior_activation_timeout
        self.enable_face_detection = enable_face_detection
        self.estimate_facial_expression = estimate_facial_expression
        self.enable_custom_object_detection = enable_custom_object_detection
        self.cache_animation_lists = cache_animation_lists

        # Robot state/sensor data
        self._pose: util.Pose = None
        self._pose_angle_rad: float = None
        self._pose_pitch_rad: float = None
        self._left_wheel_speed_mmps: float = None
        self._right_wheel_speed_mmps: float = None
        self._head_angle_rad: float = None
        self._lift_height_mm: float = None
        self._accel: util.Vector3 = None
        self._gyro: util.Vector3 = None
        self._carrying_object_id: float = None
        self._head_tracking_object_id: float = None
        self._localized_to_object_id: float = None
        self._last_image_time_stamp: float = None
        self._status: status.RobotStatus = status.RobotStatus()

        self._enable_audio_feed = enable_audio_feed
        if enable_nav_map_feed is not None:
            self._enable_nav_map_feed = enable_nav_map_feed
        else:
            self._enable_nav_map_feed = False
        self._show_viewer = show_viewer
        self._show_3d_viewer = show_3d_viewer
        if show_3d_viewer and enable_nav_map_feed is None:
            self.logger.warning(
                "enable_nav_map_feed should be True for 3d viewer to render correctly."
            )
            self._enable_nav_map_feed = True

    @property
    def force_async(self) -> bool:
        """A flag used to determine if this is a :class:`Robot` or :class:`AsyncRobot`."""
        return True

    @property
    def conn(self) -> Connection:
        """A reference to the :class:`~anki_vector.connection.Connection` instance."""
        return self._conn

    @property
    def events(self) -> events.EventHandler:
        """A reference to the :class:`~anki_vector.events.EventHandler` instance."""
        return self._events

    @property
    def anim(self) -> animation.AnimationComponent:
        """A reference to the :class:`~anki_vector.animation.AnimationComponent` instance."""
        if self._anim is None:
            raise VectorNotReadyException("AnimationComponent is not yet initialized")
        return self._anim

    @property
    def audio(self) -> audio.AudioComponent:
        """The audio instance used to control Vector's microphone feed and speaker playback."""

        if self._audio is None:
            raise VectorNotReadyException("AudioComponent is not yet initialized")
        return self._audio

    @property
    def behavior(self) -> behavior.BehaviorComponent:
        """A reference to the :class:`~anki_vector.behavior.BehaviorComponent` instance."""
        return self._behavior

    @property
    def camera(self) -> camera.CameraComponent:
        """The :class:`~anki_vector.camera.CameraComponent` instance used to control Vector's camera feed.

        .. testcode::

            import anki_vector

            with anki_vector.Robot() as robot:
                robot.camera.init_camera_feed()
                image = robot.camera.latest_image
                image.raw_image.show()
        """
        if self._camera is None:
            raise VectorNotReadyException("CameraComponent is not yet initialized")
        return self._camera

    @property
    def faces(self) -> faces.FaceComponent:
        """A reference to the :class:`~anki_vector.faces.FaceComponent` instance."""
        if self._faces is None:
            raise VectorNotReadyException("FaceComponent is not yet initialized")
        return self._faces

    @property
    def motors(self) -> motors.MotorComponent:
        """A reference to the :class:`~anki_vector.motors.MotorComponent` instance."""
        if self._motors is None:
            raise VectorNotReadyException("MotorComponent is not yet initialized")
        return self._motors

    @property
    def nav_map(self) -> nav_map.NavMapComponent:
        """A reference to the :class:`~anki_vector.nav_map.NavMapComponent` instance."""
        if self._nav_map is None:
            raise VectorNotReadyException("NavMapComponent is not yet initialized")
        return self._nav_map

    @property
    def screen(self) -> screen.ScreenComponent:
        """A reference to the :class:`~anki_vector.screen.ScreenComponent` instance."""
        if self._screen is None:
            raise VectorNotReadyException("ScreenComponent is not yet initialized")
        return self._screen

    @property
    def photos(self) -> photos.PhotographComponent:
        """A reference to the :class:`~anki_vector.photos.PhotographComponent` instance."""
        if self._photos is None:
            raise VectorNotReadyException("PhotographyComponent is not yet initialized")
        return self._photos

    @property
    def proximity(self) -> proximity.ProximityComponent:
        """:class:`~anki_vector.proximity.ProximityComponent` containing state related to object proximity detection.

        .. code-block:: python

            import anki_vector
            with anki_vector.Robot() as robot:
                proximity_data = robot.proximity.last_sensor_reading
                if proximity_data is not None:
                    print(proximity_data.distance)
        """
        return self._proximity

    @property
    def touch(self) -> touch.TouchComponent:
        """:class:`~anki_vector.touch.TouchComponent` containing state related to object touch detection.

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                print('Robot is being touched: {0}'.format(robot.touch.last_sensor_reading.is_being_touched))
        """
        return self._touch

    @property
    def viewer(self) -> ViewerComponent:
        """The :class:`~anki_vector.viewer.ViewerComponent` instance used to render Vector's camera feed.

        .. testcode::

            import time

            import anki_vector

            with anki_vector.Robot() as robot:
                # Render video for 5 seconds
                robot.viewer.show()
                time.sleep(5)

                # Disable video render and camera feed for 5 seconds
                robot.viewer.close()
        """
        if self._viewer is None:
            raise VectorNotReadyException("ViewerComponent is not yet initialized")
        return self._viewer

    @property
    def viewer_3d(self) -> Viewer3DComponent:
        """The :class:`~anki_vector.viewer.Viewer3DComponent` instance used to render Vector's navigation map.

        .. testcode::

            import time

            import anki_vector

            with anki_vector.Robot(show_3d_viewer=True, enable_nav_map_feed=True) as robot:
                # Render 3D view of navigation map for 5 seconds
                time.sleep(5)
        """
        if self._viewer_3d is None:
            raise VectorNotReadyException("Viewer3DComponent is not yet initialized")
        return self._viewer_3d

    @property
    def vision(self) -> vision.VisionComponent:
        """:class:`~anki_vector.vision.VisionComponent` containing functionality related to vision based object detection.

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                robot.vision.enable_custom_object_detection()
        """
        return self._vision

    @property
    def world(self) -> world.World:
        """A reference to the :class:`~anki_vector.world.World` instance, or None if the World is not yet initialized."""
        if self._world is None:
            raise VectorNotReadyException("WorldComponent is not yet initialized")
        return self._world

    @property
    @util.block_while_none()
    def pose(self) -> util.Pose:
        """:class:`anki_vector.util.Pose`: The current pose (position and orientation) of Vector.

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_robot_pose = robot.pose
        """
        return self._pose

    @property
    @util.block_while_none()
    def pose_angle_rad(self) -> float:
        """Vector's pose angle (heading in X-Y plane).

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_pose_angle_rad = robot.pose_angle_rad
        """
        return self._pose_angle_rad

    @property
    @util.block_while_none()
    def pose_pitch_rad(self) -> float:
        """Vector's pose pitch (angle up/down).

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_pose_pitch_rad = robot.pose_pitch_rad
        """
        return self._pose_pitch_rad

    @property
    @util.block_while_none()
    def left_wheel_speed_mmps(self) -> float:
        """Vector's left wheel speed in mm/sec

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_left_wheel_speed_mmps = robot.left_wheel_speed_mmps
        """
        return self._left_wheel_speed_mmps

    @property
    @util.block_while_none()
    def right_wheel_speed_mmps(self) -> float:
        """Vector's right wheel speed in mm/sec

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_right_wheel_speed_mmps = robot.right_wheel_speed_mmps
        """
        return self._right_wheel_speed_mmps

    @property
    @util.block_while_none()
    def head_angle_rad(self) -> float:
        """Vector's head angle (up/down).

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_head_angle_rad = robot.head_angle_rad
        """
        return self._head_angle_rad

    @property
    @util.block_while_none()
    def lift_height_mm(self) -> float:
        """Height of Vector's lift from the ground.

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_lift_height_mm = robot.lift_height_mm
        """
        return self._lift_height_mm

    @property
    @util.block_while_none()
    def accel(self) -> util.Vector3:
        """:class:`anki_vector.util.Vector3`: The current accelerometer reading (x, y, z)

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_accel = robot.accel
        """
        return self._accel

    @property
    @util.block_while_none()
    def gyro(self) -> util.Vector3:
        """The current gyroscope reading (x, y, z)

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_gyro = robot.gyro
        """
        return self._gyro

    @property
    @util.block_while_none()
    def carrying_object_id(self) -> int:
        """The ID of the object currently being carried (-1 if none)

        .. testcode::

            import anki_vector
            from anki_vector.util import degrees

            # Set the robot so that he can see a cube.
            with anki_vector.Robot() as robot:
                robot.behavior.set_head_angle(degrees(0.0))
                robot.behavior.set_lift_height(0.0)

                robot.world.connect_cube()

                if robot.world.connected_light_cube:
                    robot.behavior.pickup_object(robot.world.connected_light_cube)

                print("carrying_object_id: ", robot.carrying_object_id)
        """
        return self._carrying_object_id

    @property
    @util.block_while_none()
    def head_tracking_object_id(self) -> int:
        """The ID of the object the head is tracking to (-1 if none)

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_head_tracking_object_id = robot.head_tracking_object_id
        """
        return self._head_tracking_object_id

    @property
    @util.block_while_none()
    def localized_to_object_id(self) -> int:
        """The ID of the object that the robot is localized to (-1 if none)

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_localized_to_object_id = robot.localized_to_object_id
        """
        return self._localized_to_object_id

    # TODO Move to photos or somewhere else
    @property
    @util.block_while_none()
    def last_image_time_stamp(self) -> int:
        """The robot's timestamp for the last image seen.

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                current_last_image_time_stamp = robot.last_image_time_stamp
        """
        return self._last_image_time_stamp

    @property
    def status(self) -> status.RobotStatus:
        """A property that exposes various status properties of the robot.

        This status provides a simple mechanism to, for example, detect if any
        of Vector's motors are moving, determine if Vector is being held, or if
        he is on the charger.  The full list is available in the
        :class:`RobotStatus <anki_vector.status.RobotStatus>` class documentation.

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                if robot.status.is_being_held:
                    print("Vector is being held!")
                else:
                    print("Vector is not being held.")
        """
        return self._status

    @property
    def enable_audio_feed(self) -> bool:
        """The audio feed enabled/disabled

        :getter: Returns whether the audio feed is enabled
        :setter: Enable/disable the audio feed

        .. code-block:: python

            import asyncio
            import time

            import anki_vector

            with anki_vector.Robot(enable_audio_feed=True) as robot:
                time.sleep(5)
                robot.enable_audio_feed = False
                time.sleep(5)
        """
        # TODO When audio is ready, convert `.. code-block:: python` to `.. testcode::`
        return self._enable_audio_feed

    @enable_audio_feed.setter
    def enable_audio_feed(self, enable) -> None:
        self._enable_audio_feed = enable
        # TODO add audio feed enablement when ready

    # Unpack streamed data to robot's internal properties
    def _unpack_robot_state(self, _robot, _event_type, msg):
        self._pose = util.Pose(
            x=msg.pose.x,
            y=msg.pose.y,
            z=msg.pose.z,
            q0=msg.pose.q0,
            q1=msg.pose.q1,
            q2=msg.pose.q2,
            q3=msg.pose.q3,
            origin_id=msg.pose.origin_id,
        )
        self._pose_angle_rad = msg.pose_angle_rad
        self._pose_pitch_rad = msg.pose_pitch_rad
        self._left_wheel_speed_mmps = msg.left_wheel_speed_mmps
        self._right_wheel_speed_mmps = msg.right_wheel_speed_mmps
        self._head_angle_rad = msg.head_angle_rad
        self._lift_height_mm = msg.lift_height_mm
        self._accel = util.Vector3(msg.accel.x, msg.accel.y, msg.accel.z)
        self._gyro = util.Vector3(msg.gyro.x, msg.gyro.y, msg.gyro.z)
        self._carrying_object_id = msg.carrying_object_id
        self._head_tracking_object_id = msg.head_tracking_object_id
        self._localized_to_object_id = msg.localized_to_object_id
        self._last_image_time_stamp = msg.last_image_time_stamp
        self._status.set(msg.status)

    def connect(self, timeout: int = 10) -> None:
        """Start the connection to Vector.

        .. testcode::

            import anki_vector

            robot = anki_vector.Robot()
            robot.connect()
            robot.anim.play_animation_trigger("GreetAfterLongTime")
            robot.disconnect()

        :param timeout: The time to allow for a connection before a
            :class:`anki_vector.exceptions.VectorTimeoutException` is raised.
        """
        self.conn.connect(timeout=timeout)
        self.events.start(self.conn)

        # Initialize components
        self._anim = animation.AnimationComponent(self)
        self._audio = audio.AudioComponent(self)
        self._behavior = behavior.BehaviorComponent(self)
        self._faces = faces.FaceComponent(self)
        self._motors = motors.MotorComponent(self)
        self._nav_map = nav_map.NavMapComponent(self)
        self._screen = screen.ScreenComponent(self)
        self._photos = photos.PhotographComponent(self)
        self._proximity = proximity.ProximityComponent(self)
        self._touch = touch.TouchComponent(self)
        self._viewer = viewer.ViewerComponent(self)
        self._viewer_3d = viewer.Viewer3DComponent(self)
        self._vision = vision.VisionComponent(self)
        self._world = world.World(self)
        self._camera = camera.CameraComponent(self)

        if self.cache_animation_lists:
            # Load animation triggers and animations so they are ready to play when requested
            anim_request = self._anim.load_animation_list()
            if isinstance(anim_request, concurrent.futures.Future):
                anim_request.result()
            anim_trigger_request = self._anim.load_animation_trigger_list()
            if isinstance(anim_trigger_request, concurrent.futures.Future):
                anim_trigger_request.result()

        # TODO enable audio feed when ready

        # Start rendering camera feed
        if self._show_viewer:
            self.camera.init_camera_feed()
            self.viewer.show()

        if self._show_3d_viewer:
            self.viewer_3d.show()

        if self._enable_nav_map_feed:
            self.nav_map.init_nav_map_feed()

        # Enable face detection, to allow Vector to add faces to its world view
        if self.conn.requires_behavior_control:
            face_detection = self.vision.enable_face_detection(
                detect_faces=self.enable_face_detection,
                estimate_expression=self.estimate_facial_expression,
            )
            if isinstance(face_detection, concurrent.futures.Future):
                face_detection.result()
            object_detection = self.vision.enable_custom_object_detection(
                detect_custom_objects=self.enable_custom_object_detection
            )
            if isinstance(object_detection, concurrent.futures.Future):
                object_detection.result()

        # Subscribe to a callback that updates the robot's local properties
        self.events.subscribe(
            self._unpack_robot_state,
            events.Events.robot_state,
            _on_connection_thread=True,
        )

        # get the camera configuration from the robot
        response = self._camera.get_camera_config()
        if isinstance(response, concurrent.futures.Future):
            response = response.result()
        self._camera.set_config(response)

        # Subscribe to a callback for camera exposure settings
        self.events.subscribe(
            self._camera.update_state,
            events.Events.camera_settings_update,
            _on_connection_thread=True,
        )

        # access the pose to prove it has gotten back from the event stream once
        try:
            if not self.pose:
                pass
        except VectorPropertyValueNotReadyException as e:
            raise VectorUnreliableEventStreamException() from e

    def disconnect(self) -> None:
        """Close the connection with Vector.

        .. testcode::

            import anki_vector
            robot = anki_vector.Robot()
            robot.connect()
            robot.anim.play_animation_trigger("GreetAfterLongTime")
            robot.disconnect()
        """
        if self.conn.requires_behavior_control:
            self.vision.close()

        # Stop rendering video
        self.viewer.close()

        # Stop rendering 3d video
        self.viewer_3d.close()

        # Shutdown camera feed
        self.camera.close_camera_feed()

        # TODO shutdown audio feed when available

        # Shutdown nav map feed
        self.nav_map.close_nav_map_feed()

        # Close the world and cleanup its objects
        self.world.close()

        self.proximity.close()
        self.touch.close()

        self.events.close()
        self.conn.close()

    def __enter__(self):
        self.connect(self.behavior_activation_timeout)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    @on_connection_thread(requires_control=False)
    async def get_battery_state(self) -> protocol.BatteryStateResponse:
        """Check the current state of the robot and cube batteries.

        The robot is considered fully-charged above 4.1 volts. At 3.6V, the robot is approaching low charge.

        Robot battery level values are as follows:

        +-------+---------+---------------------------------------------------------------+
        | Value | Level   | Description                                                   |
        +=======+=========+===============================================================+
        | 1     | Low     | 3.6V or less. If on charger, 4V or less.                      |
        +-------+---------+---------------------------------------------------------------+
        | 2     | Nominal | Normal operating levels.                                      |
        +-------+---------+---------------------------------------------------------------+
        | 3     | Full    | This state can only be achieved when Vector is on the charger |
        +-------+---------+---------------------------------------------------------------+

        Cube battery level values are shown below:

        +-------+---------+---------------------------------------------------------------+
        | Value | Level   | Description                                                   |
        +=======+=========+===============================================================+
        | 1     | Low     | 1.1V or less.                                                 |
        +-------+---------+---------------------------------------------------------------+
        | 2     | Normal  | Normal operating levels.                                      |
        +-------+---------+---------------------------------------------------------------+

        .. testcode::

            import anki_vector

            with anki_vector.Robot() as robot:
                print("Connecting to a cube...")
                robot.world.connect_cube()

                battery_state = robot.get_battery_state()
                if battery_state:
                    print("Robot battery voltage: {0}".format(battery_state.battery_volts))
                    print("Robot battery Level: {0}".format(battery_state.battery_level))
                    print("Robot battery is charging: {0}".format(battery_state.is_charging))
                    print("Robot is on charger platform: {0}".format(battery_state.is_on_charger_platform))
                    print("Robot suggested charger time: {0}".format(battery_state.suggested_charger_sec))
                    print("Cube battery level: {0}".format(battery_state.cube_battery.level))
                    print("Cube battery voltage: {0}".format(battery_state.cube_battery.battery_volts))
                    print("Cube battery seconds since last reading: {0}".format(battery_state.cube_battery.time_since_last_reading_sec))
                    print("Cube battery factory id: {0}".format(battery_state.cube_battery.factory_id))
        """
        get_battery_state_request = protocol.BatteryStateRequest()
        return await self.conn.grpc_interface.BatteryState(get_battery_state_request)

    @on_connection_thread(requires_control=False)
    async def get_version_state(self) -> protocol.VersionStateResponse:
        """Get the versioning information for Vector, including Vector's os_version and engine_build_id.

        .. testcode::

            import anki_vector
            with anki_vector.Robot() as robot:
                version_state = robot.get_version_state()
                if version_state:
                    print("Robot os_version: {0}".format(version_state.os_version))
                    print("Robot engine_build_id: {0}".format(version_state.engine_build_id))
        """
        get_version_state_request = protocol.VersionStateRequest()
        return await self.conn.grpc_interface.VersionState(get_version_state_request)


class AsyncRobot(Robot):
    """The AsyncRobot object is just like the Robot object, but allows multiple commands
    to be executed at the same time. To achieve this, all grpc function calls also
    return a :class:`concurrent.futures.Future`.

    1. Using :code:`with`: it works just like opening a file, and will close when
    the :code:`with` block's indentation ends.

    .. testcode::

        import anki_vector
        from anki_vector.util import degrees

        # Create the robot connection
        with anki_vector.AsyncRobot() as robot:
            # Start saying text asynchronously
            say_future = robot.behavior.say_text("Now is the time")
            # Turn robot, wait for completion
            turn_future = robot.behavior.turn_in_place(degrees(3*360))
            turn_future.result()
            # Play greet animation trigger, wait for completion
            greet_future = robot.anim.play_animation_trigger("GreetAfterLongTime")
            greet_future.result()
            # Make sure text has been spoken
            say_future.result()

    2. Using :func:`connect` and :func:`disconnect` to explicitly open and close the connection:
    it allows the robot's connection to continue in the context in which it started.

    .. testcode::

        import anki_vector
        from anki_vector.util import degrees

        # Create a Robot object
        robot = anki_vector.AsyncRobot()
        # Connect to Vector
        robot.connect()
        # Start saying text asynchronously
        say_future = robot.behavior.say_text("Now is the time")
        # Turn robot, wait for completion
        turn_future = robot.behavior.turn_in_place(degrees(3 * 360))
        turn_future.result()
        # Play greet animation trigger, wait for completion
        greet_future = robot.anim.play_animation_trigger("GreetAfterLongTime")
        greet_future.result()
        # Make sure text has been spoken
        say_future.result()
        # Disconnect from Vector
        robot.disconnect()

    When getting callbacks from the event stream, it's important to understand that function calls
    return a :class:`concurrent.futures.Future` and not an :class:`asyncio.Future`. This means any
    async callback functions will need to use :func:`asyncio.wrap_future` to be able to await the
    function's response.

    .. testcode::

        import asyncio
        import time

        import anki_vector

        async def callback(robot, event_type, event):
            await asyncio.wrap_future(robot.anim.play_animation_trigger('GreetAfterLongTime'))
            await asyncio.wrap_future(robot.behavior.set_head_angle(anki_vector.util.degrees(40)))

        if __name__ == "__main__":
            args = anki_vector.util.parse_command_args()
            with anki_vector.AsyncRobot(serial=args.serial, enable_face_detection=True) as robot:
                robot.behavior.set_head_angle(anki_vector.util.degrees(40))
                robot.events.subscribe(callback, anki_vector.events.Events.robot_observed_face)

                # Waits 10 seconds. Show Vector your face.
                time.sleep(10)

    :param serial: Vector's serial number. The robot's serial number (ex. 00e20100) is located on the underside of Vector,
                   or accessible from Vector's debug screen. Used to identify which Vector configuration to load.
    :param ip: Vector's IP Address. (optional)
    :param config: A custom :class:`dict` to override values in Vector's configuration. (optional)
                   Example: :code:`{"cert": "/path/to/file.cert", "name": "Vector-XXXX", "guid": "<secret_key>"}`
                   where :code:`cert` is the certificate to identify Vector, :code:`name` is the name on Vector's face
                   when his backpack is double-clicked on the charger, and :code:`guid` is the authorization token
                   that identifies the SDK user. Note: Never share your authentication credentials with anyone.
    :param default_logging: Toggle default logging.
    :param behavior_activation_timeout: The time to wait for control of the robot before failing.
    :param cache_animation_lists: Get the list of animation triggers and animations available at startup.
    :param enable_face_detection: Turn on face detection.
    :param estimate_facial_expression: Turn estimating facial expression on/off.
    :param enable_audio_feed: Turn audio feed on/off.
    :param enable_custom_object_detection: Turn custom object detection on/off.
    :param enable_nav_map_feed: Turn navigation map feed on/off.
    :param show_viewer: Specifies whether to display a view of Vector's camera in a window.
    :param show_3d_viewer: Specifies whether to display a 3D view of Vector's understanding of the world in a window.
    :param behavior_control_level: Request control of Vector's behavior system at a specific level of control.  Pass
                                   :code:`None` if behavior control is not needed.
                                   See :class:`ControlPriorityLevel` for more information."""

    @functools.wraps(Robot.__init__)
    def __init__(self, *args, **kwargs):
        super(AsyncRobot, self).__init__(*args, **kwargs)
        self._force_async = True
