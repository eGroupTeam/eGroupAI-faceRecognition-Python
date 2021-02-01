import os
import os.path as osp
import threading
from threading import Thread

from egroup.util.FolderUtil import FolderUtil
from egroupai.engine.control.CreateEngineFileUtil import CreateEngineFileUtil
from egroupai.engine.control.EngineUtil import EngineUtil
from egroupai.engine.control.GetResultUtil import GetResultUtil
# TODO: add logging
from egroupai.engine.entity.ModelAppend import ModelAppend
from egroupai.engine.entity.ModelInsert import ModelInsert
from egroupai.engine.entity.RecognizeFace import RecognizeFace
from egroupai.engine.entity.TrainFace import TrainFace


# init func
engineUtil = EngineUtil()
createEngineFileUtil = CreateEngineFileUtil()
folderUtil = FolderUtil()
getResultUtil = GetResultUtil()
# init variable
logDeleteFlag = False
# init path
quickStartPath = "C:\\QuickStart"
enginePath = quickStartPath + "\\eGroupAI_FaceEngine_CPU_Windows_V4.2.2"
faceDBPath = enginePath + "\\eGroup"
resourcesPath = enginePath + "\\resources"
trainResultLogPath = enginePath + "\\Status.TrainResultCPU.eGroup"
trainListPath = resourcesPath + "\\list.txt"
modelAppendListPath = faceDBPath + "\\modelList.egroup.List"
outputfacePath = enginePath + "\\outputFace"
outputframePath = enginePath + "\\outputFrame"
jsonFolderPath = enginePath + "\\json"
catchJsonName = "output.cache.egroup"
# final static
# allJsonName = "output." + LocalDate.now() + ".egroup"
# allJsonName = "output." + datetime.today().strftime('%Y-%m-%d') + ".egroup"
modelInserFilePath = enginePath + "\\Singal_For_Model_Insert.txt"
videoPath = "resources\\example.mp4"
resolution = "720p"
# init file
# outputfaceFile = new File(outputfacePath.toString())
# faceDBFile = new File(faceDBPath.toString());
# outputframeFile = new File(outputframePath.toString())
# jsonFolderFile = new File(jsonFolderPath.toString())
# init person path
jerryFaceDBPath = faceDBPath + "\\jerry"
leonardFaceDBPath = faceDBPath + "\\leonard"
danielFaceDBPath = faceDBPath + "\\daniel"
# init person image
jerryFaceImageFolderPath = resourcesPath + "\\jerry"
danielFaceImageFolderPath = resourcesPath + "\\daniel"
lenardFaceImageFolderPath = resourcesPath + "\\leonard"
# jerryFaceImageFolder = new File(jerryFaceImageFolderPath.toString())
# danielFaceImageFolder = new File(danielFaceImageFolderPath.toString());
# leonardFaceImageFolder = new File(lenardFaceImageFolderPath.toString());


def createDir(path):
    if not osp.exists(path):
        os.makedirs(path)


def getFaceDBPath(name: str):
    faceDB = str(faceDBPath)
    if name.lower() == "daniel":
        faceDB = str(danielFaceDBPath)
    elif name.lower() == "leonard":
        faceDB = str(leonardFaceDBPath)
    elif name.lower() == "jerry":
        faceDB = str(jerryFaceDBPath)
    return faceDB


def getFaceImageFolder(name: str):
    imagePathList = list()
    if name.lower() == "daniel":
        imagePathList = folderUtil.listPath(danielFaceImageFolderPath)
    elif name.lower() == "leonard":
        imagePathList = folderUtil.listPath(lenardFaceImageFolderPath)
    elif name.lower() == "jerry":
        imagePathList = folderUtil.listPath(jerryFaceImageFolderPath)
    return imagePathList


def training(name: str):
    # https://www.egroup.com.tw/en/docs/windows-cpu/v4.2.1/getting-started#0054007200610069006e0069006e0067
    # init variable
    trainFaceList = list()
    # Set training variable
    trainFace = TrainFace()
    trainFace.setTrainListPath(str(trainListPath))
    trainFace.setModelPath(getFaceDBPath(name))
    trainFace.setEnginePath(str(enginePath))
    trainFace.setPersonId(name)
    # Get image in folder and set training image
    trainFace.setImagePathList(getFaceImageFolder(name))
    # Add to trainFace list
    trainFaceList.append(trainFace)
    # Create train face list
    createEngineFileUtil.createTrainFaceTxt(str(trainListPath), trainFaceList)
    # Start training and get result
    trainResult = engineUtil.trainFace(trainFace, logDeleteFlag)
    # LOGGER.info("trainResult=" + new Gson().toJson(trainResult))


