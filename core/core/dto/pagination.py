from typing import Sequence

from pydantic import BaseModel, ConfigDict, NonNegativeInt, PositiveInt, computed_field


class Page[T](BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    items: Sequence[T]
    page: PositiveInt
    page_size: PositiveInt
    total_items: NonNegativeInt

    @computed_field  # type: ignore[prop-decorator]
    @property
    def total_pages(self) -> int:
        return self.total_items // self.page_size + int(
            self.total_items % self.page_size > 0
        )


class Pageable(BaseModel):
    page: PositiveInt
    page_size: PositiveInt

    @computed_field  # type: ignore[prop-decorator]
    @property
    def skip(self) -> int:
        return (self.page - 1) * self.page_size
