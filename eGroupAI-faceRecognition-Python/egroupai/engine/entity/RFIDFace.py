class RFIDFace:
    def __init__(self) -> None:
        self._hasFound = None
        self._faceSize = None
        self._faceConsecutiveFrame = None
        self._faceDurationFrame = None

    def getHasFound(self):
        return self._hasFound

    def setHasFound(self, hasFound):
        self._hasFound = hasFound

    def getFaceSize(self):
        return self._faceSize

    def setFaceSize(self, faceSize):
        self._faceSize = faceSize

    def getFaceConsecutiveFrame(self):
        return self._faceConsecutiveFrame

    def setFaceConsecutiveFrame(self, faceConsecutiveFrame):
        self._faceConsecutiveFrame = faceConsecutiveFrame

    def getFaceDurationFrame(self):
        return self._faceDurationFrame

    def setFaceDurationFrame(self, faceDurationFrame):
        self._faceDurationFrame = faceDurationFrame
