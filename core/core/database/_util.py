from core.database.entities.base import Entity
from core.database.entities.project import Project
from core.database.entities.project_tag import ProjectTag
from core.database.entities.tag import Tag
from core.database.entities.tagtoken import TagToken
from core.database.entities.user import User


def get_database_entites() -> list[type[Entity]]:
    return [
        User,
        Project,
        Tag,
        TagToken,
        ProjectTag,
    ]
