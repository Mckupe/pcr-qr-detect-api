from dataclasses import dataclass
import uuid
from datetime import datetime
from typing import Annotated, Optional

from sqlalchemy import DateTime, func
from sqlalchemy.dialects.postgresql import UUID as PgUUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

@dataclass(frozen=True)
class Camera:
    def __init__(self, name: str):
        self.name = name

class TrackingObject:
    def __init__(self, label: str):
        self.label = label

class Frame:
    def __init__(self, path_frame: str, camera_id: Camera):
        self.path_frame = path_frame
        self.camera_id = camera_id.id

class Detect:
    def __init__(self, left: float, right: float, top: float, bottom: float, label: str, conf: str, frame_id: Frame):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.label = label
        self.conf = conf
        self.frame_id = frame_id.id

class StartCubeControl:
    def __init__(self, config: str):
        self.config = config

class StartQrRead:
    def __init__(self, config: str):
        self.config = config

class ControllerOwen:
    def __init__(self, start_qr_read: StartQrRead):
        self.start_qr_read_id = start_qr_read.id

class CubeWrapping:
    def __init__(self, start_cube_control: StartCubeControl):
        self.start_cube_control = start_cube_control.id

class ReadedQr:
    def __init__(self, QR: str, frame_id: Frame, camera_id: Camera):
        self.qr = QR
        self.frame_id = frame_id.id
        self.camera_id = camera_id.id

class NotReadedQr:
    def __init__(self, frame_id: Frame):
        self.frame_id = frame_id.id

class Track:
    def __init__(self, detect_id: Detect, tracking_object_id: TrackingObject):
        self.detect_id = detect_id.id
        self.tracking_object_id = tracking_object_id.id

class QrReadCamera:
    def __init__(self, camera_id: Camera, start_qr_read_id: StartQrRead):
        self.camera_id = camera_id.id
        self.start_qr_read_id = start_qr_read_id.id

class CubeControlCamera:
    def __init__(self, camera_id: Camera, start_cube_control_id: StartCubeControl):
        self.camera_id = camera_id.id
        self.start_cube_control_id = start_cube_control_id.id

    # def allocate(self, line: OrderLine):
    #     if self.can_allocate(line):
    #         self._allocations.add(line)

    # def deallocate(self, line: OrderLine):
    #     if line in self._allocations:
    #         self._allocations.remove(line)

    # @property
    # def allocated_quantity(self) -> int:
    #     return sum(line.qty for line in self._allocations)

    # @property
    # def available_quantity(self) -> int:
    #     return self._purchased_quantity - self.allocated_quantity

    # def can_allocate(self, line: OrderLine) -> bool:
    #     return self.sku == line.sku and self.available_quantity >= line.qty