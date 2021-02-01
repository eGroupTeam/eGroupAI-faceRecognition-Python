from egroup.util.AttributeCheck import AttributeCheck


class TrainResult:
    def __init__(self):
        self._passFacePathList = None
        self._failFacePathList = None
        self._fileSize = None
        self._faceSize = None
        self._processingTime = None
        self._avgPprocessingSpped = None
        self._trainInfoList = None
        # programe control
        self._trainResultFileExist = True
        self._trainCmdSuccess = True
        self._trainStatus = False
        self._trainSize = None
        # init func
        self._attributeCheck = None

    def isTrainResultFileExist(self):
        return self._trainResultFileExist

    def setTrainResultFileExist(self, trainResultFileExist: bool):
        self._trainResultFileExist = trainResultFileExist

    def getPassFacePathList(self):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()
        # TODO: Recheck not
        if not self._attributeCheck.listNotEmpty(self._passFacePathList):
            self._passFacePathList = list()

        return self._passFacePathList

    def setPassFacePathList(self, passFacePathList: list):
        self._passFacePathList = passFacePathList

    def getFailFacePathList(self):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()

        if not self._attributeCheck.listNotEmpty(self._failFacePathList):
            self._failFacePathList = list()
        return self._failFacePathList

    def setFailFacePathList(self, failFacePathList: list):
        self._failFacePathList = failFacePathList

    def getFileSize(self):
        return self._fileSize

    def setFileSize(self, fileSize: int):
        self._fileSize = fileSize

    def getFaceSize(self):
        return self._faceSize

    def setFaceSize(self, faceSize: int):
        self._faceSize = faceSize

    def getProcessingTime(self):
        return self._processingTime

    def setProcessingTime(self, processingTime: str):
        self._processingTime = processingTime

    def getAvgPprocessingSpped(self):
        return self._avgPprocessingSpped

    def setAvgPprocessingSpped(self, avgPprocessingSpped: str):
        self._avgPprocessingSpped = avgPprocessingSpped

    def getTrainInfoList(self):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()
        if not self._attributeCheck.listNotEmpty(self._trainInfoList):
            self._trainInfoList = list()
        return self._trainInfoList

    def setTrainInfoList(self, trainInfoList: list):
        self._trainInfoList = trainInfoList

    def isTrainCmdSuccess(self):
        return self._trainCmdSuccess

    def setTrainCmdSuccess(self, trainCmdSuccess: bool):
        self._trainCmdSuccess = trainCmdSuccess;

    def isTrainStatus(self):
        return self._trainStatus

    def setTrainStatus(self, trainStatus: bool):
        self._trainStatus = trainStatus

    def getTrainSize(self):
        return self._trainSize

    def setTrainSize(self, trainSize: int):
        self._trainSize = trainSize
