from .FrameFace import FrameFace

class FACEQUALITY:
    C1="人臉圖模糊"
    C2="人臉圖過暗"
    C3="人臉圖過亮"
    C4="人臉圖非正臉"
    PASS="人臉圖品質通過"

    def __init__(self,value: str) -> None:
        self.value=value 

    def getValue(self)->str:
        return self.value


class Face:
    def __init__(self) -> None:
        self.hasFound=None
        self.personId=None
        self.similarFaceList=None
        self.frameFace=None
        self.framePath=None
        self.systemTime=None
        self.videoTime=None
        self.videoFrameNo=None
        self.imageSourcePath=None
        self.faceQuality=None
        self.faceQualityBlurness=None
        self.faceQualityLowLuminance=None
        self.faceQualityHighLuminance=None
        self.faceQualityHeadpose=None
        self.faceQualityName=None
        self.faceSize=None
        self.livenessHeadposeX=None
        self.livenessHeadposeY=None
        self.livenessHeadposeZ=None
        self.livenessHeadposeClass=None
        self.result=None
        self.questionID=None
        self.faceLabel=None
        self.depthInfo=None

        # program control
        self.startIndex=None
        self.endIndex=None
        self.success=None
        self.message=None
        self.statusCode=None

    def getHasFound(self):
        return self.hasFound
    
    def setHasFound(self,hasFound: str):
        self.hasFound=hasFound
    

    def getPersonId(self):
        return self.personId
    
    def setPersonId(self,personId):
        self.personId=personId
    
    def getSimilarFaceList(self):
        if self.similarFaceList:
            return self.similarFaceList
        return []
    def setSimilarFaceList(self,similarFaceList: list):
        self.similarFaceList=similarFaceList

    def getFrameFace(self):
        if self.frameFace:
            return self.frameFace
        return FrameFace()
    
    def setFrameFace(self,frameFace):
        if type(frameFace) is not FrameFace:
            raise ValueError("frameFace should be instance of FrameFace")

    def getFramePath(self):
        return self.framePath
    
    def setFramePath(self,framePath: str):
        self.framePath=framePath

    def getSystemTime(self):
        return self.systemTime
    
    def setSystemTime(self,systemTime: str):
        self.systemTime=systemTime


    def getVideoTime(self):
        return self.videoTime        

    def setVideoTime(self,videoTime):
        self.videoTime=videoTime     
        

    def getVideoFrameNo(self):
        return self.videoFrameNo

    def setVideoFrameNo(self,videoFrameNo):
        self.videoFrameNo=videoFrameNo     
        

    def getImageSourcePath(self):
        return self.imageSourcePath

    def setImageSourcePath(self,imageSourcePath):
        self.imageSourcePath=imageSourcePath


    def getFaceQuality(self):
        return self.faceQuality

    def setFaceQuality(self,faceQuality):
        self.faceQuality=faceQuality


    def getFaceQualityBlurness(self):
        return self.faceQualityBlurness

    def setFaceQualityBlurness(self,faceQualityBlurness):
        self.faceQualityBlurness=faceQualityBlurness


    def getFaceQualityLowLuminance(self):
        return self.faceQualityLowLuminance

    def setFaceQualityLowLuminance(self,faceQualityLowLuminance):
        self.faceQualityLowLuminance=faceQualityLowLuminance


    def getFaceQualityHighLuminance(self):
        return self.faceQualityHighLuminance

    def setFaceQualityHighLuminance(self,faceQualityHighLuminance):
        self.faceQualityHighLuminance=faceQualityHighLuminance


    def getFaceQualityHeadpose(self):
        return self.faceQualityHeadpose

    def setFaceQualityHeadpose(self,faceQualityHeadpose):
        self.faceQualityHeadpose=faceQualityHeadpose


    def getFaceQualityName(self):
        return self.faceQualityName

    def setFaceQualityName(self,faceQualityName):
        self.faceQualityName=faceQualityName


    def getFaceSize(self):
        return self.faceSize

    def setFaceSize(self,faceSize):
        self.faceSize=faceSize


    def getLivenessHeadposeX(self):
        return self.livenessHeadposeX

    def setLivenessHeadposeX(self,livenessHeadposeX):
        self.livenessHeadposeX=livenessHeadposeX


    def getLivenessHeadposeY(self):
        return self.livenessHeadposeY

    def setLivenessHeadposeY(self,livenessHeadposeY):
        self.livenessHeadposeY=livenessHeadposeY


    def getLivenessHeadposeZ(self):
        return self.livenessHeadposeZ

    def setLivenessHeadposeZ(self,livenessHeadposeZ):
        self.livenessHeadposeZ=livenessHeadposeZ


    def getLivenessHeadposeClass(self):
        return self.livenessHeadposeClass

    def setLivenessHeadposeClass(self,livenessHeadposeClass):
        self.livenessHeadposeClass=livenessHeadposeClass


    def getResult(self):
        return self.result

    def setResult(self,result):
        self.result=result


    def getQuestionID(self):
        return self.questionID

    def setQuestionID(self,questionID):
        self.questionID=questionID


    def getFaceLabel(self):
        return self.faceLabel

    def setFaceLabel(self,faceLabel):
        self.faceLabel=faceLabel


    def getDepthInfo(self):
        return self.depthInfo

    def setDepthInfo(self,depthInfo):
        self.depthInfo=depthInfo
