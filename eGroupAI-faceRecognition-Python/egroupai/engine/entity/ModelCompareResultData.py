class ModelCompareResultData:
	def __init__(self) -> None:
		self.totalTime= None
		self.startTime= None
		self.endTime= None
		self.imagePerSec= None
		self.samPersonCount= None
		self.notSamPersonCount= None

	def getTotalTime(self):
		return self.totalTime        

	def setTotalTime(self,totalTime):
		self.totalTime=totalTime     
		

	def getStartTime(self):
		return self.startTime        

	def setStartTime(self,startTime):
		self.startTime=startTime     
		

	def getEndTime(self):
		return self.endTime

	def setEndTime(self,endTime):
		self.endTime=endTime


	def getImagePerSec(self):
		return self.imagePerSec

	def setImagePerSec(self,imagePerSec):
		self.imagePerSec=imagePerSec

	def getSamPersonCount(self):
		return self.samPersonCount

	def setSamPersonCount(self,samPersonCount):
		self.samPersonCount=samPersonCount


	def getNotSamPersonCount(self):
		return self.notSamPersonCount

	def setNotSamPersonCount(self,notSamPersonCount):
		self.notSamPersonCount=notSamPersonCount
		
