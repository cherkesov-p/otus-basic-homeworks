"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from typing import List, Iterable
from sqlalchemy.ext.asyncio import AsyncSession

from models import Base, Session, User, Post, async_engine
from jsonplaceholder_requests import get_posts, get_users


async def fetch_users_data() -> Iterable[User]:
    json_data: list = await get_users()
    users = []
    for data in json_data:
        user = User(
            id=data["id"],
            name=data["name"],
            username=data["username"],
            email=data["email"],
        )
        users.append(user)

    return users


async def fetch_posts_data() -> Iterable[Post]:
    json_data: list = await get_posts()
    posts = []
    for data in json_data:
        post = Post(
            id=data["id"],
            user_id=data["userId"],
            title=data["title"],
            body=data["body"],
        )
        posts.append(post)

    return posts


async def write_data_to_db(session: AsyncSession, data: Iterable):
    session.add_all(data)
    await session.commit()


async def init_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def async_main():
    await init_tables()

    users_data: List[User]
    posts_data: List[Post]
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    async with Session() as session:
        await write_data_to_db(session, users_data)
        await write_data_to_db(session, posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
