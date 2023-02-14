import zipfile
import os

with  zipfile.ZipFile(r"D:\CODE\NEW\FileMonitoringSystem-main\DATA\DATA.zip", "r", zipfile.ZIP_DEFLATED,) as zip_reader:
    for file in zip_reader.namelist():
        print(os.path.splitext(file), file.endswith(".txt"), file[-1] != "/")



