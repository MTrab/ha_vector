import asyncio
from os import environ
import aiohttp
import threading

import ha_vector
from ha_vector.setup import VectorSetup
from ha_vector.robot import AsyncRobot
from ha_vector.events import Events
from ha_vector.util import degrees

SETTINGS_DIR = "./.vector"

said_text = False


async def main():
    async with aiohttp.ClientSession() as session:
        vector_api = VectorSetup(
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
        "guid": vector_api.guid.replace("b'", "").replace("'", ""),
    }

    robot = AsyncRobot(
        # with Robot(
        environ["SERIAL"],
        ip_address=environ["IP"],
        name=environ["NAME"],
        config=config,
        default_logging=False,
        behavior_control_level=None,
        cache_animation_lists=False,
        enable_face_detection=True,
        estimate_facial_expression=True,
        enable_audio_feed=True,
        enable_nav_map_feed=True,
    )
    # robot.conn.request_control()
    # robot.behavior.say_text(
    #     text="Hello there!",
    #     use_vector_voice=True,
    # )
    # robot.conn.release_control(timeout=1.0)
    robot.connect()

    # robot.camera.init_camera_feed()
    await asyncio.wrap_future(robot.conn.request_control())
    image = await asyncio.wrap_future(robot.camera.capture_single_image())
    image.raw_image.show()
    image.raw_image.save("latist.jpg")
    robot.disconnect()


asyncio.run(main())
