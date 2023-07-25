"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_json(url: str) -> list:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: list = await response.json()
            if isinstance(data, list):
                return data
            else:
                return list()


async def get_posts() -> list:
    return await get_json(POSTS_DATA_URL)


async def get_users() -> list:
    return await get_json(USERS_DATA_URL)
