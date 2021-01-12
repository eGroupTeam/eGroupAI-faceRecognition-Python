class ModelCompareInfo:
	def __init__(self) -> None:
		self.filePath1 = None
		self.filePath2 = None
		self.isSamPerson = None
		self.confidence = None

	def getFilePath1(self):
		return self.filePath1        

	def setFilePath1(self,filePath1):
		self.filePath1=filePath1     
		

	def getFilePath2(self):
		return self.filePath2        

	def setFilePath2(self,filePath2):
		self.filePath2=filePath2     
		

	def getIsSamPerson(self):        
		return self.isSamPerson      

	def setIsSamPerson(self,isSamPerson):
		self.isSamPerson=isSamPerson


	def getConfidence(self):
		return self.confidence

	def setConfidence(self,confidence):
		self.confidence=confidence


