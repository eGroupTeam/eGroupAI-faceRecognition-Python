class SimilarFace:
	def __init__(self) -> None:
		self.personFaceId=None
		self.personFacePath=None
		self.similarity=None

	def getPersonFaceId(self):
		return self.personFaceId


	def setPersonFaceId(self,personFaceId):
		self.personFaceId=personFaceId     
		

	def getPersonFacePath(self):
		return self.personFacePath

	def setPersonFacePath(self,personFacePath):
		self.personFacePath=personFacePath     
		

	def getSimilarity(self):
		return self.similarity

	def setSimilarity(self,similarity):
		self.similarity=similarity
