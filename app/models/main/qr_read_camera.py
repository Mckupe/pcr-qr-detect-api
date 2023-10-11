from sqlalchemy.orm import DeclarativeBase, Mapped

class OrmQrReadCamera(DeclarativeBase):
    """Модель алхимии для """

    __tablename__ = "qr_read_camera"

    camera_id: Mapped[str | None]

    start_qr_read_id: Mapped[str | None]