def recognition(usedFaceDB: str):
    # Set recognition variable
    recognizeFace = RecognizeFace()
    recognizeFace.setEnginePath(str(enginePath))
    recognizeFace.setTrainedFaceDBPath(usedFaceDB)
    recognizeFace.setOutputFacePath(str(outputfacePath))
    recognizeFace.setOutputFramePath(str(outputframePath))
    recognizeFace.setJsonPath(jsonFolderPath + "\\output")
    recognizeFace.setHideMainWindow(False)
    recognizeFace.setOutputFrame(True)
    recognizeFace.setOutputFace(True)
    recognizeFace.setOnface(True)
    recognizeFace.setThreshold(0.6)
    recognizeFace.setResolution(resolution)
    recognizeFace.setVideoPath(str(videoPath))
    recognizeFace.setMinimumFaceSize(100)
    recognizeFace.setThreads(2)
    # Start recognition
    engineUtil.recognizeFaceSingle(recognizeFace)
    # Get all result after recognize is done
    faceList = getResultUtil.cacheResult(str(jsonFolderPath), str(catchJsonName))
    # TODO: logging


def modelInsert(name: str):
    # Set insert facedb list
    faceDBList = list()
    faceDBList.append(getFaceDBPath(name) + ".faceDB")
    # Set model insert variable
    modelInsertVar = ModelInsert()
    modelInsertVar.setEnginePath(str(enginePath))
    modelInsertVar.setFaceDBList(faceDBList)
    modelInsertVar.setListPath(str(modelInserFilePath))
    modelInsertResult = engineUtil.modelInsert(modelInsertVar, False, 3000)
    # TODO: logging


def modelAppend():
    # https://www.egroup.com.tw/en/docs/windows-cpu/v4.2.1/getting-started#0054007200610069006e0069006e0067
    # Set append faceDB list
    faceDBList = list()
    faceDBList.append(jerryFaceDBPath + ".faceDB")
    faceDBList.append(leonardFaceDBPath + ".faceDB")
    faceDBList.append(danielFaceDBPath + ".faceDB")
    # Model Append
    modelAppendVar = ModelAppend()
    modelAppendVar.setTrainedFaceDBPath(faceDBPath + ".faceDB")
    modelAppendVar.setFaceDBList(faceDBList)
    modelAppendVar.setListPath(str(modelAppendListPath))
    modelAppendVar.setEnginePath(str(enginePath))
    modelAppendResult = engineUtil.modelAppend(modelAppendVar, False, 2500)
    # TODO: logging


def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return synced_func


def main():
    # ================================================== Create folder==================================================
    createDir(faceDBPath)
    createDir(outputfacePath)
    createDir(outputframePath)
    createDir(jsonFolderPath)
    # ================================================== Step1 : Training===============================================
    # // Example: Input jerry's Face, Create jerry's Face Model.
    # // Document: https: // reurl.cc/Y6r94a
    training("jerry")
    # ==================================================Step2 : Recognition=============================================
    # // Example: Input jerry Face, Recognized with jerry’s Face Model and get Result（JSON）.
    # // Document: https://reurl.cc/Y6r9Ya

    # recognition(jerryFaceDBPath + ".faceDB")

    # @synchronized
    def runRecognition():
        recognition(jerryFaceDBPath + ".faceDB")
    recognitionThread = Thread(target=runRecognition)
    recognitionThread.start()
    # =================================================Step3 : ModelInsert==============================================
    # Document: https://reurl.cc/EzMpQm
    # 1.Example: Input leonard Face(Untrained Face) and Trained immediately
    training("leonard")
    # 2.then Insert leonard Face Model to Face Model and get Recognition Resultat the same time
    modelInsert("leonard")
    # ================================================wait recognition thread done======================================

    # TODO: synchronized (recognitionThread) {
    #       try {
    #         recognitionThread.wait();
    #       } catch (InterruptedException e) {
    #         LOGGER.error(new Gson().toJson(e));
    #       }
    #     }

    # ==================================================Step4 : Model Append============================================
    # Example: Append daniel and leonard Face Model into all face DB.
    # Document: https://reurl.cc/EzMpQm
    # 1.Execute train face instructions (see Training Procedure for details)
    training("daniel")
    # 2.Execute Model Append instructions (see Model Append Procedure for details)
    modelAppend()
    # 3.Recognition - Example: Recognized with all face DB and get Result（JSON）.
    recognitionThread = Thread(target=runRecognition)
    recognitionThread.start()


if __name__ == '__main__':
    main()
