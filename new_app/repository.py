import abc
import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def addCamera(self, camera: model.Camera):
        raise NotImplementedError

    @abc.abstractmethod
    def getCamera(self, reference) -> model.Camera:
        raise NotImplementedError


    @abc.abstractmethod
    def addTrackingObject(self, tracking_object: model.TrackingObject):
        raise NotImplementedError

    @abc.abstractmethod
    def getTrackingObject(self, reference) -> model.TrackingObject:
        raise NotImplementedError
    

    @abc.abstractmethod
    def addFrame(self, frame: model.Frame):
        raise NotImplementedError

    @abc.abstractmethod
    def getFrame(self, reference) -> model.Frame:
        raise NotImplementedError


    @abc.abstractmethod
    def addDetect(self, detect: model.Detect):
        raise NotImplementedError

    @abc.abstractmethod
    def getDetect(self, reference) -> model.Detect:
        raise NotImplementedError
    

    @abc.abstractmethod
    def addTrack(self, batch: model.Track):
        raise NotImplementedError

    @abc.abstractmethod
    def getTrack(self, reference) -> model.Track:
        raise NotImplementedError


    @abc.abstractmethod
    def addStartCubeControl(self, batch: model.StartCubeControl):
        raise NotImplementedError

    @abc.abstractmethod
    def getStartCubeControl(self, reference) -> model.StartCubeControl:
        raise NotImplementedError
    

    @abc.abstractmethod
    def addStartQrRead(self, batch: model.StartQrRead):
        raise NotImplementedError

    @abc.abstractmethod
    def getStartQrRead(self, reference) -> model.StartQrRead:
        raise NotImplementedError


    @abc.abstractmethod
    def addControllerOwen(self, batch: model.ControllerOwen):
        raise NotImplementedError

    @abc.abstractmethod
    def getControllerOwen(self, reference) -> model.ControllerOwen:
        raise NotImplementedError
    

    @abc.abstractmethod
    def addCubeWrapping(self, batch: model.CubeWrapping):
        raise NotImplementedError

    @abc.abstractmethod
    def getCubeWrapping(self, reference) -> model.CubeWrapping:
        raise NotImplementedError


    @abc.abstractmethod
    def addReadedQr(self, batch: model.ReadedQr):
        raise NotImplementedError

    @abc.abstractmethod
    def getReadedQr(self, reference) -> model.ReadedQr:
        raise NotImplementedError
    

    @abc.abstractmethod
    def addNotReadedQr(self, batch: model.NotReadedQr):
        raise NotImplementedError

    @abc.abstractmethod
    def getNotReadedQr(self, reference) -> model.NotReadedQr:
        raise NotImplementedError


    @abc.abstractmethod
    def addQrReadCamera(self, batch: model.QrReadCamera):
        raise NotImplementedError

    @abc.abstractmethod
    def getQrReadCamera(self, reference) -> model.QrReadCamera:
        raise NotImplementedError
    

    @abc.abstractmethod
    def addCubeControlCamera(self, batch: model.CubeControlCamera):
        raise NotImplementedError

    @abc.abstractmethod
    def getCubeControlCamera(self, reference) -> model.CubeControlCamera:
        raise NotImplementedError
    
    
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def list(self):                                     
        return self.session.query(model.Batch).all()    