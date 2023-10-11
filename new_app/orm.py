from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime, ForeignKey, Float, func
from sqlalchemy.orm import mapper, relationship

import model


metadata = MetaData()

camera = Table(
    "camera",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("create_at", DateTime, nullable=False, server_default=func.now()),
    Column("update_at", DateTime, nullable=False, server_default=func.now()),
    Column("name", String(255)),
)

tracking_object = Table(
    "tracking_object",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("create_at", DateTime, nullable=False, server_default=func.now()),
    Column("update_at", DateTime, nullable=False, server_default=func.now()),
    Column("label", String(255)),
)

frame = Table(
    "frame",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("create_at", DateTime, nullable=False, server_default=func.now()),
    Column("update_at", DateTime, nullable=False, server_default=func.now()),
    Column("path_frame", String(255)),
    Column("camera_id", ForeignKey("camera.id")),
)

detect = Table(
    "detect",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("create_at", DateTime, nullable=False, server_default=func.now()),
    Column("update_at", DateTime, nullable=False, server_default=func.now()),
    Column("left", Float),
    Column("right", Float),
    Column("top", Float),
    Column("bottom", Float),
    Column("label", String(255)),
    Column("conf", String(255)),
    Column("frame_id", ForeignKey("frame.id")),
)

start_cube_control = Table(
    "start_cube_control",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("create_at", DateTime, nullable=False, server_default=func.now()),
    Column("update_at", DateTime, nullable=False, server_default=func.now()),
    Column("config", String(255)),
)

start_qr_read = Table(
    "start_qr_read",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("create_at", DateTime, nullable=False, server_default=func.now()),
    Column("update_at", DateTime, nullable=False, server_default=func.now()),
    Column("config", String(255)),
)

controller_owen = Table(
    "controller_owen",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("create_at", DateTime, nullable=False, server_default=func.now()),
    Column("update_at", DateTime, nullable=False, server_default=func.now()),
    Column("start_qr_read_id", ForeignKey("start_qr_read.id")),
)

cube_wrapping = Table(
    "cube_wrapping",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("create_at", DateTime, nullable=False, server_default=func.now()),
    Column("update_at", DateTime, nullable=False, server_default=func.now()),
    Column("start_cube_control", ForeignKey("start_cube_control.id")),
)

readed_qr = Table(
    "readed_qr",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("create_at", DateTime, nullable=False, server_default=func.now()),
    Column("update_at", DateTime, nullable=False, server_default=func.now()),
    Column("QR", String(255)),
    Column("frame_id", ForeignKey("frame.id")),
    Column("camera_id", ForeignKey("camera.id")),
)

not_readed_qr = Table(
    "not_readed_qr",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("create_at", DateTime, nullable=False, server_default=func.now()),
    Column("update_at", DateTime, nullable=False, server_default=func.now()),
    Column("frame_id", ForeignKey("frame.id")),
)

track = Table(
    "track",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("create_at", DateTime, nullable=False, server_default=func.now()),
    Column("update_at", DateTime, nullable=False, server_default=func.now()),
    Column("detect_id", ForeignKey("detect.id")),
    Column("tracking_object_id", ForeignKey("tracking_object.id")),
)

qr_read_camera = Table(
    "qr_read_camera",
    metadata,
    Column("camera_id", ForeignKey("camera.id")),
    Column("start_qr_read_id", ForeignKey("start_qr_read.id")),
)

cube_control_camera = Table(
    "cube_control_camera",
    metadata,
    Column("camera_id", ForeignKey("camera.id")),
    Column("start_qr_read_id", ForeignKey("start_qr_read.id")),
)

def start_mappers():
    mapper(model.Camera, camera)
    mapper(model.TrackingObject, tracking_object)
    mapper(model.Frame, frame, properties={'Camera': relationship(model.Camera, primaryjoin=camera.c.id==frame.c.camera_id)},) 
    mapper(model.Detect, detect, properties={'Frame': relationship(model.Frame, primaryjoin=frame.c.id==detect.c.frame_id)},)
    mapper(model.StartCubeControl, start_cube_control)
    mapper(model.StartQrRead, start_qr_read)
    mapper(model.ControllerOwen, controller_owen, properties={'Start_Qr_Read': relationship(model.StartQrRead, primaryjoin=start_qr_read.c.id==controller_owen.c.start_qr_read_id)},)
    mapper(model.CubeWrapping, cube_wrapping, properties={'Start_Cube_Control': relationship(model.StartCubeControl, primaryjoin=start_cube_control.c.id==cube_wrapping.c.start_cube_control_id)},)
    mapper(model.ReadedQr, readed_qr, properties={'Frame': relationship(model.Frame, primaryjoin=frame.c.id==readed_qr.c.frame_id), 'Camera': relationship(model.Camera, primaryjoin=camera.c.id==readed_qr.c.camera_id)},)
    mapper(model.NotReadedQr, not_readed_qr, properties={'Frame': relationship(model.Frame, primaryjoin=frame.c.id==not_readed_qr.c.frame_id),},)
    mapper(model.Track, track, properties={'Detect': relationship(model.Detect, primaryjoin=detect.c.id==track.c.detect_id), 'Tracking_Object': relationship(model.TrackingObject, primaryjoin=tracking_object.c.id==track.c.tracking_object_id)},)
    mapper(model.QrReadCamera, qr_read_camera, properties={'Start_Qr_Read': relationship(model.StartQrRead, primaryjoin=start_qr_read.c.id==qr_read_camera.c.start_qr_read_id), 'Camera': relationship(model.Camera, primaryjoin=camera.c.id==qr_read_camera.c.camera_id)},)
    mapper(model.CubeControlCamera, cube_control_camera, properties={'Start_Cube_Control': relationship(model.StartCubeControl, primaryjoin=start_cube_control.c.id==cube_control_camera.c.start_cube_control_id), 'Camera': relationship(model.Camera, primaryjoin=camera.c.id==cube_control_camera.c.camera_id)},)
    # mapper(model.Frame, frame, properties={relationship(lines_mapper, secondary=allocations, collection_class=set,)},) 



# tracking_object = Table(
#     "tracking_object",
#     metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("reference", String(255)),
#     Column("sku", String(255)),
#     Column("_purchased_quantity", Integer, nullable=False, server_default=func.now()),
#     Column("eta", DateTime, nullable=True),
# )

# allocations = Table(
#     "allocations",
#     metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("orderline_id", ForeignKey("order_lines.id")),
#     Column("batch_id", ForeignKey("batches.id")),
# )