"""Home Assistant specific calls."""
from __future__ import annotations

import configparser
import os
import logging
import platform
import socket
from pathlib import Path
import grpc
from cryptography import x509
from cryptography.hazmat.backends import default_backend

from ha_vector import messaging

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
        settings_dir: str,
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
        self._settings_dir = settings_dir

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
        await self._async_write_config()

    async def _async_get_cert(self) -> bytes:
        """Get Vector certificate."""
        res = await self._client.get(f"{TOKEN_URL}{self._serial}")
        if res.status != 200:
            raise Exception("Could not get Vector certificate")

        self._cert = await res.read()
        return self._cert

    async def _async_save_cert(self) -> str:
        """Write Vector's certificate to a file located in the user's home directory"""
        os.makedirs(str(self._settings_dir), exist_ok=True)
        self._cert_file = str(self._settings_dir / f"{self._name}-{self._serial}.cert")
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
        print(self._handler.url)
        print(self._handler.headers)
        print(payload)
        print(res.status)
        print(res)
        if res.status != 200:
            raise Exception("Error fetching session token.")

        self._token = await res.json(content_type="text/json")
        return self._token

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
            print(request)
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
        print(self._guid)
        return self._guid

    async def _async_write_config(self, clear: bool = True):
        """Write config to sdk_config.ini."""
        home = Path.home()
        config_file = str(home / "..anki_vector" / "sdk_config.ini")

        config = configparser.ConfigParser(strict=False)

        try:
            config.read(config_file)
        except configparser.ParsingError:
            if os.path.exists(config_file):
                os.rename(config_file, config_file + "-error")
        if clear:
            config[self._serial] = {}

        config[self._serial]["cert"] = self._cert_file
        config[self._serial]["ip"] = self._ip
        config[self._serial]["name"] = self._name
        config[self._serial]["guid"] = self._guid.decode("utf-8")
        temp_file = config_file + "-temp"
        if os.path.exists(config_file):
            os.rename(config_file, temp_file)
        try:
            with os.fdopen(
                os.open(config_file, os.O_WRONLY | os.O_CREAT, 0o600), "w"
            ) as conf_file:
                config.write(conf_file)
        except Exception as err:
            if os.path.exists(temp_file):
                os.rename(temp_file, config_file)
            raise err
        else:
            if os.path.exists(temp_file):
                os.remove(temp_file)
