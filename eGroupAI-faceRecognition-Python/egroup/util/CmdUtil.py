import subprocess
import os
from egroup.util.LoggingUtil import LOGGER


class CmdUtil:
    TASKLIST = "tasklist"
    KILL = "taskkill /F /IM "

    @staticmethod
    def cmdProcessBuilder(commandList: list) -> bool:
        process = subprocess.Popen(commandList[-1], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   universal_newlines=True, shell=True, errors="ignore")
        while process.poll() is None:
            line = process.stdout.readline()
            LOGGER.info(line.strip())
        if process.returncode < 0:
            return False
        return True

    def server_cmdProcessBuilder(self, commandList: list) -> bool:

        try:
            process = subprocess.Popen(commandList, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       universal_newlines=True, shell=True)

            while process.poll() is None:
                line = process.stdout.readline()
                # print(line,end="")
                LOGGER.info(line)
            if process.returncode != 0:
                return False
            return True
        except:
            LOGGER.error("ERROR", exc_info=True)

        return False

    def isProcessRunning(self, serviceName: str) -> bool:
        try:
            process = subprocess.Popen([CmdUtil.TASKLIST], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       universal_newlines=True, shell=True)
            while process.poll() is None:
                line = process.stdout.readline()
                if serviceName in line:
                    return True
        except Exception as e:
            LOGGER.error("ERROR", exc_info=True)

        return False

    def cmdProcessCheck(self, processName: str) -> bool:
        if self.isProcessRunning(processName):
            return True
        return False

    def killProcess(self, processName: str):
        try:
            os.system(self.KILL + processName)
        except:
            LOGGER.error("Error", exc_info=True)

    def cmdProcessTerminate(self, processName: str):
        if self.isProcessRunning(processName):
            self.killProcess(processName)
