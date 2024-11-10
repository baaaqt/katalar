from typing import Any, Mapping, Sequence

from sqlalchemy import (
    ColumnElement,
    UnaryExpression,
    delete,
    func,
    insert,
    select,
    update,
)
from sqlalchemy import sql as sa_sql
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.entities.base import Entity


class AsyncBaseRepository[T: Entity]:
    entity: type[T]

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def find(
        self,
        criteria: Sequence[ColumnElement[Any]] = (),
        order_by: Sequence[UnaryExpression[Any]] = (),
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[T]:
        q = (
            select(self.entity)
            .where(*criteria)
            .order_by(*order_by)
            .offset(skip)
            .limit(limit)
        )
        result = await self._session.execute(q)
        return result.scalars().unique().all()

    async def create(self, data: Mapping[str, Any]) -> T:
        q = insert(self.entity).values(data).returning(self.entity)
        result = await self._session.execute(q)
        return result.scalars().unique().one()

    async def delete(self, criteria: Sequence[ColumnElement[Any]]) -> None:
        q = delete(self.entity).where(*criteria)
        await self._session.execute(q)

    async def update(
        self,
        criteria: Sequence[ColumnElement[Any]],
        updates: dict[str, Any],
    ) -> Sequence[T]:
        q = update(self.entity).where(*criteria).values(updates).returning(self.entity)
        result = await self._session.execute(q)
        return result.scalars().unique().all()

    async def refresh(
        self,
        entity: T,
        load_attributes: Sequence[str] | None = None,
    ) -> T:
        await self._session.refresh(entity, attribute_names=load_attributes)
        return entity

    async def count(self, criteria: Sequence[ColumnElement[Any]] = ()) -> int:
        q = select(func.count()).select_from(self.entity).where(*criteria)
        result = await self._session.execute(q)
        return result.scalar_one()

    async def exists(self, criteria: Sequence[ColumnElement[Any]]) -> bool:
        q = select(sa_sql.exists().where(*criteria))
        result = await self._session.execute(q)
        return result.scalar_one()
