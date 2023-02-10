from shutil import move
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, time
import argparse

from typing import Tuple

from ExcelDataParser import ExcelDataParser
from FileManager import FileMoveManager
from ProjectInfo import ProjectFileInfo
from ZipUtility import ZipExtrator, ZipUtility
from threading import Thread
import queue


def LoadData(excel_fullpath:str, sheetname:str):
    assert excel_fullpath is not None and sheetname is not None
    return ExcelDataParser(fr"{excel_fullpath}", sheetname)

MOVE_FILE_QUEUE = queue.Queue()

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, dir):
        FileSystemEventHandler.__init__(self)
        self.dir = dir

        self.src_files: dict = {}
        self.count = 0
    
    @property
    def SETTING_DATA_HEADER(self):
        return list(SETTING_DATA.keys())
    @property
    def working_directories(self)->list:
        return list(map(os.path.dirname, self.src_files.keys()))
    
    @staticmethod
    def is_match_regex_file(file:str, regex_strings:list)->bool:
        import re
        for regex in regex_strings:
            if re.match(fr"{regex}", file):
                return True
        return False
    
    def is_in_monitored_directory(self, dir_path:str)->Tuple[bool, str]:
        if dir_path in self.SETTING_DATA_HEADER:
            return (True, dir_path)

        for folder in self.SETTING_DATA_HEADER:
            if folder in dir_path:
                return (True, folder)
        
        return (False, str())
    
    def print_info(self, event_type, path:str):
        print(f"'{self.count}' 'thread id:'{threading.get_ident()} file {event_type} size: {os.path.getsize(path)}")
        print("############################")
        self.count += 1

    def now_file_size(self, path: str) -> None:
        if self.src_files[path] < os.path.getsize(path):
            self.src_files[path] = os.path.getsize(path)

    def create_new_file(self, path: str) -> None:
        self.src_files[path] = os.path.getsize(path)

    def delete_src_file(self, path: str) -> None:
        del self.src_files[path]

    def delete_src_files(self, path: str, files: list) -> None:
        for file in files:
            self.delete_src_file(os.path.join(path, file))
    
    def on_moved(self, event):
        # TODO: 先從這邊下手
        if event.is_directory:
            print("directory 'moved' from {0} to {1}".format(
                event.src_path, event.dest_path))
        else:
            print("file 'moved' from {0} to {1}".format(
                event.src_path, event.dest_path))

            self.delete_src_file(event.src_path)

            self.create_new_file(event.dest_path)
            self.now_file_size(event.dest_path)

        # TODO: 把檔案大小塞進self.src_files[event.src_path] = os.path.getsize(event.src_path)
        self.print_info("moved", event.dest_path)

    def on_created(self, event):
        if event.src_path not in self.src_files.keys():
            if event.is_directory:
                print("directory 'created':{0}".format(event.src_path))
                
            else:
                print("file created:{0}".format(event.src_path))
                self.create_new_file(event.src_path)
                
                working_path:str = os.path.dirname(event.src_path) # 將路徑(含檔案)只取路徑
                self.print_info("created", event.src_path)
                
                is_match_file , match_path = self.is_in_monitored_directory(working_path)
                if is_match_file:

                    setting_data = SETTING_DATA[match_path]
                    regex_strings = setting_data["正式檔下載檔名"] if isinstance(setting_data["正式檔下載檔名"], list) else [setting_data["正式檔下載檔名"]]
                    filename = os.path.basename(event.src_path)
                    if self.is_match_regex_file(filename, regex_strings):
                        dst_path = setting_data["作業目錄"]
                        dst_path = fr"{dst_path}"
                        # src_path, dst_path, filename : ('E:\\MAIL\\Andrew\\Auto\\安聯人壽－每日補單\\安聯每日測試資料夾2\\安聯每日測試.msg', 'E:\\DATA\\IAN\\IAN1\\0206TST', '安聯每日測試.msg')
                        # src_path, dst_path, filename : ('E:\\MAIL\\Andrew\\Auto\\安聯人壽－每日補單\\安聯每日測試.msg', 'E:\\DATA\\IAN\\IAN1\\0206TST', '安聯每日測試.msg')
                        MOVE_FILE_QUEUE.put([event.src_path, dst_path, filename])

                    else:
                        print(f"match field file: {os.path.basename(event.src_path)}")
                else:
                    print(f"'{event.src_path}'不匹配任一個目的路徑")
        
    def on_deleted(self, event):
        if event.src_path in self.src_files.keys():
            if event.is_directory:
                print("directory 'deleted':{0}".format(event.src_path))
            else:
                print("file 'deleted':{0}".format(event.src_path))
                self.delete_src_file(event.src_path)
                
            print(self.src_files)
            print("#############################")

    # def on_modified(self, event):
    #     if event.is_directory:
    #         print("directory 'modified':{0}".format(event.src_path))
    #     else:
    #         print("file 'modified':{0}".format(event.src_path))

    #         self.now_file_size(event.src_path)
    #         

    #     self.print_info("modified", event.src_path)
        
    def run_job(self,):
        observer.schedule(self, self.dir, True)
        print('thread id:', threading.get_ident())
        observer.start()

        print(input("input any..."))

