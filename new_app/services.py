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
    cameras = repo.cameraslist()
    if not is_valid_id(camera_id.id, cameras):
        raise InvalidSku(f"Invalid id {camera_id.id}")
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
    frames = repo.framesslist()
    if not is_valid_id(frame_id.id, frames):
        raise InvalidSku(f"Invalid id {frames.id}")
    repo.addFrame(model.Detect(left=left,right=right,top=top,bottom=bottom,label=label,conf=conf,frame_id=frame_id))
    session.commit()