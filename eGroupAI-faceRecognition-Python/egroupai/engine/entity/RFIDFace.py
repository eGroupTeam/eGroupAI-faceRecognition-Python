class RFIDFace:
	def __init__(self) -> None:
		self.hasFound=None
		self.faceSize=None
		self.faceConsecutiveFrame=None
		self.faceDurationFrame=None

	def getHasFound(self):
		return self.hasFound       

	def setHasFound(self,hasFound):
		self.hasFound=hasFound     
		

	def getFaceSize(self):
		return self.faceSize       

	def setFaceSize(self,faceSize):
		self.faceSize=faceSize     
		

	def getFaceConsecutiveFrame(self):
		return self.faceConsecutiveFrame

	def setFaceConsecutiveFrame(self,faceConsecutiveFrame):
		self.faceConsecutiveFrame=faceConsecutiveFrame


	def getFaceDurationFrame(self):
		return self.faceDurationFrame

	def setFaceDurationFrame(self,faceDurationFrame):
		self.faceDurationFrame=faceDurationFrame

