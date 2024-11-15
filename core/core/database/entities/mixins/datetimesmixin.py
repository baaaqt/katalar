from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(default=datetime.now, index=True)


class UpdatedAtMixin:
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now, onupdate=datetime.now, index=True
    )


class CreatedAtUpdatedAtMixin(CreatedAtMixin, UpdatedAtMixin): ...
