from egroup.util.AttributeCheck import AttributeCheck
from egroup.util.LoggingUtil import LOGGER


class ModelAppend:
    def __init__(self):
        self._listPath = None
        self._trainedFaceDBPath = None
        self._faceDBList = None
        self._cli = None
        self._commandList = list()
        self._disk = None
        # program control
        self._enginePath = None
        self._faceDBHashset = set()
        # init func
        self._attributeCheck = None

    def getListPath(self):
        return self._listPath

    def setListPath(self, listPath):
        self._listPath = listPath

    def getCli(self):
        return self._cli

    def setCli(self, cli):
        self._cli = cli

    def getCommandList(self):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()

        if self._attributeCheck.stringsNotNull(str(self._cli)):
            self._commandList = list()
            self._commandList.append("cmd")
            self._commandList.append("/C")
            self._commandList.append(self._disk + ": && " + str(self._cli).replace("/", "/"))

        return self._commandList

    def setCommandList(self, commandList):
        self._commandList = commandList

    def getDisk(self):
        return self._disk

    def setDisk(self, disk):
        self._disk = disk

    def generateCli(self,enginePath: str):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()
        self._disk = enginePath[0]
        if self._attributeCheck.stringsNotNull(enginePath, self._disk, self._listPath, self._trainedFaceDBPath):
            self._cli = "cd " + enginePath + " && " + self._disk + ": && ModelAppend \"" + self._listPath + "\" \"" + self._trainedFaceDBPath + "\""
        else:
            self._cli = None
        LOGGER.info(f"cli={self._cli}")

    def getTrainedFaceDBPath(self):
        return self._trainedFaceDBPath

    def setTrainedFaceDBPath(self, trainedFaceDBPath):
        self._trainedFaceDBPath = trainedFaceDBPath

    def getFaceDBList(self):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()
        if not self._attributeCheck.listNotEmpty(self._faceDBList):
            self._faceDBList = list()
        return self._faceDBList

    def setFaceDBList(self, faceDBList):
        self._faceDBList = faceDBList

    def getFaceDBHashset(self) -> set:
        return self._faceDBHashset

    def setFaceDBHashset(self,faceDBHashset: set):
        self._faceDBHashset = faceDBHashset
        self._faceDBList = list(self._faceDBHashset)

    def getEnginePath(self):
        return self._enginePath

    def setEnginePath(self,enginePath):
        self._enginePath = enginePath
