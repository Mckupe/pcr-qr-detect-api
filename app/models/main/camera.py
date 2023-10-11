from sqlalchemy.orm import Mapped

from .base import Base


class OrmCamera(Base):
    """Модель алхимии для """

    __tablename__ = "camera"

    name: Mapped[str | None]

    batches: Mapped[list["OrmBatch"]] = relationship(
        "OrmBatch", cascade="all, delete", back_populates="batch_param"
    )

    batches: Mapped[list["OrmBatch"]] = relationship(
        "OrmBatch", cascade="all, delete", back_populates="batch_param"
    )

    batches: Mapped[list["OrmBatch"]] = relationship(
        "OrmBatch", cascade="all, delete", back_populates="batch_param"
    )

    batches: Mapped[list["OrmBatch"]] = relationship(
        "OrmBatch", cascade="all, delete", back_populates="batch_param"
    )