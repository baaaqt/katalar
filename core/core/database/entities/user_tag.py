from enum import StrEnum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.database.entities.base import Entity
from core.database.entities.mixins.datetimesmixin import CreatedAtMixin
from core.database.types.string_enum import StringEnum


class UserTagRole(StrEnum):
    OWNER = "owner"
    MEMBER = "member"


class UserTag(Entity, CreatedAtMixin):
    __tablename__ = "users_tags"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), primary_key=True)
    tag_name: Mapped[str] = mapped_column(ForeignKey("tags.name"), primary_key=True)
    role: Mapped[UserTagRole] = mapped_column(
        StringEnum(UserTagRole),
        default=UserTagRole.MEMBER,
    )
