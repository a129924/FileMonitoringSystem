
from watchdog.observers import Observer
from watchdog.events import (
    FileDeletedEvent, DirDeletedEvent, FileModifiedEvent,
    DirCreatedEvent, FileCreatedEvent, DirModifiedEvent,
    FileMovedEvent, DirMovedEvent, FileSystemEventHandler)
import time
from datetime import datetime


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        if event.is_directory:
            print("directory 'moved' from {0} to {1}".format(
                event.src_path, event.dest_path))
        else:
            print("file 'moved' from {0} to {1}".format(
                event.src_path, event.dest_path))
        print("#############################")

    def on_created(self, event):
        if event.is_directory:
            print("directory 'created':{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
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
        print("#############################")


if __name__ == "__main__":
    observer = Observer()
    dirs = [r"D:\TEST\UserProfile", r"D:\TEST\UserProfile\Auto\ProjectFolder"]
    for dir in dirs:
        event_handler = FileEventHandler()
        observer.schedule(event_handler, dir, True)
    observer.start()

    print(input("input any..."))
