from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.database.entities.base import Entity
from core.database.entities.mixins.datetimesmixin import CreatedAtUpdatedAtMixin


class User(Entity, CreatedAtUpdatedAtMixin):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(length=30), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(length=255), unique=True, index=True)
    password: Mapped[str] = mapped_column()

    name: Mapped[str] = mapped_column(String(length=500))

    last_login: Mapped[datetime] = mapped_column(default=datetime.now)
