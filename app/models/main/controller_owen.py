from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, uuid_pg

if TYPE_CHECKING:
    from . import OrmStartQrRead  # noqa


class OrmСontrollerOwen(Base):
    """Модель алхимии для """

    __tablename__ = "controller_owen"

    start_qr_read_id: Mapped["OrmStartQrRead"] = relationship("OrmStartQrRead", back_populates="controller_owen")
