import json ,os

from typing import Dict, Any

from ExcelDataParser import ExcelDataParser


def load_excel_data(src_path:str, sheetname:str, is_convert:bool)->ExcelDataParser:
    return ExcelDataParser(fr"{src_path}", sheetname, is_convert)

def data_to_json(key:str ,data:dict):
    return {
        "ProjectName": key,
        "ZipPassword": data["專案來檔壓縮密碼"],
        "EasyMove": False,
        "CreateFolderByExtension": data["壓縮檔是否直接解壓縮到路徑"],
        "VbaMainFileInfo": {
            "filePath": data["VBA主程式路徑"],
            "toPath": data["VBA主程式放置路徑"]
        },
        "ZipFile": {
            "zipFileName": data["客戶抽測壓縮檔名稱"],
            "password": data["客戶抽測壓縮檔密碼"],
        },
        "UploadFiles": {
            "Files": data["上機檔案"],
            "toPath": data["上機檔案路徑"]
        }
    }

def create_project_json_file(projects_data:Dict[str,Any])->None:
    for project, setting_data in projects_data.items():
        project_basepath:str = os.path.dirname(setting_data["作業目錄"])
        dst_path = os.path.join(project_basepath, "Setting")
        
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)

        project_setting_data_fullpath = os.path.join(dst_path, "ProjectSetting.json")
        with open(project_setting_data_fullpath, "w", encoding="UTF-8") as file:
            json.dump(data_to_json(project, setting_data), file, ensure_ascii=False)
            print(f"json file is created :'{project_setting_data_fullpath}'")

# SETTING_DATA = setter.reset_index(setter.dataframe, "目的路徑")
excel_parser = load_excel_data(r"E:\自動執行程式\Python\ProjectSettingInfo.xlsx", "ProjectSettingInfo", is_convert=False)
projects_data = excel_parser.reset_index(excel_parser.dataframe, "案件代碼")

# print(type(projects_data["IAN1"]["專案來檔是否直接放到路徑"]))


# project_data = data_to_json("IANB", projects_data["IANB"])
# print(project_data)
# print(projects_data["IANB"]["作業目錄"])

# with open(".\DATA\data2.json", "w", encoding="UTF-8") as file:
#     json.dump(project_data, file, ensure_ascii=False)

create_project_json_file(projects_data)



