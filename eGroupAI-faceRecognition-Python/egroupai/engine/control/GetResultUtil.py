from time import sleep
import os
import os.path as osp

import json

from egroup.util.AttributeCheck import AttributeCheck
from egroup.util.CopyUtil import CopyUtil
from egroup.util.LoggingUtil import LOGGER
from egroup.util.TxtUtil import TxtUtil


class GetResultUtil:
    def allResult(self, jsonFolderPath: str, jsonName: str, startIndex: int, isDynamicJson: bool, waiteJsonMs: int):
        # init func
        copyUtil = CopyUtil()
        attributeCheck = AttributeCheck()
        # init variable
        faceList = list
        # Get retrieve result
        sourceJsonPath = jsonFolderPath + "/" + jsonName + ".json"
        jsonFileName = jsonFolderPath + "/" + jsonName + "_copy.json"
        try:
            sleep(waiteJsonMs / 1000)
        except InterruptedError as e:
            print(e)
        #       // TODO Auto-generated catch block
        #       e.printStackTrace()
        if osp.exists(sourceJsonPath) and osp.getsize(sourceJsonPath) > 0:
            # init func
            txtUtil = TxtUtil()
            # init variable
            jsonContent = txtUtil.read_content(jsonFileName)
            try:
                copyUtil.copyFile(sourceJsonPath, jsonFileName)
            except Exception as e:
                LOGGER.error(json.dumps(e))
            # If has data
            if attributeCheck.stringsNotNull(jsonContent):
                # Get last one object
                if isDynamicJson:
                    endIndex = jsonContent.rfind("}\n\t,")
                    if endIndex == -1:
                        endIndex = jsonContent.rfind("}\n]")
                    # Reorganization json
                    if endIndex != -1 and startIndex != endIndex and startIndex < endIndex:
                        if startIndex > 0:
                            json_ = "[" + str(jsonContent)[startIndex + 2: endIndex] + "}]"
                        else:
                            json_ = str(jsonContent)[startIndex: endIndex] + "}]"
                        if attributeCheck.stringsNotNull(json_):
                            # TODO: import jsondata
                            # faceList = gson.fromJson(json, faceListType)
                            faceList = json.loads(json_)
                            faceList[-1].setEndIndex(endIndex + 2)
                else:
                    if attributeCheck.stringsNotNull(str(jsonContent)):
                        faceList = json.loads(str(jsonContent))
        return faceList

    def allResult(self, jsonFolderPath: str, jsonName: str, startIndex: int, isDynamicJson: bool, waiteJsonMs: int):
        # init func
        copyUtil = CopyUtil()
        attributeCheck = AttributeCheck()
        # init variable
        faceList = list
        # Get retrieve result
        sourceJsonPath = jsonFolderPath + "/" + jsonName + ".json"
        jsonFileName = jsonFolderPath + "/" + jsonName + "_copy.json"
        try:
            sleep(waiteJsonMs / 1000)
        except InterruptedError as e:
            print(e)
        #       // TODO Auto-generated catch block
        #       e.printStackTrace()
        if osp.exists(sourceJsonPath) and osp.getsize(sourceJsonPath) > 0:
            # init func
            txtUtil = TxtUtil()
            # init variable
            jsonContent = txtUtil.read_content(jsonFileName)
            try:
                copyUtil.copyFile(sourceJsonPath, jsonFileName)
            except Exception as e:
                LOGGER.error(json.dumps(e))
            # If has data
            if attributeCheck.stringsNotNull(jsonContent):
                # Get last one object
                if isDynamicJson:
                    endIndex = jsonContent.rfind("}\n\t,")
                    if endIndex == -1:
                        endIndex = jsonContent.rfind("}\n]")
                    # Reorganization json
                    if endIndex != -1 and startIndex != endIndex and startIndex < endIndex:
                        if startIndex > 0:
                            json_ = "[" + str(jsonContent)[startIndex + 2: endIndex] + "}]"
                        else:
                            json_ = str(jsonContent)[startIndex: endIndex] + "}]"
                        if attributeCheck.stringsNotNull(json_):
                            # TODO: import jsondata
                            # faceList = gson.fromJson(json, faceListType)
                            faceList = json.loads(json_)
                            faceList[-1].setEndIndex(endIndex + 2)
                else:
                    if attributeCheck.stringsNotNull(str(jsonContent)):
                        faceList = json.loads(str(jsonContent))
        return faceList

    def allResult(self, jsonFolderPath: str, jsonName: str, startIndex: int, isDynamicJson: bool, waiteJsonMs: int):
        # init func
        copyUtil = CopyUtil()
        attributeCheck = AttributeCheck()
        # init variable
        faceList = list()
        # Get retrieve result
        sourceJsonPath = jsonFolderPath + "/" + jsonName + ".json"
        jsonFileName = jsonFolderPath + "/" + jsonName + "_copy.json"
        try:
            sleep(waiteJsonMs / 1000)
        except InterruptedError as e:
            print(e)
        #       // TODO Auto-generated catch block
        #       e.printStackTrace()
        if osp.exists(sourceJsonPath) and osp.getsize(sourceJsonPath) > 0:
            # init func
            txtUtil = TxtUtil()
            # init variable
            jsonContent = txtUtil.read_content(jsonFileName)
            try:
                copyUtil.copyFile(sourceJsonPath, jsonFileName)
            except Exception as e:
                LOGGER.error(json.dumps(e))
            # If has data
            if attributeCheck.stringsNotNull(jsonContent):
                # Get last one object
                if isDynamicJson:
                    endIndex = jsonContent.rfind("}\n\t,")
                    if endIndex == -1:
                        endIndex = jsonContent.rfind("}\n]")
                    # Reorganization json
                    if endIndex != -1 and startIndex != endIndex and startIndex < endIndex:
                        if startIndex > 0:
                            json_ = "[" + str(jsonContent)[startIndex + 2: endIndex] + "}]"
                        else:
                            json_ = str(jsonContent)[startIndex: endIndex] + "}]"
                        if attributeCheck.stringsNotNull(json_):
                            # TODO: import jsondata
                            # faceList = gson.fromJson(json, faceListType)
                            faceList = json.loads(json_)
                            faceList[-1].setEndIndex(endIndex + 2)
                else:
                    if attributeCheck.stringsNotNull(str(jsonContent)):
                        faceList = json.loads(str(jsonContent))
        return faceList

    def cacheResult(self, jsonFolderPath: str, jsonName: str):
        # init func
        attributeCheck = AttributeCheck()
        # init variable
        faceList = None

        if attributeCheck.stringsNotNull(jsonFolderPath, jsonName):
            # init func
            copyUtil = CopyUtil()

            # init variable

            # get retrieve result
            sourceJsonPath = jsonFolderPath + "\\" + jsonName + ".json"
            jsonFileName = jsonFolderPath + "\\" + jsonName + "_copy.json"

            if osp.exists(sourceJsonPath) and osp.getsize(sourceJsonPath) != osp.getsize(jsonFileName):
                # init func
                txtUtil = TxtUtil()
                # init variable
                try:
                    copyUtil.copyFile(sourceJsonPath, jsonFileName)
                except Exception as e:
                    LOGGER.error(json.dumps(e))
                jsonContent = txtUtil.read_content(jsonFileName)

                # If has data
                if attributeCheck.stringsNotNull(jsonContent):
                    # Get last one object
                    endIndex = jsonContent.rfind("}\n]")
                    if endIndex == -1:
                        endIndex = jsonContent.rfind("}\n\t,")

                    if endIndex > 0:
                        json_ = jsonContent[0, endIndex] + "}]"
                        faceList = json.loads(json_)
        return faceList

    def serverPhotoResult(self, jsonPath: str, jsonName: str, deleteJson: bool):
        # init func
        # init variable
        faceList = list()
        # Get retrieve result
        sourceJson = jsonPath + "\\" + jsonName + ".json"
        if osp.exists(sourceJson):
            # init func
            txtUtil = TxtUtil()
            attributeCheck = AttributeCheck()
            # init variable
            jsonFileName = jsonPath + "\\" + jsonName + ".json"
            jsonContent = txtUtil.read_content(jsonFileName)

            if attributeCheck.stringsNotNull(jsonContent):
                faceList = json.loads(jsonContent)

                if deleteJson:
                    try:
                        # TODO: recheck
                        os.remove(sourceJson)
                    except Exception as e:
                        LOGGER.error(json.dumps(e))

        return faceList
