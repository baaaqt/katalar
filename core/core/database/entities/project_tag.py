from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from core.database.entities.base import Entity


class ProjectTag(Entity):
    __tablename__ = "projects_tags"
    project_id: Mapped[str] = mapped_column(ForeignKey("projects.id"), primary_key=True)
    tag_name: Mapped[str] = mapped_column(ForeignKey("tags.name"), primary_key=True)

    __table_args__ = (
        UniqueConstraint(
            "project_id", "tag_name", name="project_tag_unique_constraint"
        ),
    )
