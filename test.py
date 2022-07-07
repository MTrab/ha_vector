import asyncio
from os import environ
import aiohttp

import ha_vector
from ha_vector.home_assistant import API
from ha_vector.robot import AsyncRobot

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
        "guid": vector_api.guid.replace("b'", "").replace("'", ""),
    }


    robot = AsyncRobot(
        # with Robot(
        environ["SERIAL"],
        default_logging=False,
        behavior_control_level=None,
        cache_animation_lists=False,
        enable_face_detection=True,
        estimate_facial_expression=True,
        enable_audio_feed=True,
        ip=environ["IP"],
        config=config,
    )
    # robot.conn.request_control()
    # robot.behavior.say_text(
    #     text="Hello there!",
    #     use_vector_voice=True,
    # )
    # robot.conn.release_control(timeout=1.0)
    robot.connect()

    print("Getting battery states")
    print(robot.get_battery_state().result())

    robot.disconnect()


asyncio.run(main())
