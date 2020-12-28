import shutil
import traceback
import os

class CopyUtil:
    def copyFile(source: str, dest: str):
        try:
          if  not os.path.exists(os.path.dirname(dest)):
              os.mkdir(os.path.dirname(dest))
          shutil.copy(source,dest)
          return True
        except IOError:
          traceback.print_exc()
          return False

    def copyFolder(source: str, dest: str):
      try:
        shutil.copytree(source,dest)
        return True
      except IOError:
        return False
