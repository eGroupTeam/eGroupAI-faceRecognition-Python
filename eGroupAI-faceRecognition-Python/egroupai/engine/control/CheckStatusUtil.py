import json
import os.path as osp
from enum import Enum
from time import time, sleep

from egroup.util.AttributeCheck import AttributeCheck
from egroup.util.LoggingUtil import LOGGER
from egroup.util.TxtUtil import TxtUtil, Charsets
from egroupai.engine.entity.ModelAppendInfo import ModelAppendInfo
from egroupai.engine.entity.ModelAppendResult import ModelAppendResult
from egroupai.engine.entity.ModelInsertInfo import ModelInsertInfo
from egroupai.engine.entity.ModelInsertResult import ModelInsertResult
from egroupai.engine.entity.ModelSwitchResult import ModelSwitchResult
from egroupai.engine.entity.RecognizeFace import RECOGNIZEMODE_
from egroupai.engine.entity.TrainInfo import TrainInfo
from egroupai.engine.entity.TrainResult import TrainResult
from egroupai.engine.status.entity.StartupStatus import StartupStatus


class Check(Enum):
    CHECK0 = "初始化驗證"
    CHECK1 = "金鑰驗證"
    CHECK2 = "辨識引擎啟動參數"
    CHECK3 = "辨識引擎運作程式"
    CHECK4 = "硬體驗證"
    CHECK5 = "儲存空間"
    CHECK6 = "影像來源"
    CHECK7 = "辨識引擎演算法程式"
    CHECK8 = "模型檔案"
    CHECK9 = "模型檔案載入"
    CHECK10 = "輸出結果資料夾"


