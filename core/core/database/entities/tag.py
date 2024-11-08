from sqlalchemy.orm import Mapped, mapped_column

from core.database.entities.base import Entity


class Tag(Entity):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(unique=True)
