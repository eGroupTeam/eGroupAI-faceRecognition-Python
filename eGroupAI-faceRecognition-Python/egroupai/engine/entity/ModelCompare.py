import logging

from egroup.util.AttributeCheck import AttributeCheck


class ModelCompare:
    # TODO: add logging

    def __init__(self) -> None:
        self._threshold = None
        self._modelFaceDBPathA = None
        self._modelFaceDBPathB = None
        self._outputCsvPath = None
        self._cli = None
        self._commandList = None
        self._disk = None
        self._enginePath = None
        # init func
        self._attributeCheck = None

    def getThreshold(self) -> float:
        return self._threshold

    def setThreshold(self, threshold: float):
        self._threshold = threshold

    def getModelFaceDBPathA(self) -> str:
        return self._modelFaceDBPathA

    def setModelFaceDBPathA(self, modelFaceDBPathA: str):
        self._modelFaceDBPathA = modelFaceDBPathA

    def getModelFaceDBPathB(self) -> str:
        return self._modelFaceDBPathB

    def setModelFaceDBPathB(self, modelFaceDBPathB: str):
        self._modelFaceDBPathB = modelFaceDBPathB

    def getCli(self):
        return self._cli

    def setCli(self, cli):
        self._cli = cli

    def getEnginePath(self):
        return self._enginePath

    def setEnginePath(self, enginePath):
        self._enginePath = enginePath

    def getCommandList(self):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()

        if self._attributeCheck.stringsNotNull(self._cli.toString()):
            commandList = list()
            commandList.append("cmd")
            commandList.append("/C")
            commandList.append(self._disk + ": && " + str(self._cli).replace("/", "/"))
        return self._commandList

    def setCommandList(self, commandList):
        self._commandList = commandList

    def getOutputCsvPath(self):
        return self._outputCsvPath

    def setOutputCsvPath(self, outputCsvPath):
        self._outputCsvPath = outputCsvPath

    def generateCli(self):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()

        self._disk = self._enginePath[0]
        if self._attributeCheck.stringsNotNull(self._enginePath, self._disk):
            self._cli = (
                        "cd " + self._enginePath + " && " + self._disk + ": && ModelCompare " + self._threshold + " " + " \"" + self._modelFaceDBPathA + "\" \"" + self._modelFaceDBPathB + "\" \"" + self._outputCsvPath + "\"");
        else:
            self._cli = None
        # TODO: add logging
        # LOGGER.info("RecognizeFace cli : " + cli);
