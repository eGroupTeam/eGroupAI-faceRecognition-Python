class TrainInfo:
	def __init__(self) -> None:
		self.time=None
		self.status=None
		self.facePath=None
		self.personId=None
		self.isFaceQuality =None
		self.isFaceQualityBlurness = None
		self.isFaceQualityLowLuminance = None
		self.isFaceQualityHighLuminance = None
		self.isFaceQualityHeadpose = None

	def getTime(self):  
		return self.time

	def setTime(self,time):
		self.time=time

	def getStatus(self):
		return self.status

	def setStatus(self,status):
		self.status=status


	def getFacePath(self):
		return self.facePath

	def setFacePath(self,facePath):
		self.facePath=facePath


	def getPersonId(self):
		return self.personId

	def setPersonId(self,personId):
		self.personId=personId


	def getIsFaceQuality (self):
		return self.isFaceQuality

	def setIsFaceQuality (self,isFaceQuality ):
		self.isFaceQuality =isFaceQuality


	def getIsFaceQualityBlurness(self):
		return self.isFaceQualityBlurness

	def setIsFaceQualityBlurness(self,isFaceQualityBlurness):
		self.isFaceQualityBlurness=isFaceQualityBlurness


	def getIsFaceQualityLowLuminance(self):
		return self.isFaceQualityLowLuminance

	def setIsFaceQualityLowLuminance(self,isFaceQualityLowLuminance):
		self.isFaceQualityLowLuminance=isFaceQualityLowLuminance


	def getIsFaceQualityHighLuminance(self):
		return self.isFaceQualityHighLuminance

	def setIsFaceQualityHighLuminance(self,isFaceQualityHighLuminance):
		self.isFaceQualityHighLuminance=isFaceQualityHighLuminance


	def getIsFaceQualityHeadpose(self):
		return self.isFaceQualityHeadpose

	def setIsFaceQualityHeadpose(self,isFaceQualityHeadpose):
		self.isFaceQualityHeadpose=isFaceQualityHeadpose