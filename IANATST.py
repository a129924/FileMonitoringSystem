import zipfile
import os

file = r"E:\DATA\IAN\IANA\0210TST\data\變額年金累積期滿給付通知書.zip"
zip_driver = r"D:\CODE\NEW\FileMonitoringSystem-main\EXE\7z.exe"

print(zipfile.is_zipfile(file))

with zipfile.ZipFile(file, "r", zipfile.ZIP_DEFLATED,) as zip_reader:
    try:
        zip_reader.extractall(path=".\\DATA", pwd = "89283591".encode("ascii"))
    except NotImplementedError:
        import subprocess
        command = [zip_driver, "x", file, f"-o{os.path.dirname(file)}", "-p89283591"]
        result = subprocess.run(command)
        
        print(result)
