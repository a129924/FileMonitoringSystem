import os
from openpyxl import load_workbook, Workbook

from regex_converter import CheckCommaList

class ExcelDataParser():
    def __init__(self,file_path:str, sheet_name:str) -> None:
        assert os.path.splitext(file_path)[1] in [".xls", ".xlsx", ".csv"], "檔案副檔名錯誤" 
        self.file_path = file_path
        self.sheet_name = sheet_name

    @property
    def wb(self)->Workbook:
        return load_workbook(self.file_path)
    
    @property
    def sheet_names(self,)->list:
        return self.wb.sheetnames

    @property
    def data(self)->list:
        data = []

        for rows in self.wb[self.sheet_name]:
            data.append(CheckCommaList([row.value for row in rows]))

        return data

    @property
    def header(self)->list:
        return self.data[0]
    
    @property
    def body(self)->list:
        return self.data[1:]

    @property
    def dataframe(self,)->list:
        return [dict(zip(self.data[0], row)) for row in self.data[1:]]

    @staticmethod
    def reset_index(dataframe:list, index:str)->dict:
        assert index in dataframe[0].keys(), "Key不存在"
        reset_index_data = {}
        for row in dataframe:
            new_index = row[index]
            del row[index]
            reset_index_data[new_index] = row

        return reset_index_data


if "__main__" == __name__:
    data = ExcelDataParser(
        r"D:\code\python\FileMonitoringSystem\Setting\ProjectSettingInfo.xlsx", "ProjectSettingInfo")
    # print(data.header)
    # print(data.body)
    # print(data.dataframe)
    import re
    new_data = data.reset_index(data.dataframe, "目的路徑")
    files = ["123.zip", "ABC.msg", "ABCD.bat", "1234.zip"]
    contensions = new_data["E:\MAIL\Andrew\Auto\安聯人壽－每日補單"]["正式檔下載檔名"]
    def is_match_regex_file(file: str, regex_strings: list) -> bool:
        import re
        for regex in regex_strings:
            if re.match(fr"{regex}", file):
                return True
        return False
    
    print(is_match_regex_file(files[0], contensions))
    # # 利用正則表達式篩選出符合的檔案(字串)
    # contensions = new_data["E:\MAIL\Andrew\Auto\安聯人壽－每日補單"]["正式檔下載檔名"]
    # matching_files = []
    # for file in files:
    #     for contension in contensions:
    #         if re.match(fr"{contension}", file):
    #             matching_files.append(file)
    #             break

