from .AttributeCheck import *
import os
import logging

logging.basicConfig(filename='log.txt',level=logging.ERROR,format="%(asctime)s-%(levelname)s-%(message)s")


class Charsets:
	def __init__(self,value: str) -> None:
		self.BIG5="Big5"
		self.UTF8="utf-8"
		self.ISO_8859_1="iso_8859_1"
		self.value=value

	def getValue(self) -> str:
		return self.value

class TxtUtil:
	
	def __init__(self) -> None:
		pass

	def create(filePath: str,dataList: any,charsets: Charsets):
		if AttributeCheck.listNotEmpty(dataList) and AttributeCheck.stringsNotNull(filePath):
			if not os.path.exists(os.path.dirname(filePath)):
				os.makedirs(os.path.dirname(filePath))

				try:
					with open(filePath,'w',encoding=charsets.getValue()) as fp:
						if isinstance(dataList,list):
							fp.writelines(dataList)
						else:
							fp.write(dataList)

					if os.path.exists(filePath):
						return True
						
				except:
					logging.error("IO Exception",exc_info=True)
					return False

		return False

	def createSingalForRecognition(filePath: str, dataList: list)->bool:
		if AttributeCheck.listNotEmpty(dataList) and AttributeCheck.stringsNotNull(filePath):
			if not os.path.exists(os.path.dirname(filePath)):
				os.makedirs(os.path.dirname(filePath))

				try:
					with open(filePath,'w',encoding='utf-8') as fp:
						if isinstance(dataList,list):
							fp.writelines(dataList)
						else:
							fp.write(dataList)

					if os.path.exists(filePath):
						return True
						
				except:
					logging.error("IO Exception",exc_info=True)
					return False

	def read_content(txtPath: str):
		content=[]
		if AttributeCheck.stringsNotNull(txtPath):
			if os.path.isfile(txtPath) and os.path.exists(txtPath):
				lines=[line for line in open(txtPath,encoding='utf-8')]
				for l in lines:
					if len(l)>0:
						content.append(l)
		
		return "\n".join(content)

	
	def read_lineList(txtPath: str,charset):
		content=[]
		if AttributeCheck.stringsNotNull(txtPath):
			if os.path.isfile(txtPath) and os.path.exists(txtPath):
				lines=[line for line in open(txtPath,encoding=charset.getValue())]
				for l in lines:
					content.append(l)
		
		return content