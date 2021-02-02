class TrainResultData:
    def __init__(self) -> None:
        self._faceCount = None
        self._sucessCount = None
        self._failCount = None
        self._imagePerSec = None
        self._totalTime = None
        self._startTime = None
        self._endTime = None

    def getFaceCount(self):
        return self._faceCount

    def setFaceCount(self, faceCount):
        self._faceCount = faceCount

    def getSucessCount(self):
        return self._sucessCount

    def setSucessCount(self, sucessCount):
        self._sucessCount = sucessCount

    def getFailCount(self):
        return self._failCount

    def setFailCount(self, failCount):
        self._failCount = failCount

    def getImagePerSec(self):
        return self._imagePerSec

    def setImagePerSec(self, imagePerSec):
        self._imagePerSec = imagePerSec

    def getTotalTime(self):
        return self._totalTime

    def setTotalTime(self, totalTime):
        self._totalTime = totalTime

    def getStartTime(self):
        return self._startTime

    def setStartTime(self, startTime):
        self._startTime = startTime

    def getEndTime(self):
        return self._endTime

    def setEndTime(self, endTime):
        self._endTime = endTime
