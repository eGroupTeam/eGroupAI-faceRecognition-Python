import os.path as osp

from egroup.util.TxtUtil import TxtUtil, Charsets
from egroup.util.UUIDGenerator import UUIDGenerator


class CreateEngineFileUtil:
    def createTrainFaceTxt(self, trainListPath: str, trainFaceList: list) -> bool:
        # init func
        uuidGenerator = UUIDGenerator()
        txtUtil = TxtUtil()
        flag = False
        # Create training
        dataList = list()
        for getTrainFace in trainFaceList:
            for imagePath in getTrainFace.getImagePathList():
                dataList.append(imagePath + "\t" + getTrainFace.getPersonId() + "[No]" + uuidGenerator.getUUID())
        txtUtil.create(trainListPath, dataList, Charsets.BIG5)
        if osp.exists(trainListPath):
            flag = True
        return flag
