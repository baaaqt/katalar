from core.database.patterns.repositories.id_repository import IDEntityRepository
from core.database.patterns.repositories.pagination import PaginationRepository


class UserRepositoryBase(IDEntityRepository, PaginationRepository): ...


class ProjectRepositoryBase(IDEntityRepository, PaginationRepository): ...


class RecordRepositoryBase(IDEntityRepository, PaginationRepository): ...


class TagRepositoryBase(PaginationRepository): ...


class TagTokenRepositoryBase(IDEntityRepository, PaginationRepository): ...
