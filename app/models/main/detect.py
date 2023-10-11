from sqlalchemy.orm import DeclarativeBase, Mapped

class OrmQrReadCamera(DeclarativeBase):
    """Модель алхимии для """

    __tablename__ = "qr_read_camera"

    left: Mapped[float | None]

    right: Mapped[float | None]

    top: Mapped[float | None]

    bottom: Mapped[float | None]

    label: Mapped[str | None]

    conf: Mapped[str | None]

    frame_id: 