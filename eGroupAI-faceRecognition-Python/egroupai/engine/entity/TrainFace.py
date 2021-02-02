from egroup.util.AttributeCheck import AttributeCheck
from egroup.util.LoggingUtil import LOGGER
from egroupai.engine.entity.TrainResult import TrainResult


class TrainFace:
    def __init__(self):
        self._isModelExist = None
        self._trainListPath = None
        self._modelPath = None
        self._cli = None
        self._commandList = None
        self._disk = None
        self._trainResult = None

        # programe control
        self._imagePathList = None
        self._personId = None
        self._imagePathJson = None
        self._uploadFace = False
        self._isGGPass = False

        # blackwhite variable
        self._hasTrainFaceCount = None
        self._train_successCount = None
        self._train_failCount = None
        self._enginePath = None
        self._trainResultList = None
        self._attributeCheck = None

    def getAttributeCheck(self) -> AttributeCheck:
        if self._attributeCheck is None:
          self._attributeCheck = AttributeCheck()
        return self._attributeCheck

    def setAttributeCheck(self,attributeCheck: AttributeCheck):
        self._attributeCheck = attributeCheck

    def isModelExist(self) -> bool:
        return self._isModelExist

    def setModelExist(self,isModelExist: bool):
        self._isModelExist = isModelExist

    def getTrainListPath(self) -> str:
        return self._trainListPath

    def setTrainListPath(self, trainListPath: str):
        self._trainListPath = trainListPath

    def getModelPath(self) -> str:
        return self._modelPath

    def setModelPath(self, modelPath: str):
        self._modelPath = modelPath

    def getCli(self) -> str:
        return self._cli

    def generateCli(self):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()

        self._disk = self._enginePath[0]
        if self._attributeCheck.stringsNotNull(self._enginePath, self._disk, self._trainListPath, self._modelPath):
            if self._isModelExist:
                self._cli = f"cd {self._enginePath} && {self._disk}: && TrainFace {' --eGroupGGPass ' if self._isGGPass else ''} --append \"{self._trainListPath}\" \"{self._modelPath}\""
            else:
                self._cli = f"cd {self._enginePath} && {self._disk}: && TrainFace {' --eGroupGGPass ' if self._isGGPass else ''} \"{self._trainListPath}\" \"{self._modelPath}\""
        else:
            self._cli = None
        LOGGER.info(f"cli={self._cli}")

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

    def getImagePathList(self) -> list:
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()

        if not self._attributeCheck.listNotEmpty(self._imagePathList):
            self._imagePathList = list()

        return self._imagePathList

    def setImagePathList(self, imagePathList: list):
        self._imagePathList = imagePathList

    def getImagePathJson(self) -> str:
        return self._imagePathJson

    def setImagePathJson(self, imagePathJson: str):
        self._imagePathJson = imagePathJson

    def getPersonId(self) -> str:
        return self._personId

    def setPersonId(self, personId: str):
        self._personId = personId

    def isUploadFace(self) -> bool:
        return self._uploadFace

    def setUploadFace(self, uploadFace: bool):
        self._uploadFace = uploadFace

    def getHasTrainFaceCount(self) -> int:
        return self._hasTrainFaceCount

    def setHasTrainFaceCount(self, hasTrainFaceCount: int):
        self._hasTrainFaceCount = hasTrainFaceCount

    def getEnginePath(self) -> str:
        return self._enginePath

    def setEnginePath(self, enginePath: str):
        self._enginePath = enginePath

    def getTrain_successCount(self) -> int:
        return self._train_successCount

    def setTrain_successCount(self, train_successCount: int):
        self._train_successCount = train_successCount

    def getTrain_failCount(self) -> int:
        return self._train_failCount

    def setTrain_failCount(self, train_failCount: int):
        self._train_failCount = train_failCount

    def getTrainResultList(self) -> list:
        return self._trainResultList

    def setTrainResultList(self, trainResultList: list):
        self._trainResultList = trainResultList

    def getTrainResult(self) -> TrainResult:
        if self._trainResult is None:
            self._trainResult = TrainResult()

        return self._trainResult

    def setTrainResult(self, trainResult: TrainResult):
        self._trainResult = trainResult

    def isGGPass(self) -> bool:
        return self._isGGPass

    def setGGPass(self, isGGPass: bool):
        self._isGGPass = isGGPass
