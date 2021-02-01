class TrainInfo:
	def __init__(self) -> None:
		self._time = None
		self._status = None
		self._facePath = None
		self._personId = None
		self._isFaceQuality = False
		self._isFaceQualityBlurness = False
		self._isFaceQualityLowLuminance = False
		self._isFaceQualityHighLuminance = False
		self._isFaceQualityHeadpose = False

	def getTime(self) -> str:
		return self._time

	def setTime(self,time: str):
		self._time = time

	def getStatus(self) -> str:
		return self._status

	def setStatus(self,status: str):
		self._status=status


	def getFacePath(self) -> str:
		return self._facePath

	def setFacePath(self,facePath: str):
		self._facePath=facePath


	def getPersonId(self) -> str:
		return self._personId

	def setPersonId(self,personId: str):
		self._personId=personId


	def isFaceQuality (self) -> bool:
		return self._isFaceQuality

	def setFaceQuality (self,isFaceQuality: bool ):
		self._isFaceQuality =isFaceQuality


	def isFaceQualityBlurness(self) -> bool:
		return self._isFaceQualityBlurness

	def setFaceQualityBlurness(self,isFaceQualityBlurness: bool):
		self._isFaceQualityBlurness=isFaceQualityBlurness


	def isFaceQualityLowLuminance(self) -> bool:
		return self._isFaceQualityLowLuminance

	def setIsFaceQualityLowLuminance(self,isFaceQualityLowLuminance: bool):
		self._isFaceQualityLowLuminance=isFaceQualityLowLuminance


	def isFaceQualityHighLuminance(self) -> bool:
		return self._isFaceQualityHighLuminance

	def setIsFaceQualityHighLuminance(self,isFaceQualityHighLuminance: bool):
		self._isFaceQualityHighLuminance=isFaceQualityHighLuminance


	def isFaceQualityHeadpose(self) -> bool:
		return self._isFaceQualityHeadpose

	def setIsFaceQualityHeadpose(self,isFaceQualityHeadpose: bool):
		self._isFaceQualityHeadpose=isFaceQualityHeadpose
