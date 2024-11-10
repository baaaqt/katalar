from typing import Any, Sequence

from sqlalchemy import ColumnElement, UnaryExpression

from core.database.entities.base import Entity
from core.database.patterns.repositories.base import AsyncBaseRepository
from core.dto.pagination import Page, Pageable


class PaginationRepository[T: Entity](AsyncBaseRepository[T]):
    async def find_paginated(
        self,
        pageable: Pageable,
        criteria: Sequence[ColumnElement[Any]] = (),
        order_by: Sequence[UnaryExpression[Any]] = (),
    ) -> Page[T]:
        items = await self.find(
            criteria=criteria,
            order_by=order_by,
            skip=pageable.skip,
            limit=pageable.page_size,
        )
        total_items = await self.count(criteria=criteria)
        return Page(
            items=items,
            page=pageable.page,
            page_size=pageable.page_size,
            total_items=total_items,
        )
