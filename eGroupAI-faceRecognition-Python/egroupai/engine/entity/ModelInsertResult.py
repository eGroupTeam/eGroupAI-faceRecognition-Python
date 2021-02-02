class ModelInsertResult:
    def __init__(self) -> None:
        self._modelInsertInfoList = None
        self._isSuccess = None
        self._faceReload = None
        self._reloadTime = None

    def to_dict(self):
        return {
            "modelInsertInfoList": [model_insert_info.to_dict() for model_insert_info in self.getModelInsertInfoList()],
            "isSuccess": self.isSuccess(),
            "faceReload": self.getFaceReload(),
            "reloadTime": self.getReloadTime(),
        }

    def getModelInsertInfoList(self):
        if self._modelInsertInfoList:
            return self._modelInsertInfoList
        return []

    def setModelInsertInfoList(self, modelInsertInfoList):
        self._modelInsertInfoList = modelInsertInfoList

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
