import asyncio
from os import environ
import aiohttp

from ha_vector.home_assistant import API

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


asyncio.run(main())
