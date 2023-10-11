import uuid
from datetime import datetime
from typing import Annotated

from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import UUID as PgUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

uuid_pg = Annotated[
    uuid.UUID,
    mapped_column(PgUUID(as_uuid=True)),
]
uuid_pk = Annotated[
    uuid_pg,
    mapped_column(primary_key=True, default=uuid.uuid4),
]
datetime_created_at = Annotated[
    datetime,
    mapped_column(default=func.now(), index=True),
]
datetime_updated_at = Annotated[
    datetime_created_at,
    mapped_column(onupdate=func.now()),
]


class Base(DeclarativeBase):
    id: Mapped[uuid_pk]
    created_at: Mapped[datetime_created_at] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[datetime_updated_at] = mapped_column(DateTime(timezone=True))