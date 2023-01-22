
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

    def on_moved(self, event):
        if event.is_directory:
            print("directory 'moved' from {0} to {1}".format(
                event.src_path, event.dest_path))
        else:
            print("file 'moved' from {0} to {1}".format(
                event.src_path, event.dest_path))
        print(f"file moved size: {os.path.getsize(event.dest_path)}") # TODO: 把檔案大小塞進self.src_files[event.src_path] = os.path.getsize(event.src_path)
        print("#############################")

    def on_created(self, event):
        if event.is_directory:
            print("directory 'created':{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
        print(f"file created size: {os.path.getsize(event.src_path)}")
        print("#############################")

    def on_deleted(self, event):
        if event.is_directory:
            print("directory 'deleted':{0}".format(event.src_path))
        else:
            print("file 'deleted':{0}".format(event.src_path))
        print("#############################")

    def on_modified(self, event):
        if event.is_directory:
            print("directory 'modified':{0}".format(event.src_path))
        else:
            print("file 'modified':{0}".format(event.src_path))
        print(f"file modified size: {os.path.getsize(event.src_path)}") # TODO: 把檔案大小塞進self.src_files[event.src_path] = os.path.getsize(event.src_path)
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
