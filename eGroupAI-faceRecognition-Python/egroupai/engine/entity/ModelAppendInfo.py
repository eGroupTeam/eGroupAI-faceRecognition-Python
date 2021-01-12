class ModelAppendInfo:
	def __init__(self) -> None:
		self.time = None
		self.workingFolderCheckStatus = None
		self.workingFolderStatus = None
		self.workingFolderSize = None
		self.outputFaceDBCheckStatus = None
		self.outputFaceDBStatus = None
		self.outputFaceDBSize = None
		self.DBSizeCheckStatus = None
		self.DBSize = None
		self.DBFaceDBPath = None
		self.isSucess = None
		self.errorMessage = None


	def getTime(self):     
		return self.time   

	def setTime(self,time):
		self.time=time     


	def getWorkingFolderCheckStatus(self):
		return self.workingFolderCheckStatus

	def setWorkingFolderCheckStatus(self,workingFolderCheckStatus):
		self.workingFolderCheckStatus=workingFolderCheckStatus     


	def getWorkingFolderStatus(self):
		return self.workingFolderStatus

	def setWorkingFolderStatus(self,workingFolderStatus):
		self.workingFolderStatus=workingFolderStatus


	def getWorkingFolderSize(self):
		return self.workingFolderSize

	def setWorkingFolderSize(self,workingFolderSize):
		self.workingFolderSize=workingFolderSize


	def getOutputFaceDBCheckStatus(self):
		return self.outputFaceDBCheckStatus

	def setOutputFaceDBCheckStatus(self,outputFaceDBCheckStatus):
		self.outputFaceDBCheckStatus=outputFaceDBCheckStatus


	def getOutputFaceDBStatus(self):
		return self.outputFaceDBStatus

	def setOutputFaceDBStatus(self,outputFaceDBStatus):
		self.outputFaceDBStatus=outputFaceDBStatus


	def getOutputFaceDBSize(self):
		return self.outputFaceDBSize

	def setOutputFaceDBSize(self,outputFaceDBSize):
		self.outputFaceDBSize=outputFaceDBSize


	def getDBSizeCheckStatus(self):
		return self.DBSizeCheckStatus

	def setDBSizeCheckStatus(self,DBSizeCheckStatus):
		self.DBSizeCheckStatus=DBSizeCheckStatus


	def getDBSize(self):
		return self.DBSize

	def setDBSize(self,DBSize):
		self.DBSize=DBSize


	def getDBFaceDBPath(self):
		return self.DBFaceDBPath

	def setDBFaceDBPath(self,DBFaceDBPath):
		self.DBFaceDBPath=DBFaceDBPath


	def getIsSucess(self):
		return self.isSucess

	def setIsSucess(self,isSucess):
		self.isSucess=isSucess


	def getErrorMessage(self):
		return self.errorMessage

	def setErrorMessage(self,errorMessage):
		self.errorMessage=errorMessage