class ModelInsertResult:
	def __init__(self) -> None:
		self.modelInsertInfoList= None
		self.isSuccess= None
		self.faceReload= None
		self.reloadTime= None


	def getModelInsertInfoList(self):
		if self.modelInsertInfoList:
			return self.modelInsertInfoList
		return []

	def setModelInsertInfoList(self,modelInsertInfoList):
		self.modelInsertInfoList=modelInsertInfoList     
		

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

