from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from . import OrmStartCubeControl  # noqa


class OrmCubeWrapping(Base):
    """Модель алхимии для """

    __tablename__ = "cube_wrapping"

    start_cube_control: Mapped["OrmStartCubeControl"] = relationship("OrmStartCubeControl", back_populates="cube_wrapping")
