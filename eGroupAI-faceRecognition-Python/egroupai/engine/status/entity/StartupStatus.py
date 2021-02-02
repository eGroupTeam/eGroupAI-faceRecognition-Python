class StartupStatus:
    def __init__(self) -> None:
        self._checkId = None
        self._checkName = None
        self._checkFlag = None

    def getCheckId(self, checkId):
        self._checkId = checkId

    def setCheckId(self, checkId: int):
        self._checkId = checkId

    def getCheckName(self):
        return self._checkName

    def setCheckName(self, checkName):
        self._checkName = checkName

    def isCheckFlag(self):
        return self._checkFlag

    def setCheckFlag(self, checkFlag):
        self._checkFlag = checkFlag
