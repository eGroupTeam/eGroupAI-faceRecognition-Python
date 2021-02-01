
import os
import os.path as osp
from egroup.util.AttributeCheck import AttributeCheck


class FolderUtil:

    def listName(self, folder: str) -> list:
        file_name_list=[]
        if os.path.exists(folder):

            for (dirpath,dirname,filenames) in os.walk(folder):
                for filename in filenames:
                    file_name_list.append(os.path.basename(filename))
                
        return file_name_list

    def listFile(self, folder: str) -> list:
        file_name_list=[]
        if os.path.exists(folder):

            for (dirpath,dirname,filenames) in os.walk(folder):
                for filename in filenames:
                    file_name_list.append(filename)
                
        return file_name_list

    def listPath(self, folder: str)->list:
        file_name_list=[]
        if os.path.exists(folder):

            for (dirpath,dirname,filenames) in os.walk(folder):
                for filename in filenames:
                    file_name_list.append(osp.join(folder, filename))
                
        return file_name_list

    def checkEmpty(self, folder_path: str) -> bool:
        if AttributeCheck.stringsNotNull(folder_path):
            if os.path.exists(folder_path) and os.path.isdir(folder_path) and len(os.listdir(folder_path))>0:
                return False

        return True
