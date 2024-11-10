from core.database.entities.project import Project
from core.database.entities.record import Record
from core.database.entities.tag import Tag
from core.database.entities.tagtoken import TagToken
from core.database.entities.user import User
from core.database.entities.user_tag import UserTag
from core.database.patterns.repositories.id_repository import IDEntityRepository
from core.database.patterns.repositories.pagination import PaginationRepository


class UserRepositoryBase(IDEntityRepository[User, str], PaginationRepository[User]):
    entity = User


class ProjectRepositoryBase(
    IDEntityRepository[Project, str],
    PaginationRepository[Project],
):
    entity = Project


class RecordRepositoryBase(
    IDEntityRepository[Record, str], PaginationRepository[Record]
):
    entity = Record


class TagRepositoryBase(PaginationRepository[Tag]):
    entity = Tag


class TagTokenRepositoryBase(
    IDEntityRepository[TagToken, str],
    PaginationRepository[TagToken],
):
    entity = TagToken


class UserTagRepositoryBase(PaginationRepository[UserTag]):
    entity = UserTag
