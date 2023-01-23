
from watchdog.observers import Observer
from watchdog.events import (
    FileDeletedEvent, DirDeletedEvent, FileModifiedEvent,
    DirCreatedEvent, FileCreatedEvent, DirModifiedEvent,
    FileMovedEvent, DirMovedEvent, FileSystemEventHandler)
import os


class FileEventHandler(FileSystemEventHandler):
    def __init__(self,dirs):
        FileSystemEventHandler.__init__(self)
        self.dirs = dirs

        self.src_files:dict = {}
        self.move_files:dict = {}

    def now_file_size(self,path:str)->None:
        if self.src_files[path] < os.path.getsize(path):
            self.src_files[path] = os.path.getsize(path)
    
    def create_new_file(self,path:str)->None:
        self.src_files[path] = os.path.getsize(path)

    def delete_src_file(self,path:str)->None:
        del self.src_files[path]

    def delete_src_files(self,path:str, files:list)->None:
        for file in files:
            self.delete_src_file(os.path.join(path, file))

    def on_moved(self, event):
        # TODO: 先從這邊下手
        if event.is_directory:
            print("directory 'moved' from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file 'moved' from {0} to {1}".format(event.src_path, event.dest_path))

            self.delete_src_file(event.src_path)

            self.create_new_file(event.dest_path)
            self.now_file_size(event.dest_path)
            
        print(f"file moved size: {os.path.getsize(event.dest_path)}") # TODO: 把檔案大小塞進self.src_files[event.src_path] = os.path.getsize(event.src_path)
        


        print("#############################")

    def on_created(self, event):
        if event.is_directory:
            print("directory 'created':{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
            self.create_new_file(event.src_path)

            print(self.src_files)

        print("#############################")
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

    def on_modified(self, event):
        if event.is_directory:
            print("directory 'modified':{0}".format(event.src_path))
        else:
            print("file 'modified':{0}".format(event.src_path))

            self.now_file_size(event.src_path)
            print(self.src_files)
            
        print("#############################")

    def run_job(self,):
        for dir in dirs:
            observer.schedule(self, dir, True)
        observer.start()

        print(input("input any..."))

    def run_job_2(self,):
        while True:
            for dir in self.dirs:
                observer.schedule(self, dir, True)
                observer.start()
        
                try:
                    pass
                except KeyboardInterrupt:
                    observer.stop()

                observer.join()


if __name__ == "__main__":
    observer = Observer()
    # dirs = [r"D:\TEST\UserProfile", r"D:\TEST\UserProfile\Auto\ProjectFolder"]
    dirs = ["/home/andrew/TEST/UserProfile/", "/home/andrew/TEST/UserProfile/Auto/ProjectFolder/"]
    # dirs = ["/home/andrew/TEST/UserProfile/"]
    monitor = FileEventHandler(dirs)

    monitor.run_job_2()
