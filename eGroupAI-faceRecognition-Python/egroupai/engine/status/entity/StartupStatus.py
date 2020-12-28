class StartupStatus:
    def __init__(self) -> None:
        self.checkId=None
        self.checkName=None
        self.checkFlag=None

    def getCheckId(self,checkId):
        self.checkId=checkId

    def setCheckId(self,checkId: int):
        self.checkId=checkId
    
    def getCheckName(self):
        return self.checkName

    def setCheckName(self,checkName):
        self.checkName=checkName
    
    def isCheckFlag(self):
        return self.checkFlag
    
    def setCheckFlag(self,checkFlag):
        self.checkFlag=checkFlag
