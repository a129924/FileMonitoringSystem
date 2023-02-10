import os
import shutil
import threading
import time

from typing import Tuple

class FileManager():
    """
    to_same_path(path:str) : 強制轉換path \n
    create_files(filenames:list[str]) : 創建多個檔案 \n
    create_folder(folder:str) : 建立單個資料夾 \n
    create_folders(create_base_folder_path:str, create_folders:list[str] = []) 建立多個資料夾 \n
    """    
    @staticmethod
    def to_same_path(path):
        return os.path.abspath(path)

    @staticmethod
    def create_files(filenames:str)->None:
        for filename in filenames:
            with open(filename, "w"):
                pass
    
    @staticmethod
    def create_folder(folder:str)->None:os.mkdir(folder)

    def create_folders(self, create_base_folder_path:str, create_folders:list = []):
        # create_base_folder_path .\Project\childProject\{today}
        folders = [os.path.join(create_base_folder_path,folder) for folder in create_folders]
        if all(list(map(os.path.exists, folders))) is False:
            self.create_folder(create_base_folder_path)
            for folder in folders:
                self.create_folder(folder)

class FileMoveManager(FileManager):
    def __init__(self,dst_path:str)->None:
        assert os.path.exists(dst_path), "Folder '%s' not exists" % dst_path
        self.dst_path = dst_path
        
    def move_file(self, src_file_path:str, easy_move:bool = False)->tuple:
        """
        return if True return (True, 輸出完整路徑)
        """
        assert os.path.exists(src_file_path), "File '%s' not exists" % src_file_path
        print('thread id:', threading.get_ident())
        
        if easy_move is False:
            file_extension = os.path.splitext(src_file_path)[1]  # get file 副檔名
            if file_extension == ".msg":
                target = "mail"
            else:
                target = "data"
        else:
            target = ""
                
        dst_path = os.path.join(self.dst_path, target) if easy_move is False else self.dst_path
        if os.path.exists(dst_path) is False:
            self.create_folder(dst_path)
        
        while True:
            time.sleep(0.5)
            try:
                shutil.move(src_file_path, dst_path)
                break
            except PermissionError as e:
                pass
        return (True, dst_path)

    def copy_file(self, src_path:str, rename:bool= False, new_filename = "")->Tuple[bool, str]:
        filename = os.path.basename(src_path)
        if rename:
            dst_path = os.path.join(self.dst_path, new_filename)
            print(("dst_path, new_filename: " ,(dst_path, new_filename)))
        else:
            dst_path = os.path.join(self.dst_path, filename)
            print(("dst_path, new_filename: " ,(dst_path, filename)))


        if not os.path.exists(dst_path):
            shutil.copy2(src_path, dst_path)

        return (True, dst_path)

    def move_files(self, files: list, src_path: str):
        # to_path .\Project\childProject\{today}
        for file in files:
            self.move_file(os.path.join(src_path, file))

if __name__ == '__main__':
    # folder_manager = FileManager()
    # folder_manager.create_folders(r".\data\DATA1", ["mail", "data"])
    def now(): return time.time()
    start = now()
    file_mover = FileMoveManager(r"C:\Users\user\TEST_DATA")
    files = ["TEST1.zip", "TEST2.zip"]
    
    file_mover.move_files(files, r"D:\code\python\FileMonitoringSystem\data")
    
    print(now() - start)

    
