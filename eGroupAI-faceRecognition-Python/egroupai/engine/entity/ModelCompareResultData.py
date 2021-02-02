class ModelCompareResultData:
    def __init__(self) -> None:
        self._totalTime = None
        self._startTime = None
        self._endTime = None
        self._imagePerSec = None
        self._samPersonCount = None
        self._notSamPersonCount = None

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

    def getImagePerSec(self):
        return self._imagePerSec

    def setImagePerSec(self, imagePerSec):
        self._imagePerSec = imagePerSec

    def getSamPersonCount(self):
        return self._samPersonCount

    def setSamPersonCount(self, samPersonCount):
        self._samPersonCount = samPersonCount

    def getNotSamPersonCount(self):
        return self._notSamPersonCount

    def setNotSamPersonCount(self, notSamPersonCount):
        self._notSamPersonCount = notSamPersonCount