def move_file(src_path: str, dst_path: str, easy_move:bool=False)->tuple:
    print("移動完畢")
    return FileMoveManager(dst_path).move_file(fr"{src_path}", easy_move = easy_move)

def copy_file(src_path:str, dst_path:str, rename:bool, new_filename:str) -> Tuple[bool, str]:
    return FileMoveManager(dst_path).copy_file(src_path, rename, new_filename)

def unzip(dst_path: str, filename: str, password, create_folder_by_extension:bool, move_no_same_filename_by_folder:dict):
    ZipExtrator(
        zip_file=os.path.join(dst_path,filename),
        password=password,
        to_path=dst_path).unzip(create_folder_by_extension, move_no_same_filename_by_folder)

def get_project_setting_info(filepath:str)->ProjectFileInfo:
    return ProjectFileInfo(filepath)

def have_XXXX(string:str,target:str)->str:
    if "╳╳╳╳" in string:
        return string.replace("╳╳╳╳", target)
    elif "XXXX" in string:
        return string.replace("XXXX", target)
    elif "mmdd" in string:
        return string.replace("mmdd", target)

    return string

def print_thread_id(move_files:list):
    print('thread id:', threading.get_ident())

    # ['E:\\MAIL\\Andrew\\Auto\\安聯人壽－每日補單\\新壓縮 (zipped) 資料夾 (2).zip', 'E:\\DATA\\IAN\\IAN1\\0203TST', '新壓縮 (zipped) 資料夾 (2).zip']
    src_path, dst_path, filename = move_files
    project_setting_path = os.path.dirname(dst_path)

    print(f"src_path, dst_path, filename : {(src_path, dst_path, filename)}")
    print(f"project_setting_path : {project_setting_path}")

    json_data = get_project_setting_info(os.path.join(project_setting_path, "FileSetting.json"))
    
    if os.path.exists(dst_path) is False:
        os.mkdir(dst_path)

    # (True, 移動檔案的完整路徑不包含檔案名稱)
    is_move_over, unzip_path = move_file(src_path, dst_path, easy_move=json_data.easy_move)
    print(f"move_file : {(is_move_over, unzip_path)} filename : {filename}")
    if is_move_over and ZipUtility.is_zipfile(os.path.join(unzip_path, filename)):
        unzip(unzip_path, 
        filename, 
        password=str(json_data.zip_password), 
        create_folder_by_extension=json_data.create_folder_by_extension,
        move_no_same_filename_by_folder=json_data.move_same_filename_by_folder)
    
    vba_main_file_info = json_data.vba_main_file_info
    src_vba_filename:str = vba_main_file_info["filePath"]  # type: ignore
    is_check_name = vba_main_file_info["checkName"]["type"]  # type: ignore



    if not os.path.exists(os.path.join(dst_path, os.path.basename(src_vba_filename))):
        copy_to_path:str = vba_main_file_info["toPath"]   # type: ignore
        if is_check_name:
            new_filename = os.path.join(copy_to_path, os.path.basename(have_XXXX(src_vba_filename, vba_main_file_info["checkName"]["target"])))  # type: ignore
            is_copy, vba_file =  copy_file(src_vba_filename, copy_to_path, rename=True, new_filename=new_filename)  # type: ignore
        else:
            is_copy, vba_file =  copy_file(src_vba_filename, copy_to_path, rename=False, new_filename="")  # type: ignore

        if is_copy:
            os.startfile(fr"{dst_path}")
            os.startfile(fr"{vba_file}")



    print("done")

def file_mover():
    i = 0
    while True:
        move_files = []
        if MOVE_FILE_QUEUE.empty():
            pass
        else:
            move_files:list[str] = MOVE_FILE_QUEUE.get()

            children_thread = Thread(target=print_thread_id, args=(move_files,))
            children_thread.start()

        print(f'{i} thread id: {threading.get_ident()} move_file: {move_files}')

        time.sleep(1)
        i += 1

if __name__ == "__main__":
    
    cmd_parser = argparse.ArgumentParser(description="FileMonitoringSystem Command")
    cmd_parser.add_argument("-p", "--excel_data_fullpath", type=str, help="專案設定檔完整路徑")
    cmd_parser.add_argument("-s", "--sheetname", type=str ,help="專案設定檔的sheetname")
    cmd_parser.add_argument("-m", "--monitor_path", type=str ,help="偵測的路徑")
    args = cmd_parser.parse_args()

    setter = LoadData(
        args.excel_data_fullpath, args.sheetname)
    SETTING_DATA = setter.reset_index(setter.dataframe, "目的路徑")
    dirs = fr"{args.monitor_path}"
    print(f"專案設定檔完整路徑 : {args.excel_data_fullpath},\n專案設定檔的sheetname : {args.sheetname}\n偵測的路徑 : {dirs}")

    consumer = Thread(target=file_mover, args=())
    consumer.start()

    observer = Observer()
    monitor = FileEventHandler(dirs)
    monitor.run_job()

