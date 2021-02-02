from egroupai.engine.entity.FrameFace import FrameFace


class FACEQUALITY:
    C1 = "人臉圖模糊"
    C2 = "人臉圖過暗"
    C3 = "人臉圖過亮"
    C4 = "人臉圖非正臉"
    PASS = "人臉圖品質通過"

    def __init__(self, value: str):
        self._value = value

    def getValue(self) -> str:
        return self._value


class Face:
    def __init__(self):
        self._hasFound = None
        self._personId = None
        self._similarFaceList = None
        self._frameFace = None
        self._framePath = None
        self._systemTime = None
        self._videoTime = None
        self._videoFrameNo = None
        self._imageSourcePath = None
        self._faceQuality = None
        self._faceQualityBlurness = None
        self._faceQualityLowLuminance = None
        self._faceQualityHighLuminance = None
        self._faceQualityHeadpose = None
        self._faceQualityName = None
        self._faceSize = None
        self._livenessHeadposeX = None
        self._livenessHeadposeY = None
        self._livenessHeadposeZ = None
        self._livenessHeadposeClass = None
        self._result = None
        self._questionID = None
        self._faceLabel = None
        self._depthInfo = None

        # program control
        self._startIndex = None
        self._endIndex = None
        self._success = None
        self._message = None
        self._statusCode = None

    def getHasFound(self):
        return self._hasFound

    def setHasFound(self, hasFound: str):
        self._hasFound = hasFound

    def getPersonId(self):
        return self._personId

    def setPersonId(self, personId):
        self._personId = personId

    def getSimilarFaceList(self):
        if self._similarFaceList:
            return self._similarFaceList
        return []

    def setSimilarFaceList(self, similarFaceList: list):
        self._similarFaceList = similarFaceList

    def getFrameFace(self):
        if self._frameFace:
            return self._frameFace
        return FrameFace()

    def setFrameFace(self, frameFace):
        if type(frameFace) is not FrameFace:
            raise ValueError("frameFace should be instance of FrameFace")

    def getFramePath(self):
        return self._framePath

    def setFramePath(self, framePath: str):
        self._framePath = framePath

    def getSystemTime(self):
        return self._systemTime

    def setSystemTime(self, systemTime: str):
        self._systemTime = systemTime

    def getVideoTime(self):
        return self._videoTime

    def setVideoTime(self, videoTime):
        self._videoTime = videoTime

    def getVideoFrameNo(self):
        return self._videoFrameNo

    def setVideoFrameNo(self, videoFrameNo):
        self._videoFrameNo = videoFrameNo

    def getImageSourcePath(self):
        return self._imageSourcePath

    def setImageSourcePath(self, imageSourcePath):
        self._imageSourcePath = imageSourcePath

    def getFaceQuality(self):
        return self._faceQuality

    def setFaceQuality(self, faceQuality):
        self._faceQuality = faceQuality

    def getFaceQualityBlurness(self):
        return self._faceQualityBlurness

    def setFaceQualityBlurness(self, faceQualityBlurness):
        self._faceQualityBlurness = faceQualityBlurness

    def getFaceQualityLowLuminance(self):
        return self._faceQualityLowLuminance

    def setFaceQualityLowLuminance(self, faceQualityLowLuminance):
        self._faceQualityLowLuminance = faceQualityLowLuminance

    def getFaceQualityHighLuminance(self):
        return self._faceQualityHighLuminance

    def setFaceQualityHighLuminance(self, faceQualityHighLuminance):
        self._faceQualityHighLuminance = faceQualityHighLuminance

    def getFaceQualityHeadpose(self):
        return self._faceQualityHeadpose

    def setFaceQualityHeadpose(self, faceQualityHeadpose):
        self._faceQualityHeadpose = faceQualityHeadpose

    def getFaceQualityName(self):
        return self._faceQualityName

    def setFaceQualityName(self, faceQualityName):
        self._faceQualityName = faceQualityName

    def getFaceSize(self):
        return self._faceSize

    def setFaceSize(self, faceSize):
        self._faceSize = faceSize

    def getLivenessHeadposeX(self):
        return self._livenessHeadposeX

    def setLivenessHeadposeX(self, livenessHeadposeX):
        self._livenessHeadposeX = livenessHeadposeX

    def getLivenessHeadposeY(self):
        return self._livenessHeadposeY

    def setLivenessHeadposeY(self, livenessHeadposeY):
        self._livenessHeadposeY = livenessHeadposeY

    def getLivenessHeadposeZ(self):
        return self._livenessHeadposeZ

    def setLivenessHeadposeZ(self, livenessHeadposeZ):
        self._livenessHeadposeZ = livenessHeadposeZ

    def getLivenessHeadposeClass(self):
        return self._livenessHeadposeClass

    def setLivenessHeadposeClass(self, livenessHeadposeClass):
        self._livenessHeadposeClass = livenessHeadposeClass

    def getResult(self):
        return self._result

    def setResult(self, result):
        self._result = result

    def getQuestionID(self):
        return self._questionID

    def setQuestionID(self, questionID):
        self._questionID = questionID

    def getFaceLabel(self):
        return self._faceLabel

    def setFaceLabel(self, faceLabel):
        self._faceLabel = faceLabel

    def getDepthInfo(self):
        return self._depthInfo

    def setDepthInfo(self, depthInfo):
        self._depthInfo = depthInfo
