import asyncio
from os import environ
import aiohttp

from ha_vector.home_assistant import API
from ha_vector.robot import Robot

SETTINGS_DIR = "./.vector"


async def main():
    async with aiohttp.ClientSession() as session:
        vector_api = API(
            environ["EMAIL"],
            environ["PASSWORD"],
            environ["NAME"],
            environ["SERIAL"],
            environ["IP"],
            SETTINGS_DIR,
            session,
        )

        await vector_api.async_configure()

    config = {
        "cert": vector_api.certificate,
        "name": environ["NAME"],
        "guid": vector_api.guid,
    }

    robot = Robot(
        environ["SERIAL"],
        behavior_control_level=None,
        default_logging=False,
        cache_animation_lists=False,
        enable_face_detection=True,
        estimate_facial_expression=True,
        enable_audio_feed=True,
        ip=environ["IP"],
        config=config,
    )


asyncio.run(main())
