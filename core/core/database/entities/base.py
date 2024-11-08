from sqlalchemy.orm import DeclarativeBase


class Entity(DeclarativeBase):
    __abstract__ = True
