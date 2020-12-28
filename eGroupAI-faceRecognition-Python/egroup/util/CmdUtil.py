import subprocess
import logging
import os

class CmdUtil:
  TASKLIST = "tasklist"
  KILL = "taskkill /F /IM "

  def cmdProcessBuilder(commandList: list) -> bool:
    process=subprocess.Popen(commandList,stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,shell=True)

    while process.poll() is None:
      line = process.stdout.readline()
      # print(line,end="")
      logging.info(line)
    if process.returncode!=0:
      return False
    return True

  def server_cmdProcessBuilder(commandList: list) -> bool:

    try:
      process=subprocess.Popen(commandList,stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,shell=True)

      while process.poll() is None:
        line = process.stdout.readline()
        # print(line,end="")
        logging.info(line)
      if process.returncode!=0:
        return False
      return True
    except:
      logging.error("ERROR",exc_info=True)
    
    return False

  
  def isProcessRunning(serviceName: str) -> bool:
    try:
      process=subprocess.Popen([CmdUtil.TASKLIST],stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True)

      while process.poll() is None:
        line=process.stdout.readline()
        if serviceName in line:
          return True
    except:
      logging.error("ERROR",exc_info=True)
    
    return False


  def cmdProcessCheck(processName: str) -> bool:
    if CmdUtil.isProcessRunning(processName):
      return True
    return False

  def killProcess(processName: str):
    try:
      os.system(CmdUtil.KILL+processName)
    except:
      logging.error("Error",exc_info=True)


  def cmdProcessTerminate(processName: str):
    if CmdUtil.isProcessRunning(processName):
      CmdUtil.killProcess(processName)