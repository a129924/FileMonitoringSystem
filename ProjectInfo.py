import json
import os

from dataclasses import dataclass
from typing import Dict ,Any

from regex_converter import ComplexString



@dataclass
class ProjectFileInfo():
    json_data_path : str

    def __post_init__(self):
        assert os.path.exists(self.json_data_path)
        self.projectname:str = self.json_data.get("ProjectName")  # type: ignore
        self.zip_password:int = self.json_data.get("ZipPassword")  # type: ignore
        self.easy_move:bool = self.json_data.get("EasyMove")  # type: ignore
        self.create_folder_by_extension:bool = self.json_data.get("CreateFolderByExtension")  # type: ignore
        self.move_same_filename_by_folder:Dict[str,Any] = self.json_data.get("MoveSameFileByFolder")  # type: ignore
        self.vba_main_file_info:Dict[Dict[str, Any],Dict[str,str]] = self.json_data.get("VbaMainFileInfo")  # type: ignore
        self.zip_file:Dict[str, Any] = self.json_data.get("ZipFile")  # type: ignore

    @property    
    def json_data(self)->Dict[str, Any]:
        with open(self.json_data_path, "r", encoding= "UTF-8") as f:
            json_string = f.read()
            json_data = ComplexString(fr"{json_string}").complex_str()
            json_data = json.loads(json_data)
            json_data["ZipFile"]["password"] = "8482"

            # 可以用 但是不是在這邊用            
            # if json_data["VbaMainFileInfo"]["checkName"]["type"]:
            #     json_data["VbaMainFileInfo"]["filePath"] = ComplexString(json_data["VbaMainFileInfo"]["filePath"]).have_XXXX(json_data["VbaMainFileInfo"]["checkName"]["target"])
        return json_data
    
if __name__ == "__main__":
    ## IAN1
    # data = ProjectFileInfo(r"E:\DATA\IAN\IAN1\FileSetting.json")
    # project_data = data.json_data["ZipFile"]
    # print(project_data)  

    ## IAN4
    # data = ProjectFileInfo(r"E:\DATA\IAN\IAN4\FileSetting.json")
    # project_data = data.json_data
    # print(project_data)    

    ## IANA
    data = ProjectFileInfo(r"E:\DATA\IAN\IANA\FileSetting.json")
    project_data = data.json_data["VbaMainFileInfo"]
    print(project_data)        
