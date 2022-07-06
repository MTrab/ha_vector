import asyncio
from os import environ
import time
import aiohttp

from ha_vector.home_assistant import API
from ha_vector.robot import AsyncRobot, Robot

import ha_vector

SETTINGS_DIR = "./.vector"


async def callback(robot, event_type, event):
    await asyncio.wrap_future(robot.anim.play_animation_trigger("GreetAfterLongTime"))
    await asyncio.wrap_future(
        robot.behavior.set_head_angle(anki_vector.util.degrees(40))
    )


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
    robot.conn.request_control()
    robot.behavior.say_text(
        text="Hello there!",
        use_vector_voice=True,
    )
    robot.conn.release_control(timeout=1.0)

asyncio.run(main())
