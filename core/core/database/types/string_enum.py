from enum import StrEnum

from sqlalchemy import Dialect, String, TypeDecorator


class StringEnum[T: StrEnum](TypeDecorator):
    impl = String

    def __init__(
        self,
        enum: type[T],
        length: int | None = None,
        collation: str | None = None,
    ):
        self.enum = enum
        super().__init__(length=length, collation=collation)

    def process_bind_param(self, value: T, dialect: Dialect) -> str:
        return value.value

    def process_result_value(self, value: str, dialect: Dialect):
        return self.enum(value)
