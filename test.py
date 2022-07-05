import asyncio
from os import environ
import aiohttp

from ha_vector.home_assistant import API

SETTINGS_DIR = "./.vector"


async def async_run():
    async with aiohttp.ClilentSession() as session:
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

asyncio.run(async_run)
