

class FileUtil:
    def __init__(self,originalName: str) -> None:
        self.originalName=originalName
        try:
            self.fileType=originalName.split(".")[-1].lower()
        except:
            self.fileType=""
        self.fileName=originalName.replace(self.fileType,"")
        self.lowerCaseName=self.fileName+"."+self.fileType
    
    def getOriginalName(self):
        return self.originalName

    def setOriginalName(self,originalName: str):
        self.originalName=originalName
        try:
            self.fileType=originalName.split(".")[-1].lower()
        except:
            self.fileType=""
        self.fileName=originalName.replace(self.fileType,"")
        self.lowerCaseName=self.fileName+"."+self.fileType

    def getFileType(self) -> str:
        return self.fileType
    
    def setFileType(self, fileType: str) -> None:
        self.fileType=fileType

    def getFileName(self):
        return self.fileName
    
    def setFileName(self,fileName: str):
        self.fileName=fileName

    def getLowerCaseName(self):
        return self.lowerCaseName

    def setLowerCaseName(self,lowerCaseName):
        self.lowerCaseName=lowerCaseName
