class ModelInsertInfo:

	def __init__(self) -> None:

		self.datetimeString = None
		self.insertModelStatus = None
		self.insertFacesCount = None
		self.insertPeopleCount = None
		self.CurrDBFaceCout = None
		self.CurrDBPeopleCount = None
		self.insertProcessTime = None

	def getDatetimeString(self):
		return self.datetimeString

	def setDatetimeString(self,datetimeString):
		self.datetimeString=datetimeString     
		

	def getInsertModelStatus(self):
		return self.insertModelStatus

	def setInsertModelStatus(self,insertModelStatus):
		self.insertModelStatus=insertModelStatus     
		

	def getInsertFacesCount(self):
		return self.insertFacesCount

	def setInsertFacesCount(self,insertFacesCount):
		self.insertFacesCount=insertFacesCount


	def getInsertPeopleCount(self):
		return self.insertPeopleCount

	def setInsertPeopleCount(self,insertPeopleCount):
		self.insertPeopleCount=insertPeopleCount


	def getCurrDBFaceCout(self):
		return self.CurrDBFaceCout

	def setCurrDBFaceCout(self,CurrDBFaceCout):
		self.CurrDBFaceCout=CurrDBFaceCout


	def getCurrDBPeopleCount(self):
		return self.CurrDBPeopleCount

	def setCurrDBPeopleCount(self,CurrDBPeopleCount):
		self.CurrDBPeopleCount=CurrDBPeopleCount


	def getInsertProcessTime(self):
		return self.insertProcessTime

	def setInsertProcessTime(self,insertProcessTime):
		self.insertProcessTime=insertProcessTime

