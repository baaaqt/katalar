from enum import StrEnum
from typing import Any

from sqlalchemy import Dialect, String, TypeDecorator


class StringEnum[T: StrEnum](TypeDecorator[Any]):
    impl = String

    def __init__(
        self,
        enum: type[T],
        length: int | None = None,
        collation: str | None = None,
    ):
        self.enum = enum
        super().__init__(length=length, collation=collation)

    def process_bind_param(self, value: T | None, dialect: Dialect) -> str:
        if value is None:
            raise TypeError(f"Value is not an instance of the {self.enum!r}")
        return value.value

    def process_result_value(self, value: str | Any, dialect: Dialect) -> T:
        return self.enum(value)
