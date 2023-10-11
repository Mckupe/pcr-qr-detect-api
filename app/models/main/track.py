from sqlalchemy.orm import Mapped

from .base import Base


class OrmStartQrRead(Base):
    """Модель алхимии для """

    __tablename__ = "start_qr_read"

    detect_id: Mapped[str | None]
    
    tracking_object_id: Mapped[str | None]