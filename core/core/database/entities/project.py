from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.core.database.entities.tag import Tag
from core.database.entities.base import Entity
from core.database.entities.mixins.id import IDAsUUIDStringMixin


class Project(IDAsUUIDStringMixin, Entity):
    __tablename__ = "projects"

    name: Mapped[str] = mapped_column(String(length=255), unique=True)
    description: Mapped[str] = mapped_column(Text())
    is_active: Mapped[bool] = mapped_column(default=True, index=True)
    tags: Mapped[list[Tag]] = relationship(
        "Tag",
        secondary="projects_tags",
        lazy="joined",
    )

    @property
    def tag_names(self) -> list[str]:
        return [tag.name for tag in self.tags]
