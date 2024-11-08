from sqlalchemy import Uuid
from sqlalchemy.orm import Mapped, mapped_column


class IDAsUUIDStringMixin:
    id: Mapped[str] = mapped_column(
        Uuid(as_uuid=True, native_uuid=True),
        primary_key=True,
    )
