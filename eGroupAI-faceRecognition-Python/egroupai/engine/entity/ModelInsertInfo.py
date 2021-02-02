class ModelInsertInfo:

    def __init__(self) -> None:
        self._datetimeString = None
        self._insertModelStatus = None
        self._insertFacesCount = None
        self._insertPeopleCount = None
        self._CurrDBFaceCout = None
        self._CurrDBPeopleCount = None
        self._insertProcessTime = None

    def to_dict(self):
        return {
            "insertFacesCount": self.getInsertFacesCount(),
            "insertPeopleCount": self.getInsertPeopleCount(),
            "CurrDBFaceCout": self.getCurrDBFaceCout(),
            "CurrDBPeopleCount": self.getCurrDBPeopleCount(),
        }

    def getDatetimeString(self):
        return self._datetimeString

    def setDatetimeString(self, datetimeString):
        self._datetimeString = datetimeString

    def getInsertModelStatus(self):
        return self._insertModelStatus

    def setInsertModelStatus(self, insertModelStatus):
        self._insertModelStatus = insertModelStatus

    def getInsertFacesCount(self):
        return self._insertFacesCount

    def setInsertFacesCount(self, insertFacesCount):
        self._insertFacesCount = insertFacesCount

    def getInsertPeopleCount(self):
        return self._insertPeopleCount

    def setInsertPeopleCount(self, insertPeopleCount):
        self._insertPeopleCount = insertPeopleCount

    def getCurrDBFaceCout(self):
        return self._CurrDBFaceCout

    def setCurrDBFaceCout(self, CurrDBFaceCout):
        self._CurrDBFaceCout = CurrDBFaceCout

    def getCurrDBPeopleCount(self):
        return self._CurrDBPeopleCount

    def setCurrDBPeopleCount(self, CurrDBPeopleCount):
        self._CurrDBPeopleCount = CurrDBPeopleCount

    def getInsertProcessTime(self):
        return self._insertProcessTime

    def setInsertProcessTime(self, insertProcessTime):
        self._insertProcessTime = insertProcessTime
