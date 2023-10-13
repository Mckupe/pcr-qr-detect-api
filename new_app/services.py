from __future__ import annotations
from typing import Optional
from datetime import date

import model
from repository import AbstractRepository

class InvalidSku(Exception):
    pass

def is_valid_id(id, list):
    return id in {b.id for b in list}

def add_camera(
    name: Optional[str],
    repo: AbstractRepository, session,
) -> None:
    repo.addCamera(model.Camera(name))
    session.commit()

def add_tracking_object(
    label: Optional[str],
    repo: AbstractRepository, session,
) -> None:
    repo.addTrackingObject(model.TrackingObject(label))
    session.commit()

def add_frame(
    path_frame: Optional[str],camera_id:int,
    repo: AbstractRepository, session,
) -> None:
    cameras = repo.cameras_list()
    if not is_valid_id(camera_id, cameras):
        raise InvalidSku(f"Invalid id {camera_id}")
    repo.addFrame(model.Frame(path_frame=path_frame,camera_id=camera_id))
    session.commit()

def add_detect(
    left: float,
    right: float,
    top: float,
    bottom: float,
    label: Optional[str],
    conf: Optional[str],
    frame_id: int,
    repo: AbstractRepository, session,
) -> None:
    frames = repo.framess_list()
    if not is_valid_id(frame_id, frames):
        raise InvalidSku(f"Invalid id {frame_id}")
    repo.addDetect(model.Detect(left=left,right=right,top=top,bottom=bottom,label=label,conf=conf,frame_id=frame_id))
    session.commit()

def add_start_cube_control(
    config: Optional[str],
    repo: AbstractRepository, session,
) -> None:
    repo.addStartCubeControl(model.StartCubeControl(config=config))
    session.commit()

def add_start_qr_read(
    config: Optional[str],
    repo: AbstractRepository, session,
) -> None:
    repo.addStartQrRead(model.StartQrRead(config=config))
    session.commit()

def add_controller_owen(
    start_qr_read_id:int,
    repo: AbstractRepository, session,
) -> None:
    start_qr_reads = repo.start_qr_reads_list()
    if not is_valid_id(start_qr_read_id, start_qr_reads):
        raise InvalidSku(f"Invalid id {start_qr_read_id}")
    repo.addControllerOwen(model.ControllerOwen(start_qr_read_id=start_qr_read_id))
    session.commit()

def add_cube_wrapping(
    start_cube_control_id:int,
    repo: AbstractRepository, session,
) -> None:
    start_cube_controls = repo.start_cube_controls_list()
    if not is_valid_id(start_cube_control_id, start_cube_controls):
        raise InvalidSku(f"Invalid id {start_cube_control_id}")
    repo.addCubeWrapping(model.CubeWrapping(start_cube_control_id=start_cube_control_id))
    session.commit()

def add_readed_qr(
    QR:str,
    frame_id:int,
    camera_id:int,
    repo: AbstractRepository, session,
) -> None:
    frames = repo.frames_list()
    cameras = repo.cameras_list()
    if not is_valid_id(frame_id, frames):
        raise InvalidSku(f"Invalid id {frame_id}")
    if not is_valid_id(camera_id, cameras):
        raise InvalidSku(f"Invalid id {camera_id}")
    repo.addReadedQr(model.ReadedQr(QR=QR,frame_id=frame_id,camera_id=camera_id))
    session.commit()

def add_not_readed_qr(
    frame_id:int,
    repo: AbstractRepository, session,
) -> None:
    frames = repo.frames_list()
    if not is_valid_id(frame_id, frames):
        raise InvalidSku(f"Invalid id {frame_id}")
    repo.addNotReadedQr(model.NotReadedQr(frame_id=frame_id))
    session.commit()

def add_track(
    detect_id:int,
    tracking_object_id:int,
    repo: AbstractRepository, session,
) -> None:
    detects = repo.detects_list()
    tracking_objects = repo.tracking_objects_list()
    if not is_valid_id(detect_id, detects):
        raise InvalidSku(f"Invalid id {detect_id}")
    if not is_valid_id(tracking_object_id, tracking_objects):
        raise InvalidSku(f"Invalid id {tracking_object_id}")
    repo.addTrack(model.Track(detect_id=detect_id,tracking_object_id=tracking_object_id))
    session.commit()

def add_qr_read_camera(
    camera_id:int,
    start_qr_read_id:int,
    repo: AbstractRepository, session,
) -> None:
    cameras = repo.cameras_list()
    start_qr_reads = repo.start_qr_reads_list()
    if not is_valid_id(camera_id, cameras):
        raise InvalidSku(f"Invalid id {camera_id}")
    if not is_valid_id(start_qr_read_id, start_qr_reads):
        raise InvalidSku(f"Invalid id {start_qr_read_id}")
    repo.addQrReadCamera(model.QrReadCamera(camera_id=camera_id,start_qr_read_id=start_qr_read_id))
    session.commit()

def add_cube_control_camera(
    camera_id:int,
    start_cube_control_id:int,
    repo: AbstractRepository, session,
) -> None:
    cameras = repo.cameras_list()
    start_cube_controls = repo.start_cube_controls_list()
    if not is_valid_id(camera_id, cameras):
        raise InvalidSku(f"Invalid id {camera_id}")
    if not is_valid_id(start_cube_control_id, start_cube_controls):
        raise InvalidSku(f"Invalid id {start_cube_control_id}")
    repo.addCubeControlCamera(model.CubeControlCamera(camera_id=camera_id,start_cube_control_id=start_cube_control_id))
    session.commit()