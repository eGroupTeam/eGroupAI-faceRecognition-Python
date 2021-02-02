class RecognizeResultData:
    def __init__(self) -> None:
        self._imageCount = None
        self._imagePerSec = None
        self._totalTime = None
        self._startTime = None
        self._endTime = None

    def getImageCount(self):
        return self._imageCount

    def setImageCount(self, imageCount):
        self._imageCount = imageCount

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
