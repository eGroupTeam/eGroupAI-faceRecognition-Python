class ModelAppendResult:
	def __init__(self) -> None:
		self.modelListCheckStatus = None
		self.modelListPath = None
		self.modelAppendInfoList = None
		self.appendPassCount = None
		self.appendFailCount = None
		self.totalFaceCount = None
		self.appendCmdSuccess = True

	def getModelListCheckStatus(self):
		return self.modelListCheckStatus

	def setModelListCheckStatus(self,modelListCheckStatus):
		self.modelListCheckStatus=modelListCheckStatus     


	def getModelListPath(self):
		if self.modelListPath:
			return self.modelListPath
		return []

	def setModelListPath(self,modelListPath):
		self.modelListPath=modelListPath     


	def getModelAppendInfoList(self):  
		if self.modelAppendInfoList:      
			return self.modelAppendInfoList     
		return [] 

	def setModelAppendInfoList(self,modelAppendInfoList):
		self.modelAppendInfoList=modelAppendInfoList


	def getAppendPassCount(self):
		return self.appendPassCount

	def setAppendPassCount(self,appendPassCount):
		self.appendPassCount=appendPassCount


	def getAppendFailCount(self):
		return self.appendFailCount

	def setAppendFailCount(self,appendFailCount):
		self.appendFailCount=appendFailCount


	def getTotalFaceCount(self):
		return self.totalFaceCount

	def setTotalFaceCount(self,totalFaceCount):
		self.totalFaceCount=totalFaceCount


	def getAppendCmdSuccess(self):
		return self.appendCmdSuccess

	def setAppendCmdSuccess(self,appendCmdSuccess):
		self.appendCmdSuccess=appendCmdSuccess
