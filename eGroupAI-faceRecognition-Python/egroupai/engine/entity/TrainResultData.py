class TrainResultData:
	def __init__(self) -> None:
		self.faceCount= None
		self.sucessCount= None
		self.failCount= None
		self.imagePerSec= None
		self.totalTime= None
		self.startTime= None
		self.endTime= None

	def getFaceCount(self):
		return self.faceCount

	def setFaceCount(self,faceCount):
		self.faceCount=faceCount


	def getSucessCount(self):
		return self.sucessCount

	def setSucessCount(self,sucessCount):
		self.sucessCount=sucessCount


	def getFailCount(self):
		return self.failCount

	def setFailCount(self,failCount):
		self.failCount=failCount


	def getImagePerSec(self):
		return self.imagePerSec

	def setImagePerSec(self,imagePerSec):
		self.imagePerSec=imagePerSec


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
