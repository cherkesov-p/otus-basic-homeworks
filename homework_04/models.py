"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    MetaData,
)
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://test:test123@localhost/test"

async_engine = create_async_engine(url=PG_CONN_URI, echo=False)
Session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
metadata = MetaData()


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True, autoincrement=True)


Base = declarative_base(cls=Base)


class User(Base):
    name = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True)

    posts = relationship("Post", back_populates="user", uselist=True)

    def __str__(self) -> str:
        return f"User(id={self.id}, username={self.username}, email={self.email})"


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"), unique=False, nullable=False)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False, default="", server_default="")

    user = relationship("User", back_populates="posts", uselist=False)

    def __str__(self) -> str:
        return f"Post(id={self.id}, user_id={self.user_id}, title={self.title})"
