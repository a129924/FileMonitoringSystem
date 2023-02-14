from asyncio import subprocess
from fileinput import filename
import zipfile
import os
from typing import overload ,Tuple, Dict
import threading



class DriverException(Exception):
    def __init__(self, message):
        super(DriverException, self).__init__(message)

class FileNotDefinedException(Exception):
    def __init__(self, message):
        super(FileNotDefinedException, self).__init__(message)

class ZipUtility:
    @overload
    def __init__(self, zip_file: str): ...
    @overload
    def __init__(self, zip_file: str, password: str): ...
    @overload
    def __init__(self, zip_file: str, to_path: str): ...
    @overload
    def __init__(self, zip_file: str, password: str, to_path: str): ...

    def __init__(self, zip_file: str, password: str = "", to_path: str = "./") -> None:  # type: ignore
        # assert zipfile.is_zipfile(zip_file)
        self.zip_file = zip_file
        self.password = password
        self.to_path = to_path


    
    @staticmethod
    def is_zipfile(zip_file_path:str)->bool:
        return zipfile.is_zipfile(zip_file_path)

class ZipExtrator(ZipUtility):
    """
    # 解壓縮壓縮檔
    1. 支援解密壓縮檔
    2. 可選擇解壓縮檔案存放路徑
    """

    @staticmethod
    def get_unzip_file_folder(filename:str)->Tuple[str,str]:
            decode_file = filename.encode("cp437").decode("BIG5") # V
            foldername = os.path.dirname(filename)
            # file.filename = decode_file
            filename = os.path.basename(decode_file) # 覆蓋原始檔案名稱
            file_extension: str = os.path.splitext(filename)[1][1:].upper()
            # 修改邏輯
            # if is_move:
            #     if file_extension == is_move_file_extension.upper() and foldername == os.path.splitext(filename)[0]:
            #         return (filename, "")
            #     elif file_extension == "TXT":
            #         return (filename, "TST")

            # elif file_extension == "TXT":
            #     return (filename, "TST")
            # 修改邏輯
            if file_extension == "TXT" and "件數套印資料" in filename:
                return (filename, "TST")
            elif file_extension == "TXT" or (file_extension == "" and filename[-1] != "/"):
                return (filename, "")

           
            return (filename, file_extension)

    def unzip(self, create_folder_by_extension: bool, special_type:Dict[str,str]) -> None:
        """
        create_folder_by_extension若為True則會在to_path底下創建該檔案副檔名的資料夾 並將檔案放置在這底下 若為False會直接依照to_path放置在該路徑
        move_same_filename_by_folder
        special_type
        """
        with zipfile.ZipFile(self.zip_file, "r", zipfile.ZIP_DEFLATED,) as zip_reader:
            # same_is_move:bool = move_same_filename_by_folder.get("isMove") # type: ignore
            # same_file_extension:str = move_same_filename_by_folder.get("fileExtension")  # type: ignore
            special_type_type:str = special_type.get("type")  # type: ignore
            

            print(f"thread id:{threading.get_ident()}")
            try:
                if create_folder_by_extension:
                    for file in zip_reader.infolist():
                        if os.path.splitext(file.filename)[1] == "":
                            continue
                        file.filename, file_extension = self.get_unzip_file_folder(file.filename) 

                        path = fr".\{os.path.join(self.to_path, file_extension)}"
                        # (file, path, file.orig_filename) : ('REMINDER_T11200001078.pdf', '.\\E:\\DATA\\IAN\\IAN1\\0207TST\\data\\PDF', 'REMINDER_20230204/REMINDER_T11200001078.pdf')
                        print(f"(file, path, file.orig_filename) : {(file.filename, path, file.orig_filename)}")

                        zip_reader.extract(
                            file,
                            path=fr".\{os.path.join(self.to_path, file_extension)}",
                            pwd=self.password.encode("ascii") if self.password != b"" else None
                            )

                else:
                    zip_reader.extractall(
                        path=self.to_path, 
                        pwd=self.password.encode("ascii") if self.password.encode("ascii") != b"" else None
                        )

            except NotImplementedError:
                import subprocess
                command = [r"D:\CODE\NEW\FileMonitoringSystem-main\EXE\7z.exe",
                "x", self.zip_file, f"-o{os.path.dirname(self.zip_file)}",
                f"-p{self.password}"]

                subprocess.run(command)     

class ZipCreator():
    """
    # 建立壓縮檔
    1. 支援加密壓縮 
    2. 支援多個檔案、資料夾，單個檔案、資料夾壓縮成壓縮檔
    """

    def __init__(self,zip_filename: str,  password: str, to_path: str , zip_driver: str = ".\\EXE\\7z.exe") -> None:
        if os.path.isfile(zip_driver) is False:
            raise DriverException("Zip driver not found")

        self.zip_filename = zip_filename
        self.password = password
        self.to_path = to_path
        self.zip_driver = zip_driver
    
    @staticmethod
    def is_all_defined(src_path, files: list) -> bool:
        return set(os.listdir(src_path)) & set(files) == set(files)

    def compress_files(self, src_path: str, files: list) -> bool:
        if self.is_all_defined(src_path, files) is False:
            raise FileNotDefinedException("File not defined")

        import subprocess

        command = [self.zip_driver, 'a', f'-p{self.password}', f"{self.zip_filename}"] + [
            os.path.join(src_path, file) for file in files]
        result = subprocess.run(command)
        
        return result.returncode == 0


if __name__ == "__main__":
    # # 解壓縮檔案
    # zip_file = ZipExtrator("aio1.zip", password="1234", to_path="./data")  # V
    # print(zip_file.unzip(True))

    # 檔案壓縮成壓縮檔

    create_zip = ZipCreator(zip_filename = "aio加密8482.zip", password = "8482", to_path=".\\EXE") # V
    create_zip.compress_files(src_path=".\\", files= ["ABC.md","ABC.pdf"])
