import os
import argparse

from typing import List

from ProjectInfo import ProjectFileInfo
from ZipUtility import ZipCreator


class FilesZiper(ZipCreator):
    def __init__(self, project_info_path:str, zip_driver: str) -> None:
        self.project_info_data = ProjectFileInfo(project_info_path).zip_file
        zip_filename = self.project_info_data["zipFileName"]
        password = self.project_info_data["password"]
        to_path = self.project_info_data["toPath"]
        super().__init__(zip_filename, password, to_path, zip_driver)

    @property
    def ok_extension_amount(self)->int:
        return len(tuple(filter(lambda file: file.endswith(".ok"), os.listdir(os.path.join(self.to_path, "批次檔")))))

    @staticmethod
    def is_match_regex_file(file:str, regex_strings:list)->bool:
        import re
        for regex in regex_strings:
            if re.match(fr"{regex}", file):
                return True
        return False

    def zip_files(self):
        files = []
        print(self.ok_extension_amount)
        regex_strings = self.project_info_data["files"]
        if self.ok_extension_amount == int(self.project_info_data["okAmount"]):
            search_files:List[str] = os.listdir(self.to_path)
            for search_file in search_files:
                if self.is_match_regex_file(search_file, regex_strings):
                        files.append(search_file)

            self.compress_files(self.to_path, files)
            return files 

        else:
            return "OK檔案數量不符"


if __name__ == "__main__":
    cmd_parser = argparse.ArgumentParser(description="壓縮檔整合程式")
    cmd_parser.add_argument("-setting_path", "--json_setting_path", type=str, help="專案設定JSON檔完整路徑")
    cmd_parser.add_argument("-d", "--zip_driver", type=str ,help="7z檔案路徑")
    args = cmd_parser.parse_args()



    my_zip_maker = FilesZiper(fr"{args.json_setting_path}", fr"{args.zip_driver}").zip_files()

    # print(my_zip_maker.zip_files())