from sqlalchemy.orm import Mapped

from .base import Base


class OrmStartCubeControl(Base):
    """Модель алхимии для """

    __tablename__ = "start_cube_control"

    config: Mapped[str | None]