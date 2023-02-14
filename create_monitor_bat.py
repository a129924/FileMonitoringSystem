import os

from ExcelDataParser import ExcelDataParser


def load_excel_data(src_path:str, sheetname:str, is_convert:bool)->ExcelDataParser:
    return ExcelDataParser(fr"{src_path}", sheetname, is_convert)

def create_bat(usernames:set, dst_path:str)->None:
    for username in usernames:
        to_path = os.path.join(dst_path, f"start_monitoring_system.bat({username}).bat")
        
        with open(fr"{to_path}", "w", encoding="ansi") as bat:
            bat.write(fr"E:\自動執行程式\Python\EXE\FileMonitoringSystem.exe -p E:\自動執行程式\Python\ProjectSettingInfo.xlsx -s ProjectSettingInfo -m E:\MAIL\{username}\Auto")


excel_data = load_excel_data(
    r"D:\CODE\NEW\FileMonitoringSystem-main\Setting\ProjectSettingInfo新架構.xlsx",
    "ProjectSettingInfo", False
)


usernames = excel_data.find_element_by_position("作業人員")

create_bat(usernames=usernames["作業人員"], dst_path= r"E:\自動執行程式\Python\bat")