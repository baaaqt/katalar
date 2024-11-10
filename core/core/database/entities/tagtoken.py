from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.database.entities.base import Entity
from core.database.entities.mixins.id import IDAsUUIDStringMixin


class TagToken(Entity, IDAsUUIDStringMixin):
    tag_name: Mapped[str] = mapped_column(ForeignKey("tags.name"), primary_key=True)
    token: Mapped[str]
