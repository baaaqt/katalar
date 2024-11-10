from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from core.database.entities.base import Entity
from core.database.entities.mixins.datetimesmixin import CreatedAtMixin
from core.database.entities.mixins.id import IDAsUUIDStringMixin


class Record(Entity, CreatedAtMixin, IDAsUUIDStringMixin):
    __tablename__ = "records"

    code: Mapped[str] = mapped_column(index=True)
    name: Mapped[str] = mapped_column(index=True)
    text: Mapped[str] = mapped_column(Text())
    project_id: Mapped[str] = mapped_column(ForeignKey("projects.id"), primary_key=True)
