import os
from enum import Enum
from time import sleep

from egroup.util.AttributeCheck import *
from egroup.util.LoggingUtil import LOGGER


class Charsets(Enum):
    BIG5 = "Big5"
    UTF8 = "utf-8"
    ISO_8859_1 = "iso_8859_1"


class TxtUtil:
    def create(self, filePath: str, dataList: any, charsets: Charsets):
        attributeCheck = AttributeCheck()
        if attributeCheck.listNotEmpty(dataList) and attributeCheck.stringsNotNull(filePath):
            if not os.path.exists(os.path.dirname(filePath)):
                os.makedirs(os.path.dirname(filePath))
            try:
                with open(filePath, 'w', encoding=charsets.value) as fp:
                    if isinstance(dataList, list):
                        fp.writelines([data + "\n" for data in dataList])
                    else:
                        fp.write(dataList)

                while not os.path.exists:
                    if os.path.exists(filePath):
                        return True
                    else:
                        sleep(0.01)
            except InterruptedError as err:
                LOGGER.error(json.dumps(err))
                return False
            except UnicodeEncodeError:
                LOGGER.error("IO Exception", exc_info=True)
                return False
        return False

    def createSingalForRecognition(self, filePath: str, dataList: list or str) -> bool:
        attributeCheck = AttributeCheck()
        if attributeCheck.listNotEmpty(dataList) and attributeCheck.stringsNotNull(filePath):
            if not os.path.exists(os.path.dirname(filePath)):
                os.makedirs(os.path.dirname(filePath))
                try:
                    with open(filePath, 'w', encoding='utf-8') as fp:
                        if isinstance(dataList, list):
                            fp.writelines(dataList)
                        else:
                            fp.write(dataList)
                    if os.path.exists(filePath):
                        return True
                except Exception as err:
                    LOGGER.error(json.dumps(err))
                    return False

    def read_content(self, txtPath: str):
        attributeCheck = AttributeCheck()
        contents = []
        if attributeCheck.stringsNotNull(txtPath):
            if os.path.isfile(txtPath) and os.path.exists(txtPath):
                with open(txtPath, encoding="utf-8") as f:
                    contents = [line.strip() for line in f.readlines() if line.strip()]
        return "\n".join(contents)

    def read_lineList(self, txtPath: str, charset: Charsets):
        attributeCheck = AttributeCheck()
        content = []
        if attributeCheck.stringsNotNull(txtPath):
            if os.path.isfile(txtPath) and os.path.exists(txtPath):
                with open(txtPath, encoding=charset.value) as f:
                    contents = [line.strip() for line in f.readlines()]
        return contents