class CheckStatusUtil:

    @staticmethod
    def recognizeServerStartup4(enginePath: str, modelPath: str, startupStatusPath: str, waitTimeMs: int,
                                recognizeMode_: RECOGNIZEMODE_) -> list:
        # init func
        attributeCheck = AttributeCheck()
        # init variable
        startupStatusList = list()
        startupStatus = StartupStatus()
        checkFlag = True

        if attributeCheck.stringsNotNull(enginePath, modelPath):
            # init variable
            licenseKeyPath = f"{enginePath}\\license.key"
            if recognizeMode_.value == RECOGNIZEMODE_.LIVENESS:
                recognizeExePath = f"{enginePath}\\LivenessDetectionServer.exe"
            else:
                recognizeExePath = f"{enginePath}\\RecognizeFace.exe"
            trainExePath = f"{enginePath}\\TrainFace.exe"
            modelAppendExePath = f"{enginePath}\\ModelAppend.exe"
            if not (osp.exists(enginePath) and osp.exists(modelPath) and osp.exists(licenseKeyPath) and osp.exists(
                    recognizeExePath) and osp.exists(trainExePath) and osp.exists(modelAppendExePath)):
                checkFlag = False
        else:
            checkFlag = False
        startupStatus.setCheckId(0)
        startupStatus.setCheckFlag(checkFlag)
        startupStatus.setCheckName(Check.CHECK0)
        startupStatusList.append(startupStatus)

        if checkFlag and attributeCheck.stringsNotNull(startupStatusPath):
            # init func
            txtUtil = TxtUtil()
            # init variable
            startTime = time()
            endTime2 = None
            checkCount = 0
            try:
                while True:
                    endTime2 = time()
                    if (endTime2 - startTime) * 1000 > waitTimeMs or (
                            osp.exists(startupStatusPath) and osp.getsize(startupStatusPath) > 0):
                        break
                    sleep(0.2)
            except InterruptedError as e:
                LOGGER.error(json.dumps(e))

            if osp.exists(startupStatusPath) and len(startupStatusPath) > 0:
                startupStatusLineList = txtUtil.read_lineList(startupStatusPath, Charsets.BIG5)
                if attributeCheck.listNotEmpty(startupStatusLineList):
                    for startupStatusLine in startupStatusLineList:
                        if checkFlag:
                            LOGGER.info(f"checkCount={checkCount},startupStatusLine={startupStatusLine}")
                            # init variable
                            startupStatus = StartupStatus()
                            startupStatusArray = startupStatusLine.split("\t")
                            if len(startupStatusArray) == 3:
                                if checkCount == 0:
                                    if startupStatusArray[0] == "Check0":
                                        if startupStatusArray[1] == "Pass":
                                            checkFlag = True
                                            checkCount += 1
                                        else:
                                            checkFlag = False
                                        startupStatus.setCheckId(1)
                                        startupStatus.setCheckName(Check.CHECK1)
                                        startupStatus.setCheckFlag(checkFlag)
                                        startupStatusList.append(startupStatus)
                                elif checkCount == 1:
                                    if startupStatusArray[0] == "Check1":
                                        if startupStatusArray[1] == "Pass":
                                            checkFlag = True
                                            checkCount += 1
                                        else:
                                            checkFlag = False
                                        startupStatus.setCheckId(2)
                                        startupStatus.setCheckName(Check.CHECK2)
                                        startupStatus.setCheckFlag(checkFlag)
                                        startupStatusList.append(startupStatus)
                                elif checkCount == 2:
                                    if startupStatusArray[0] == "Check2":
                                        if startupStatusArray[1] == "Pass":
                                            checkFlag = True
                                            checkCount += 1
                                        else:
                                            checkFlag = False
                                        startupStatus.setCheckId(3)
                                        startupStatus.setCheckName(Check.CHECK3)
                                        startupStatus.setCheckFlag(checkFlag)
                                        startupStatusList.append(startupStatus)
                                elif checkCount == 3:
                                    if startupStatusArray[0] == "Check3":
                                        if startupStatusArray[1] == "Pass":
                                            checkFlag = True
                                            checkCount += 1
                                        else:
                                            checkFlag = False
                                        startupStatus.setCheckId(4)
                                        startupStatus.setCheckName(Check.CHECK4)
                                        startupStatus.setCheckFlag(checkFlag)
                                        startupStatusList.append(startupStatus)
                                elif checkCount == 4:
                                    if startupStatusArray[0] == "Check4":
                                        if startupStatusArray[1] == "Pass":
                                            checkFlag = True
                                            checkCount += 1
                                        else:
                                            checkFlag = False
                                        startupStatus.setCheckId(5)
                                        startupStatus.setCheckName(Check.CHECK5)
                                        startupStatus.setCheckFlag(checkFlag)
                                        startupStatusList.append(startupStatus)
                                elif checkCount == 5:
                                    if startupStatusArray[0] == "Check5":
                                        if startupStatusArray[1] == "Pass":
                                            checkFlag = True
                                            checkCount += 1
                                        else:
                                            checkFlag = False
                                        startupStatus.setCheckId(6)
                                        startupStatus.setCheckName(Check.CHECK6)
                                        startupStatus.setCheckFlag(checkFlag)
                                        startupStatusList.append(startupStatus)
                                elif checkCount == 6:
                                    if startupStatusArray[0] == "Check6":
                                        if startupStatusArray[1] == "Pass":
                                            checkFlag = True
                                            checkCount += 1
                                        else:
                                            checkFlag = False
                                        startupStatus.setCheckId(7)
                                        startupStatus.setCheckName(Check.CHECK7)
                                        startupStatus.setCheckFlag(checkFlag)
                                        startupStatusList.append(startupStatus)
                                elif checkCount == 7:
                                    if startupStatusArray[0] == "Check7":
                                        if startupStatusArray[1] == "Pass":
                                            checkFlag = True
                                            checkCount += 1
                                        else:
                                            checkFlag = False
                                        startupStatus.setCheckId(8)
                                        startupStatus.setCheckName(Check.CHECK8)
                                        startupStatus.setCheckFlag(checkFlag)
                                        startupStatusList.append(startupStatus)
                                elif checkCount == 8:
                                    if startupStatusArray[0] == "Check8":
                                        if startupStatusArray[1] == "Pass":
                                            checkFlag = True
                                            checkCount += 1
                                        else:
                                            checkFlag = False
                                        startupStatus.setCheckId(9)
                                        startupStatus.setCheckName(Check.CHECK9)
                                        startupStatus.setCheckFlag(checkFlag)
                                        startupStatusList.append(startupStatus)
                        else:
                            break
        return startupStatusList

    def recognizeMainStartup4(self, enginePath: str, modelPath: str, outputFacePath: str, outputFramePath,
                              showTrainFacePath: str, trainFacePath: str, startupStatusPath: str, waitTimeMs: int):
        attributeCheck = AttributeCheck()
        startupStatusList = list()
        startupStatus = StartupStatus()
        checkFlag = True

        if attributeCheck.stringsNotNull(enginePath, modelPath, outputFacePath, outputFramePath, showTrainFacePath,
                                         trainFacePath):
            # init variable
            if not (osp.exists(enginePath) and osp.exists(modelPath) and osp.exists(outputFacePath) and osp.exists(
                    outputFramePath) and osp.exists(showTrainFacePath) and osp.exists(trainFacePath)):
                checkFlag = False
        else:
            checkFlag = False

        startupStatus.setCheckId(0)
        startupStatus.setCheckFlag(Check.CHECK0)
        startupStatusList.append(startupStatus)

        if checkFlag:
            if attributeCheck.stringsNotNull(startupStatusPath):
                # init func
                txtUtil = TxtUtil()
                # init variable
                checkCount = 0

                try:
                    while True:
                        if osp.exists(startupStatusPath) and osp.getsize(startupStatusPath) > 0:
                            break
                        sleep(0.2)
                except InterruptedError as e:
                    LOGGER.error(json.dumps(e))

                if osp.exists(startupStatusPath) and osp.getsize(startupStatusPath) > 0:
                    startupStatusLineList = txtUtil.read_lineList(startupStatusPath, Charsets.BIG5)
                    if attributeCheck.listNotEmpty(startupStatusLineList):
                        for startupStatusLine in startupStatusLineList:
                            if checkFlag:
                                # init variable
                                startupStatus = StartupStatus()
                                startupStatusArray = startupStatusLine.split("\t")
                                if len(startupStatusArray) == 3:
                                    if checkCount == 0:
                                        if startupStatusArray[0] == "Check0":
                                            if startupStatusArray[1] == "Pass":
                                                checkFlag = True
                                                checkCount += 1
                                            else:
                                                checkFlag = False
                                            startupStatus.setCheckId(1)
                                            startupStatus.setCheckName(Check.CHECK1)
                                            startupStatus.setCheckFlag(checkFlag)
                                            startupStatusList.append(startupStatus)
                                    elif checkCount == 1:
                                        if startupStatusArray[0] == "Check1":
                                            if startupStatusArray[1] == "Pass":
                                                checkFlag = True
                                                checkCount += 1
                                            else:
                                                checkFlag = False
                                            startupStatus.setCheckId(2)
                                            startupStatus.setCheckName(Check.CHECK2)
                                            startupStatus.setCheckFlag(checkFlag)
                                            startupStatusList.append(startupStatus)
                                    elif checkCount == 2:
                                        if startupStatusArray[0] == "Check2":
                                            if startupStatusArray[1] == "Pass":
                                                checkFlag = True
                                                checkCount += 1
                                            else:
                                                checkFlag = False
                                            startupStatus.setCheckId(3)
                                            startupStatus.setCheckName(Check.CHECK3)
                                            startupStatus.setCheckFlag(checkFlag)
                                            startupStatusList.append(startupStatus)
                                    elif checkCount == 3:
                                        if startupStatusArray[0] == "Check3":
                                            if startupStatusArray[1] == "Pass":
                                                checkFlag = True
                                                checkCount += 1
                                            else:
                                                checkFlag = False
                                            startupStatus.setCheckId(4)
                                            startupStatus.setCheckName(Check.CHECK4)
                                            startupStatus.setCheckFlag(checkFlag)
                                            startupStatusList.append(startupStatus)
                                    elif checkCount == 4:
                                        if startupStatusArray[0] == "Check4":
                                            if startupStatusArray[1] == "Pass":
                                                checkFlag = True
                                                checkCount += 1
                                            else:
                                                checkFlag = False
                                            startupStatus.setCheckId(5)
                                            startupStatus.setCheckName(Check.CHECK5)
                                            startupStatus.setCheckFlag(checkFlag)
                                            startupStatusList.append(startupStatus)
                                    elif checkCount == 5:
                                        if startupStatusArray[0] == "Check5":
                                            if startupStatusArray[1] == "Pass":
                                                checkFlag = True
                                                checkCount += 1
                                            else:
                                                checkFlag = False
                                            startupStatus.setCheckId(6)
                                            startupStatus.setCheckName(Check.CHECK6)
                                            startupStatus.setCheckFlag(checkFlag)
                                            startupStatusList.append(startupStatus)
                                    elif checkCount == 6:
                                        if startupStatusArray[0] == "Check6":
                                            if startupStatusArray[1] == "Pass":
                                                checkFlag = True
                                                checkCount += 1
                                            else:
                                                checkFlag = False
                                            startupStatus.setCheckId(7)
                                            startupStatus.setCheckName(Check.CHECK7)
                                            startupStatus.setCheckFlag(checkFlag)
                                            startupStatusList.append(startupStatus)
                                    elif checkCount == 7:
                                        if startupStatusArray[0] == "Check7":
                                            if startupStatusArray[1] == "Pass":
                                                checkFlag = True
                                                checkCount += 1
                                            else:
                                                checkFlag = False
                                            startupStatus.setCheckId(8)
                                            startupStatus.setCheckName(Check.CHECK8)
                                            startupStatus.setCheckFlag(checkFlag)
                                            startupStatusList.append(startupStatus)
                                    elif checkCount == 8:
                                        if startupStatusArray[0] == "Check8":
                                            if startupStatusArray[1] == "Pass":
                                                checkFlag = True
                                                checkCount += 1
                                            else:
                                                checkFlag = False
                                            startupStatus.setCheckId(9)
                                            startupStatus.setCheckName(Check.CHECK9)
                                            startupStatus.setCheckFlag(checkFlag)
                                            startupStatusList.append(startupStatus)
                            else:
                                break
        return startupStatusList

    def trainFace(self, trainResultPath: str) -> TrainResult:
        attributeCheck = AttributeCheck()
        trainResult = TrainResult()
        if attributeCheck.stringsNotNull(trainResultPath):
            # init func
            txtUtil = TxtUtil()
            # init variable
            try:
                while True:
                    if osp.exists(trainResultPath) and osp.getsize(trainResultPath) > 0:
                        break
                    sleep(0.25)
                    LOGGER.info("訓練進行中，請稍等......")
            except InterruptedError as e:
                LOGGER.error(json.dumps(e))

            trainResultLineList = txtUtil.read_lineList(trainResultPath, Charsets.BIG5)
            if attributeCheck.listNotEmpty(trainResultLineList):
                # init variable
                trainInfoList = list()
                for trainResultLine in trainResultLineList:
                    trainArray = trainResultLine.split("\t")
                    trainInfo = TrainInfo()
                    if len(trainArray) == 9:
                        if trainArray[1] == "Pass":
                            trainResult.getPassFacePathList().append(trainArray[2])
                        else:
                            trainResult.getFailFacePathList().append(trainArray[2])
                        trainInfo.setFacePath(trainArray[2])
                        trainInfo.setStatus(trainArray[1])
                        trainInfo.setTime(trainArray[0])
                        trainInfo.setPersonId(trainArray[3])
                        trainInfo.setFaceQuality("pass" in trainArray[4].lower())
                        trainInfo.setFaceQualityBlurness("pass" in trainArray[5].lower())
                        trainInfo.setIsFaceQualityLowLuminance("pass" in trainArray[6].lower())
                        trainInfo.setIsFaceQualityHighLuminance("pass" in trainArray[7].lower())
                        trainInfo.setIsFaceQualityHeadpose("pass" in trainArray[8].lower())
                        trainInfoList.append(trainInfo)
                    elif len(trainArray) == 5:
                        if trainArray[1] == "Fail":
                            trainResult.getFailFacePathList().append(trainArray[2])
                        trainInfo.setFacePath(trainArray[3])
                        trainInfo.setStatus(trainArray[2])
                        trainInfo.setTime(trainArray[0])
                        trainInfo.setPersonId(trainArray[4])
                        trainInfoList.append(trainInfo)
                    elif len(trainArray) == 2:
                        if trainArray[1] == "faces were trained in the list file":
                            trainResult.setFaceSize(int(trainArray[0].replace(":", "")))
                        elif trainArray[1] == "list file size":
                            trainResult.setFileSize(int(trainArray[0].replace(":", "")))
                    elif len(trainArray) == 1:
                        if trainArray[0].startswith("Processing Time"):
                            trainResult.setProcessingTime(
                                trainArray[0].replace("Processing Time: ", "").replace(" sec.", ""))
                        else:
                            trainResult.setAvgPprocessingSpped(
                                trainArray[0].replace("AVG processing speed = ", "").replace(" image/sec", ""))
                trainResult.setTrainInfoList(trainInfoList)
            else:
                trainResult.setTrainResultFileExist(False)
        return trainResult

    def modelAppend(self, modelAppendPath: str, waitTimeMs: int) -> ModelAppendResult:
        # init func
        attributeCheck = AttributeCheck()
        # init variable
        modelAppendResult = None

        if attributeCheck.stringsNotNull(modelAppendPath):
            # init func
            txtUtil = TxtUtil()
            # init variable
            waitCount = 0

            try:
                while True:
                    if (osp.exists(modelAppendPath) and osp.getsize(modelAppendPath) > 0) or waitCount == 5:
                        break
                    waitCount += 1
                    sleep(waitTimeMs / 5 / 1000)
            except InterruptedError as e:
                LOGGER.error(json.dumps(e))

            # Get the model append log
            if osp.exists(modelAppendPath) and osp.getsize(modelAppendPath) > 0:
                modelAppendResult = ModelAppendResult()
                modelAppendLineList = txtUtil.read_lineList(modelAppendPath, Charsets.UTF8)
                if attributeCheck.listNotEmpty(modelAppendLineList):
                    # init variable
                    modelAppendInfoList = list()
                    modelAppendInfo = ModelAppendInfo()
                    for modelAppendLine in modelAppendLineList:
                        # init variable
                        modelAppendArray = modelAppendLine.split("\t")
                        if len(modelAppendArray) == 5:
                            if "DBSize" in modelAppendArray[2]:
                                modelAppendInfo.setDBSizeCheckStatus(modelAppendArray[1])
                                modelAppendInfo.setDBSize(int(modelAppendArray[2][7: len(modelAppendArray[2])].strip()))
                                modelAppendInfo.DBFaceDBPath(modelAppendArray[3])
                                modelAppendInfo.setSucess(True)
                                modelAppendInfoList.append(modelAppendInfo)
                                modelAppendInfo = ModelAppendInfo()
                        elif len(modelAppendArray) == 4:
                            if modelAppendArray[1] == "Fail":
                                modelAppendInfo.setSucess(False)
                                modelAppendInfo.setErrorMessage(modelAppendArray[2])
                                modelAppendInfoList.append(modelAppendInfo)
                                modelAppendInfo = ModelAppendInfo()
                            if modelAppendArray[2] == "Parsingfile":
                                modelAppendResult.setModelListPath(modelAppendArray[3].replace("file: ", ""))
                                modelAppendResult.setModelListCheckStatus(modelAppendArray[1])
                            elif modelAppendArray[2] == "WorkingFolder":
                                modelAppendInfo.setWorkingFolderCheckStatus(modelAppendArray[1])
                                modelAppendInfo.setWorkingFolderSize(float(
                                    modelAppendArray[3].replace("Not enough space to working folder (", "")[
                                    1: modelAppendArray[3].find("GB")]))
                                modelAppendInfo.setWorkingFolderStatus(modelAppendArray[3][
                                                                       modelAppendArray[3].find("GB") + 3:
                                                                       modelAppendArray[3].rfind("(")].strip())
                            elif modelAppendArray[2] == "OutputFaceDB":
                                modelAppendInfo.setOutputFaceDBCheckStatus(modelAppendArray[1])
                                modelAppendInfo.setOutputFaceDBSize(float(
                                    modelAppendArray[3].replace("Not enough space to Output Binary file (", "")[
                                    1: modelAppendArray[3].find("GB")]))
                                modelAppendInfo.setOutputFaceDBStatus(modelAppendArray[3][
                                                                      modelAppendArray[3].find("GB") + 3:
                                                                      modelAppendArray[3].rfind("(")].strip())
                        elif len(modelAppendArray) == 1:
                            if modelAppendArray[0].startswith("Total faces: "):
                                modelAppendResult.setTotalFaceCount(int(modelAppendArray[0][
                                                                        modelAppendArray[0].find("Total faces: ") + 12:
                                                                        modelAppendArray[0].find(
                                                                            "in the appended new model")].strip()))
                            else:
                                modelAppendResult.setAppendPassCount(int(modelAppendArray[0][
                                                                         0: modelAppendArray[0].find(
                                                                             "of models appended pass")].strip()))
                                modelAppendResult.setAppendFailCount(int(modelAppendArray[0][
                                                                         modelAppendArray[0].find("/") + 1:
                                                                         modelAppendArray[0].find(
                                                                             "of models appended failed")].strip()))
                    # set the model append result info
                    modelAppendResult.setModelAppendInfoList(modelAppendInfoList)
        return modelAppendResult

    def modelSwitch(self, modelSwitchStatusPath: str) -> ModelSwitchResult:
        attributeCheck = AttributeCheck()
        modelSwitchResult = None
        if attributeCheck.stringsNotNull(modelSwitchStatusPath):
            # init variable
            txtUtil = TxtUtil()
            # init variable
            flag = True
            waitCount = 0
            try:
                while True:
                    if (osp.exists(modelSwitchStatusPath) and osp.getsize(
                            modelSwitchStatusPath) > 0) or waitCount == 10:
                        break
                    waitCount += 1
                    sleep(0.2)
            except InterruptedError as e:
                LOGGER.error(json.dumps(e))

            if osp.exists(modelSwitchStatusPath) and osp.getsize(modelSwitchStatusPath) > 0:
                modelSwitchResult = ModelSwitchResult()
                modelSwitchLineList = txtUtil.read_lineList(modelSwitchStatusPath, Charsets.UTF8)
                faceDBPath = ""
                if attributeCheck.listNotEmpty(modelSwitchLineList):
                    for modelSwitchLine in modelSwitchLineList:
                        modelSwitchArray = modelSwitchLine.split("\t")
                        if len(modelSwitchArray) > 1:
                            if modelSwitchArray[1] == "Fail":
                                faceDBPath = modelSwitchArray[3].replace("Reload FaceDB file ", "")
                                modelSwitchResult.setFaceDB(faceDBPath[faceDBPath.rfind("\\") + 1: faceDBPath.length()])
                                flag = False
                            elif modelSwitchArray[1].equals("Pass") and modelSwitchArray.length == 4:
                                faceDBPath = modelSwitchArray[3].replace("Reload FaceDB file ", "")
                                modelSwitchResult.setFaceDB(faceDBPath[faceDBPath.rfind("\\") + 1: len(faceDBPath)])
                            elif modelSwitchArray[1] == "Report":
                                if modelSwitchArray[3].startswith("Overall reload:"):
                                    modelSwitchResult.setFaceReload(modelSwitchArray[3])
                                else:
                                    modelSwitchResult.setReloadTime(modelSwitchArray[3])
                else:
                    flag = False
                modelSwitchResult.setSuccess(flag)
        return modelSwitchResult

    def modelInsert(self, modelInsertStatusPath: str, waitTimeMs: int) -> ModelInsertResult:
        # init func
        attributeCheck = AttributeCheck()
        # init variable
        modelInsertResult = None
        if attributeCheck.stringsNotNull(modelInsertStatusPath):
            # init variable
            txtUtil = TxtUtil()
            waitCount = 0
            try:
                while True:
                    if (osp.exists(modelInsertStatusPath) and osp.getsize(
                            modelInsertStatusPath) > 0) or waitCount == 10:
                        break
                    waitCount += 1
                    sleep(waitTimeMs / 5 / 1000)
            except InterruptedError as e:
                LOGGER.error(json.dumps(e))

            if osp.exists(modelInsertStatusPath) and osp.getsize(modelInsertStatusPath) > 0:
                modelInsertResult = ModelInsertResult()
                modelInsertLineList = txtUtil.read_lineList(modelInsertStatusPath, Charsets.UTF8)
                if attributeCheck.listNotEmpty(modelInsertLineList):
                    # init variable
                    modelInsertInfoList = list()
                    faceAndPeople = list()
                    face = None
                    people = None
                    currentDBFaceCount = None
                    currentDBPeopleCount = None

                    for modelInsertLine in modelInsertLineList:
                        # init variable
                        modelInsertInfo = ModelInsertInfo()
                        modelInsertArray = modelInsertLine.split("\t")
                        if len(modelInsertArray) == 3:
                            if modelInsertArray[1] == "Pass":
                                modelInsertInfoList.append(modelInsertInfo)
                                modelInsertResult.setSuccess(True)
                        elif len(modelInsertArray) == 5:
                            faceAndPeople = modelInsertArray[3].replace("Overall insert:", "").replace("faces/people",
                                                                                                       "").strip().split("/")
                            currentfaceAndPeople = modelInsertArray[4].replace("CurrentDBFaceCout=", "").replace(
                                "CurrentDBPeopleCount=", "").strip().split(" ")
                            face = int(faceAndPeople[0])
                            people = int(faceAndPeople[1])
                            currentDBFaceCout = int(currentfaceAndPeople[0])
                            currentDBPeopleCount = int(currentfaceAndPeople[1])

                            modelInsertInfo.setInsertFacesCount(face)
                            modelInsertInfo.setInsertPeopleCount(people)
                            modelInsertInfo.setCurrDBFaceCout(currentDBFaceCout)
                            modelInsertInfo.setCurrDBPeopleCount(currentDBPeopleCount)
                            modelInsertInfoList.append(modelInsertInfo)
                            modelInsertResult.setSuccess(True)
                        elif len(modelInsertArray) == 4:
                            if modelInsertArray[3].startswith("Overall insert time: "):
                                modelInsertInfo.setInsertProcessTime(modelInsertArray[3][
                                                                     modelInsertArray[3].find("Overall insert time: "):
                                                                     modelInsertArray[3].find(" sec.")].strip())
                            modelInsertInfoList.append(modelInsertInfo)
                    modelInsertResult.setModelInsertInfoList(modelInsertInfoList)
        return modelInsertResult
