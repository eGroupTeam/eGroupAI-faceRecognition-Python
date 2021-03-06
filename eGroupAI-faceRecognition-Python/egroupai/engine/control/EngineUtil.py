import json
import os
import os.path as osp
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread

from egroup.util.AttributeCheck import AttributeCheck
from egroup.util.CmdUtil import CmdUtil
from egroup.util.LoggingUtil import LOGGER
from egroup.util.TxtUtil import TxtUtil, Charsets
from egroupai.engine.control.CheckStatusUtil import CheckStatusUtil
from egroupai.engine.entity.ModelAppend import ModelAppend
from egroupai.engine.entity.ModelAppendResult import ModelAppendResult
from egroupai.engine.entity.ModelCompare import ModelCompare
from egroupai.engine.entity.ModelInsert import ModelInsert
from egroupai.engine.entity.ModelInsertResult import ModelInsertResult
from egroupai.engine.entity.ModelSwitch import ModelSwitch
from egroupai.engine.entity.ModelSwitchResult import ModelSwitchResult
from egroupai.engine.entity.RecognizeFace import RecognizeFace, RECOGNIZEMODE_
from egroupai.engine.entity.TrainFace import TrainFace
from egroupai.engine.entity.TrainResult import TrainResult


class EngineUtil:
    def trainFace(self, trainFace: TrainFace, deleteTrainResultStatus: bool) -> TrainResult:
        # init func
        attributeCheck = AttributeCheck()
        checkStatusUtil = CheckStatusUtil()
        # init variable
        trainResult = TrainResult()
        trainFace.generateCli()
        if attributeCheck.listNotEmpty(trainFace.getCommandList()):
            cmdUtil = CmdUtil()
            trainResultLogPath = trainFace.getEnginePath() + "\\Status.TrainResultCPU.eGroup"
            if cmdUtil.cmdProcessBuilder(trainFace.getCommandList()):
                # init variable
                trainResult = checkStatusUtil.trainFace(trainResultLogPath)
                if deleteTrainResultStatus:
                    try:
                        os.remove(trainResultLogPath)
                    except IOError as e:
                        LOGGER.error(json.dumps(e))
            else:
                trainResult.setTrainCmdSuccess(False)
        else:
            trainResult.setTrainCmdSuccess(False)
        return trainResult

    def modelCompare(self, modelCompare: ModelCompare):
        flag = False
        # init func
        modelCompare.generateCli()
        if modelCompare.getCommandList() is not None:
            cmdUtil = CmdUtil()
            flag = cmdUtil.cmdProcessBuilder(modelCompare.getCommandList())
        return flag

    def stopRecognizeFace(self, recognizeFace: RecognizeFace, recognizeMode_: RECOGNIZEMODE_):
        flag = False
        # init func
        recognizeFace.getStopCli(recognizeMode_)
        if recognizeFace.getCommandList() is not None:
            cmdUtil = CmdUtil()
            flag = cmdUtil.cmdProcessBuilder(recognizeFace.getCommandList())
        return flag

    def recognizeFaceSingle(self, recognizeFace: RecognizeFace):
        flag = False
        # init func
        recognizeFace.generateCli()
        LOGGER.info(f"cli={recognizeFace.getCli()}")
        if recognizeFace.getCommandList() is not None:
            cmdUtil = CmdUtil()
            flag = cmdUtil.cmdProcessBuilder(recognizeFace.getCommandList())
        return flag

    def recognizeFace(self, recognizeFaceList: list, waitRecognizeDone: bool) -> dict:
        # init variable
        hashMap = dict()
        # Thread RECOGNITION_THREAD;
        RECOGNITION_THREAD = None

        if waitRecognizeDone:
            executorService = ThreadPoolExecutor(max_workers=len(recognizeFaceList))
            resultList = list()

            for idx, recognizeFace_fix in enumerate(recognizeFaceList):
                index = idx + 1

                def callFunc():
                    # init func
                    cmdUtil = CmdUtil()
                    recognizeFace_fix.generateCli()
                    if recognizeFace_fix.getCommandList() is not None:
                        flag = cmdUtil.cmdProcessBuilder(recognizeFace_fix.getCommandList())
                        _key = json.dumps(recognizeFace_fix)
                        if _key not in hashMap.keys():
                            hashMap[_key] = flag
                    return f"辨識執行續:{index}運作結束"

                future = executorService.submit(callFunc)
                resultList.append(future)
            # Monitor execute thread status
            executorService.shutdown()
            for fs in resultList:
                try:
                    while not fs.done():
                        LOGGER.debug(fs.result())
                except Exception as e:
                    LOGGER.error(json.dumps(e))
        else:
            for recognizeFace in recognizeFaceList:
                recognizeFace_fix = recognizeFace

                def runFunc():
                    # init func
                    cmdUtil = CmdUtil()
                    recognizeFace_fix.generateCli()
                    if recognizeFace_fix.getCommandList() is not None:
                        flag = cmdUtil.cmdProcessBuilder(recognizeFace_fix.getCommandList())
                        _key = json.dumps(recognizeFace_fix)
                        if _key not in hashMap.keys():
                            hashMap[_key] = flag

                RECOGNITION_THREAD = Thread(target=runFunc)
                RECOGNITION_THREAD.start()
        return hashMap

    def modelAppend(self, modelAppendVar: ModelAppend, deleteModelAppendStatus: bool,
                    waitTime: int) -> ModelAppendResult:
        # init func
        attributeCheck = AttributeCheck()
        # init variable
        modelAppendResult = ModelAppendResult()
        if modelAppendVar is not None and attributeCheck.stringsNotNull(modelAppendVar.getEnginePath(),
                                                                        modelAppendVar.getListPath(),
                                                                        modelAppendVar.getTrainedFaceDBPath()) and (
                attributeCheck.listNotEmpty(modelAppendVar.getFaceDBList()) or len(
            modelAppendVar.getFaceDBHashset()) > 0):
            # init func
            txtUtil = TxtUtil()
            checkStatusUtil = CheckStatusUtil()
            # init variable
            dataList = list()
            modelAppendStatusPath = modelAppendVar.getEnginePath() + "\\Status.ModelAppend.eGroup"
            if len(modelAppendVar.getFaceDBHashset()) > 0:
                for faceDBPath in modelAppendVar.getFaceDBHashset():
                    dataList.append(faceDBPath)
            else:
                for d in modelAppendVar.getFaceDBList():
                    dataList.append(d)
            txtUtil.create(modelAppendVar.getListPath(), dataList, Charsets.BIG5)
            modelAppendVar.generateCli(modelAppendVar.getEnginePath())
            if modelAppendVar.getCommandList() is not None:
                cmdUtil = CmdUtil()
                if cmdUtil.cmdProcessBuilder(modelAppendVar.getCommandList()):
                    modelAppendResult = checkStatusUtil.modelAppend(modelAppendStatusPath, waitTime)
                    if deleteModelAppendStatus:
                        try:
                            os.remove(modelAppendStatusPath)
                        except Exception as e:
                            LOGGER.error(json.dumps(e))
                    else:
                        modelAppendResult.setAppendCmdSuccess(False)
                else:
                    modelAppendResult.setAppendCmdSuccess(False)
            else:
                modelAppendResult.setAppendCmdSuccess(False)
        return modelAppendResult

    def modelSwitch(self, modelSwitch: ModelSwitch, deleteModelSwitchStatus: bool) -> ModelSwitchResult:
        # init func
        attributeCheck = AttributeCheck()
        # init variable
        modelSwitchResult = ModelSwitchResult()
        if modelSwitch is not None and attributeCheck.stringsNotNull(modelSwitch.getNewModelPath(),
                                                                     modelSwitch.getSwitchFilePath(),
                                                                     modelSwitch.getEnginePath(),
                                                                     modelSwitch.getModelSwitchStatusPath()):
            # init variable
            newModelFaceDB_path = modelSwitch.getNewModelPath() + ".faceDB"
            if osp.exists(newModelFaceDB_path):
                # init func
                checkStatusUtil = CheckStatusUtil()
                # Model
                dataList = list()
                dataList.append(newModelFaceDB_path)
                # init func
                txtUtil = TxtUtil()
                flag = txtUtil.create(modelSwitch.getSwitchFilePath(), dataList, Charsets.BIG5)
                if flag:
                    modelSwitchResult = checkStatusUtil.modelSwitch(modelSwitch.getModelSwitchStatusPath())
                    if modelSwitchResult is not None and deleteModelSwitchStatus:
                        try:
                            os.remove(modelSwitch.getModelSwitchStatusPath())
                        except Exception as e:
                            LOGGER.error(json.dumps(e))
        return modelSwitchResult

    def modelInsert(self, modelInsert: ModelInsert, deleteModelInsertStatusFlag: bool,
                    waitTimeMs: int) -> ModelInsertResult:
        # init func
        attributeCheck = AttributeCheck()
        # init variable
        modelInsertResult = ModelInsertResult()

        if modelInsert is not None and attributeCheck.listNotEmpty(
                modelInsert.getFaceDBList()) and attributeCheck.stringsNotNull(modelInsert.getListPath()):
            # init func
            txtUtil = TxtUtil()
            checkStatusUtil = CheckStatusUtil()
            # init variable
            dataList = list()
            modelInsertLog_path = modelInsert.getEnginePath() + "\\Status.ModelInsert.eGroup"

            for d in modelInsert.getFaceDBList():
                dataList.append(d)

            txtUtil.create(modelInsert.getListPath(), dataList, Charsets.BIG5)
            modelInsertResult = checkStatusUtil.modelInsert(modelInsertLog_path, waitTimeMs)

            if deleteModelInsertStatusFlag:
                os.remove(modelInsertLog_path)
        return modelInsertResult
