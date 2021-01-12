class RecognizeResultData:
	def __init__(self) -> None:	
		self.imageCount = None
		self.imagePerSec = None
		self.totalTime = None
		self.startTime = None
		self.endTime = None


	def getImageCount(self):
		return self.imageCount

	def setImageCount(self,imageCount):
		self.imageCount=imageCount     
		

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

