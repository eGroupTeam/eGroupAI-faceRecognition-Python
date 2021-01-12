class ModelSwitch:
	def __init__(self) -> None:
		self.newModelPath = None
		self.switchFilePath = None
		self.modelSwitchStatusPath = None
		self.enginePath = None

	def getNewModelPath(self):
		return self.newModelPath

	def setNewModelPath(self,newModelPath):
		self.newModelPath=newModelPath     
		

	def getSwitchFilePath(self):
		return self.switchFilePath

	def setSwitchFilePath(self,switchFilePath):
		self.switchFilePath=switchFilePath     
		

	def getModelSwitchStatusPath(self):        
		return self.modelSwitchStatusPath      

	def setModelSwitchStatusPath(self,modelSwitchStatusPath):
		self.modelSwitchStatusPath=modelSwitchStatusPath


	def getEnginePath(self):
		return self.enginePath

	def setEnginePath(self,enginePath):
		self.enginePath=enginePath