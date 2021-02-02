class ModelSwitchResult:
    def __init__(self) -> None:
        self._isSuccess = None
        self._faceReload = None
        self._reloadTime = None
        self._faceDB = None

    def isSuccess(self):
        return self._isSuccess

    def setSuccess(self, isSuccess):
        self._isSuccess = isSuccess

    def getFaceReload(self):
        return self._faceReload

    def setFaceReload(self, faceReload):
        self._faceReload = faceReload

    def getReloadTime(self):
        return self._reloadTime

    def setReloadTime(self, reloadTime):
        self._reloadTime = reloadTime

    def getFaceDB(self):
        return self._faceDB

    def setFaceDB(self, faceDB):
        self._faceDB = faceDB
