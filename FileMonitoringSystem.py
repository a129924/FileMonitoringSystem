import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, time

from ExcelDataParser import ExcelDataParser
from FileManager import FileMoveManager
from ZipUtility import ZipExtrator

setter = ExcelDataParser(
    r"D:\code\python\FileMonitoringSystem\Setting\ProjectSettingInfo.xlsx", "ProjectSettingInfo")
SETTING_DATA = setter.reset_index(setter.dataframe, "目的路徑")

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, dirs):
        FileSystemEventHandler.__init__(self)
        self.dirs = dirs

        self.src_files: dict = {}
        self.count = 0
        
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
        if event.is_directory:
            print("directory 'created':{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
            self.create_new_file(event.src_path)
            
            working_path = os.path.dirname(event.src_path)
            print(self.src_files)
            self.print_info("created", event.src_path)
            
            if working_path in SETTING_DATA.keys():
                setting_data = SETTING_DATA[working_path]
                regex_strings = setting_data["正式檔下載檔名"] if isinstance(setting_data["正式檔下載檔名"], list) else [setting_data["正式檔下載檔名"]]
                filename = os.path.basename(event.src_path)
                if self.is_match_regex_file(filename, regex_strings):
                    # move_file()
                    dst_path = setting_data["作業目錄"]
                    while True:
                        time.sleep(0.5)
                        try:
                            FileMoveManager(dst_path).move_file(fr"{event.src_path}",)
                            break
                        except Exception as e:
                            if "[Errno 13]" in str(e):
                                pass
                    
                    print("移動完畢")
                    
                    # unzip()
                    if event.src_path.endswith(".zip"):
                        ZipExtrator(
                            zip_file=os.path.join(dst_path, "DATA", filename),
                            password = "1234", 
                            to_path= os.path.join(dst_path, "DATA")).unzip(True)
                        
                else:
                    print(f"match field file: {os.path.basename(event.src_path)}")
                    
                    
            
            
            

        
        # print(f"file created size: {os.path.getsize(event.src_path)}") # TODO: 把檔案大小塞進self.src_files[event.src_path] = os.path.getsize(event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            print("directory 'deleted':{0}".format(event.src_path))
            # files:list[str] = os.listdir(event.src_path)
            # self.delete_src_files(event.src_path, files)
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
    #         print(self.src_files)

    #     self.print_info("modified", event.src_path)
        
    def run_job(self,):
        for dir in dirs:
            
            observer.schedule(self, dir, True)
            print('thread id:', threading.get_ident())
        observer.start()

        print(input("input any..."))

    def run_job_2(self,):
        while True:
            for dir in self.dirs:
                observer.schedule(self, dir, True)
                print('thread id:', threading.get_ident())
                observer.start()

                try:
                    pass
                except KeyboardInterrupt:
                    observer.stop()

                observer.join()
                print(input("input any..."))


if __name__ == "__main__":
    observer = Observer()
    dirs = [r"D:\TEST\UserProfile", r"D:\TEST\UserProfile\Auto\ProjectFolder"]
    # dirs = ["/home/andrew/TEST/UserProfile/",
    #         "/home/andrew/TEST/UserProfile/Auto/ProjectFolder/"]
    # dirs = ["/home/andrew/TEST/UserProfile/"]
    monitor = FileEventHandler(dirs)

    monitor.run_job_2()
