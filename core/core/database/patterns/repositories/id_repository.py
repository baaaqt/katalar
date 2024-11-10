from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.entities.base import Entity
from core.database.patterns.repositories.base import AsyncBaseRepository


class IDEntityRepository[T: Entity, TID: Any](AsyncBaseRepository[T]):
    def __init__(self, session: AsyncSession) -> None:
        if not hasattr(self.entity, "id"):
            raise TypeError(f"Type {self.entity} does not have an id attribute")

        super().__init__(session)

    async def find_by_id(self, id: TID) -> T | None:
        result = await self.find([self.entity.id == id], limit=1)  # type: ignore[attr-defined]
        if len(result) == 0:
            return None
        return result[0]

    async def update_by_id(self, id: TID, updates: Any) -> T | None:
        result = await self.update([self.entity.id == id], updates)  # type: ignore[attr-defined]
        if len(result) == 0:
            return None
        return result[0]

    async def delete_by_id(self, id: TID) -> None:
        await self.delete([self.entity.id == id])  # type: ignore[attr-defined]

    async def exists_by_id(self, id: TID) -> bool:
        return await self.exists([self.entity.id == id])  # type: ignore[attr-defined]
