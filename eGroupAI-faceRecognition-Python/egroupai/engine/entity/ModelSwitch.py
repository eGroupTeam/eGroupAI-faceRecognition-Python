class ModelSwitch:
    def __init__(self) -> None:
        self._newModelPath = None
        self._switchFilePath = None
        self._modelSwitchStatusPath = None
        self._enginePath = None

    def getNewModelPath(self):
        return self._newModelPath

    def setNewModelPath(self, newModelPath):
        self._newModelPath = newModelPath

    def getSwitchFilePath(self):
        return self._switchFilePath

    def setSwitchFilePath(self, switchFilePath):
        self._switchFilePath = switchFilePath

    def getModelSwitchStatusPath(self):
        return self._modelSwitchStatusPath

    def setModelSwitchStatusPath(self, modelSwitchStatusPath):
        self._modelSwitchStatusPath = modelSwitchStatusPath

    def getEnginePath(self):
        return self._enginePath

    def setEnginePath(self, enginePath):
        self._enginePath = enginePath
