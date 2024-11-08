from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.database.entities.base import Entity


class User(Entity):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] = mapped_column()

    name: Mapped[str] = mapped_column(String(length=500))
