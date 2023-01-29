import os
from time import sleep, time

from FileManager import FileMoveManager
from asyncio_main import AsyncPackage

file_mover = FileMoveManager(r"C:\Users\user\TEST_DATA")
files = ["TEST1.zip", "TEST2.txt"]
args = (os.path.join(r"D:\code\python\FileMonitoringSystem\data", file) for file in files)

asyncio_creator = AsyncPackage(file_mover.move_file, args)

# def now(): return time()
# start = now()
# 
# print(now() - start)
now_dir_list = os.listdir(r".\DATA")
print(now_dir_list)

while True:
    sleep(0.1)
    if now_dir_list != os.listdir(r".\DATA"):
        new_file = set(os.listdir('.\\DATA')) - set(now_dir_list)
        print(f"new_file: {new_file}")
        args = (os.path.join(r"D:\code\python\FileMonitoringSystem\data", file) for file in new_file)
        asyncio_creator = AsyncPackage(file_mover.move_file, args)
        asyncio_creator.run()
        # now_dir_list = os.listdir('.\\DATA')
        print("我在run底下")
        print(now_dir_list)
        # break
    
