from typing import Any, Self

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession


class UnitOfWork:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    @property
    def session(self) -> AsyncSession:
        return self._session

    async def start_transaction(self) -> None:
        await self._session.begin()

    async def commit(self) -> None:
        try:
            await self._session.commit()
        except SQLAlchemyError:
            await self.rollback()
            raise

    async def rollback(self) -> None:
        await self._session.rollback()
        await self.start_transaction()

    async def __aenter__(self) -> Self:
        if not self._session.in_transaction():
            await self.start_transaction()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: Any,
    ) -> None:
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()

    async def close(self) -> None:
        await self._session.aclose()

    def in_transaction(self) -> bool:
        return self._session.in_transaction()
