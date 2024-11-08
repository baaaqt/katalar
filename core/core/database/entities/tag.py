from sqlalchemy.orm import Mapped, mapped_column

from core.database.entities.base import Entity
from core.database.entities.mixins.datetimesmixin import CreatedAtMixin


class Tag(Entity, CreatedAtMixin):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(unique=True, primary_key=True)
