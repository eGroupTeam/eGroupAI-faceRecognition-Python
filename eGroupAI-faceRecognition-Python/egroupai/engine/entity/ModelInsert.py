from egroup.util.AttributeCheck import AttributeCheck


class ModelInsert:
    def __init__(self):
        self._ListPath = None
        self._enginePath = None
        self._faceDBList = None
        # init func
        self._attributeCheck = None

    def getListPath(self):
        return self._ListPath

    def setListPath(self, ListPath):
        self._ListPath = ListPath

    def getEnginePath(self):
        return self._enginePath

    def setEnginePath(self, enginePath):
        self._enginePath = enginePath

    def getFaceDBList(self):
        if self._attributeCheck is None:
            self._attributeCheck = AttributeCheck()
        if not self._attributeCheck.listNotEmpty(self._faceDBList):
            self._faceDBList = list()
        return self._faceDBList

    def setFaceDBList(self, faceDBList):
        self._faceDBList = faceDBList
