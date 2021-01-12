class ModelSwitchResult:
	def __init__(self) -> None:
		self.isSuccess = None
		self.faceReload = None
		self.reloadTime = None
		self.faceDB = None

	def getIsSuccess(self):
		return self.isSuccess        

	def setIsSuccess(self,isSuccess):
		self.isSuccess=isSuccess     
		

	def getFaceReload(self):
		return self.faceReload

	def setFaceReload(self,faceReload):
		self.faceReload=faceReload     
		

	def getReloadTime(self):
		return self.reloadTime

	def setReloadTime(self,reloadTime):
		self.reloadTime=reloadTime


	def getFaceDB(self):
		return self.faceDB

	def setFaceDB(self,faceDB):
		self.faceDB=faceDB
