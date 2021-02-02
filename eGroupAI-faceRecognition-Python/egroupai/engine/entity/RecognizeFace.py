from enum import Enum

from egroup.util.AttributeCheck import AttributeCheck
from egroup.util.LoggingUtil import LOGGER


class RECOGNIZEMODE_(Enum):
    LIVENESS = "liveness"
    GENERAL = "general"


class RecognizeFace:
    def __init__(self):
        self._threshold = None
        self._resolution = None
        self._outputFramePath = None
        self._outputFacePath = None
        self._outputMotionFramePath = None
        self._webcam = None
        self._rtsp = None
        self._videoPath = None
        self._photoListPath = None
        self._minimumFaceSize = None
        self._threads = None
        self._trainedFaceDBPath = None
        self._jsonPath = None
        self._cli = None
        self._commandList = None
        self._disk = None
        self._enginePath = None
        self._isHideMainWindow = True
        self._isHideThreadWindow = True
        self._isTesting = False
        self._isIterationSearch = False
        self._isOnface = False
        self._sampleRate = None
        self._sectionId = None
        self._mainResolution = None
        self._responseTime = None
        # init program process
        self._isOutputFace = None
        self._isOutputFrame = None
        # init func
        self._attributeCheck = None

    def getThreshold(self) -> float:
        return self._threshold

    def setThreshold(self, threshold: float):
        self._threshold = threshold

    def isHideMainWindow(self) -> bool:
        return self._isHideMainWindow

    def setHideMainWindow(self, isHideMainWindow: bool):
        self._isHideMainWindow = isHideMainWindow

    def getResolution(self) -> str:
        return self._resolution

    def setResolution(self, resolution: str):
        self._resolution = resolution

    def getOutputFramePath(self) -> str:
        return self._outputFramePath

    def setOutputFramePath(self, outputFramePath: str):
        self._outputFramePath = outputFramePath

    def getOutputFacePath(self) -> str:
        return self._outputFacePath

    def setOutputFacePath(self, outputFacePath: str):
        self._outputFacePath = outputFacePath

    def getWebcam(self) -> str:
        return self._webcam

    def setWebcam(self, webcam: str):
        self._webcam = webcam

    def getRtsp(self) -> str:
        return self._rtsp

    def setRtsp(self, rtsp: str):
        self._rtsp = rtsp

    def getVideoPath(self) -> str:
        return self._videoPath

    def setVideoPath(self, videoPath: str):
        self._videoPath = videoPath

    def getPhotoListPath(self) -> str:
        return self._photoListPath

    def setPhotoListPath(self, photoListPath: str):
        self._photoListPath = photoListPath

    def getMinimumFaceSize(self) -> int:
        return self._minimumFaceSize

    def setMinimumFaceSize(self, minimumFaceSize: int):
        self._minimumFaceSize = minimumFaceSize

    def getThreads(self) -> int:
        return self._threads

    def setThreads(self, threads: int):
        self._threads = threads

    def getTrainedFaceDBPath(self) -> str:
        return self._trainedFaceDBPath

    def setTrainedFaceDBPath(self, trainedFaceDBPath: str):
        self._trainedFaceDBPath = trainedFaceDBPath

    def getJsonPath(self) -> str:
        return self._jsonPath

    def setJsonPath(self, jsonPath: str):
        self._jsonPath = jsonPath

    def getCli(self) -> str:
        return self._cli

    def setCli(self, cli: str):
        self._cli = cli

    def getEnginePath(self) -> str:
        return self._enginePath

    def setEnginePath(self, enginePath: str):
        self._enginePath = enginePath

    def generateCli(self):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()
        self._disk = self._enginePath[0]
        if self._attributeCheck.stringsNotNull(self._enginePath, self._disk, self._trainedFaceDBPath, self._jsonPath):
            inputSource = f" --cam {self._webcam}"
            if self._attributeCheck.stringsNotNull(self._rtsp):
                inputSource = f" --rtsp {self._rtsp}"
            elif self._attributeCheck.stringsNotNull(self._videoPath):
                inputSource = f" --video {self._videoPath}"
            elif self._attributeCheck.stringsNotNull(self._photoListPath):
                inputSource = f" --photo-list {self._photoListPath}"

            self._cli = f"cd {self._enginePath} && {self._disk}: && RecognizeFace --threshold {self._threshold} "
            if not self._isHideMainWindow:
                self._cli += ' --show-main-window'
            if not self._isHideThreadWindow:
                self._cli += ' --show-thread-window'
            self._cli += f' --resolution {self._resolution} ' if self._attributeCheck.stringsNotNull(
                self._resolution) else ' --resolution 720p '
            if self._isOutputFrame and self._attributeCheck.stringsNotNull(self._outputFramePath):
                self._cli += f" --output-frame \"{self._outputFramePath}\" "
            if self._isOutputFace and self._attributeCheck.stringsNotNull(self._outputFacePath):
                self._cli += f" --output-face \"{self._outputFacePath}\" "
            self._cli += inputSource
            if self._minimumFaceSize is not None:
                self._cli += f' --minimum-face-size {self._minimumFaceSize} '
            if self._attributeCheck.stringsNotNull(self._mainResolution):
                self._cli += f' --output-window-resolution {self._mainResolution} '
            self._cli += f' --threads {self._threads} ' if self._threads is not None else ' --threads 1 '
            self._cli += f' --sample-rate {self._sampleRate} ' if self._sampleRate is not None else ' --sample-rate 5 '
            if self._isTesting:
                self._cli += ' --no-imageqa '
            if self._isIterationSearch:
                self._cli += ' --enable-iteration-search '
            self._cli += f"\"{self._trainedFaceDBPath}\" \"{self._jsonPath}\""
            # if self._isOnface:
            #     self._cli += '--one-face'
        else:
            self._cli = None
        LOGGER.info(f"RecognizeFace cli : {self._cli}")

    def getStopCli(self, recognizeMode_: RECOGNIZEMODE_):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()
        self._disk = self._enginePath[0]
        if self._attributeCheck.stringsNotNull(self._enginePath, self._disk):
            if not recognizeMode_.getValue().lower() == RECOGNIZEMODE_.LIVENESS:
                self._cli = f"cd {self._enginePath} && {self._disk}: && StopRecognize.bat"
            else:
                self._cli = f"cd {self._enginePath} && {self._disk}: && StopLiveness.bat"
        else:
            self._cli = None
        LOGGER.info(f"RecognizeFace cli : {self._cli}")

    def getCommandList(self) -> list:
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()
        if self._attributeCheck.stringsNotNull(str(self._cli)):
            self._commandList = list()
            self._commandList.append("cmd")
            self._commandList.append("/C")
            self._commandList.append(f"{self._disk}: && {str(self._cli).replace('/', '/')}")
        return self._commandList

    def setCommandList(self, commandList: list):
        self._commandList = commandList

    def getDisk(self) -> str:
        return self._disk

    def setDisk(self, disk: str):
        self._disk = disk

    def isHideThreadWindow(self) -> bool:
        return self._isHideThreadWindow

    def setHideThreadWindow(self, isHideThreadWindow: bool):
        self._isHideThreadWindow = isHideThreadWindow

    def getResponseTime(self) -> int:
        return self._responseTime

    def setResponseTime(self, responseTime: int):
        self._responseTime = responseTime

    def getSectionId(self) -> str:
        return self._sectionId

    def setSectionId(self, sectionId: str):
        self._sectionId = sectionId

    def getSampleRate(self) -> int:
        return self._sampleRate

    def setSampleRate(self, sampleRate: int):
        self._sampleRate = sampleRate

    def getOutputMotionFramePath(self) -> str:
        return self._outputMotionFramePath

    def setOutputMotionFramePath(self, outputMotionFramePath: str):
        self._outputMotionFramePath = outputMotionFramePath

    def getMainResolution(self) -> str:
        return self._mainResolution

    def setMainResolution(self, mainResolution: str):
        self._mainResolution = mainResolution

    def isOutputFrame(self) -> bool:
        return self._isOutputFrame

    def setOutputFrame(self, isOutputFrame: bool):
        self._isOutputFrame = isOutputFrame

    def isTesting(self) -> bool:
        return self._isTesting

    def setTesting(self, isTesting: bool):
        self._isTesting = isTesting

    def isOnface(self) -> bool:
        return self._isOnface

    def setOnface(self, isOnface: bool):
        self._isOnface = isOnface

    def isIterationSearch(self) -> bool:
        return self._isIterationSearch

    def setIterationSearch(self, isIterationSearch: bool):
        self._isIterationSearch = isIterationSearch

    def isOutputFace(self) -> bool:
        return self._isOutputFace

    def setOutputFace(self, isOutputFace: bool):
        self._isOutputFace = isOutputFace
