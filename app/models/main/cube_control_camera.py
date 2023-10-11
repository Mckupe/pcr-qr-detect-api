from sqlalchemy.orm import DeclarativeBase, Mapped

class OrmQrReadCamera(DeclarativeBase):
    """Модель алхимии для """

    __tablename__ = "cube_wrapping"

    camera_id: Mapped[str | None]

    start_cube_control_id: Mapped[str | None]