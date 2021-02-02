class SimilarFace:
    def __init__(self) -> None:
        self._personFaceId = None
        self._personFacePath = None
        self._similarity = None

    def getPersonFaceId(self):
        return self._personFaceId

    def setPersonFaceId(self, personFaceId):
        self._personFaceId = personFaceId

    def getPersonFacePath(self):
        return self._personFacePath

    def setPersonFacePath(self, personFacePath):
        self._personFacePath = personFacePath

    def getSimilarity(self):
        return self._similarity

    def setSimilarity(self, similarity):
        self._similarity = similarity
