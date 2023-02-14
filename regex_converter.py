import re
import os 
from datetime import datetime
from typing import Any, List

import time
# TODO 正則要改成符合符號 ["&", "!", "#", "%", "^", "-", "=",]

class CheckCommaList(list):
    def __init__(self,iterator:list):
        super(CheckCommaList, self).__init__(map(self.main, iterator))

    @staticmethod
    def have_comma_string_to_list(string:str)->list:return string.split(",")

    @staticmethod
    def is_have_comma_string(string:str)->bool:return "," in string
    
    def main(self,string:str):
        '''
        強制把含有逗號的字串 轉換成list 
        並把LIST中每個字串 轉換成ComplexString型態 
        '''
        if isinstance(string, str):
            if self.is_have_comma_string(string):
                strings = self.have_comma_string_to_list(string)
                new_strings = []
                for string in strings:
                    new_strings.append(fr"{ComplexString(string).complex_str()}")

                return new_strings
            else:
                return ComplexString(string).complex_str()
                
        elif isinstance(string, list) and isinstance(string[0], str):
            new_strings = []
            for str_ in string:  # type: ignore
                new_strings.append(fr"{ComplexString(str_).complex_str()}")

            return fr"{new_strings}"
        else:
            return string

class ComplexString(str):
    # def __init__(self, string:str, format_type="str"):
    #     self.string = string
    #     self.format_type = format_type
        
    #     self.date_format()
    #     self.string = self.regex_format()
    def __new__(cls, variable:Any):
        if isinstance(variable, str):
            return str.__new__(cls, variable)
        else:
            return variable

        
    @property
    def regex_convert(self)->dict:
        return {
            "*": '.+',
        }
    
    # 主要字串輸出    
    def __str__(self):
        return self
    
    def __repr__(self):
        return self

    def complex_str(self):
        string = ComplexString(self.regex_format()).date_format()

        return fr"{string}"
   
    def date_format(self)->str:
        # 找到<>中的字串
        # 因應json format為str型態 會有多個<MMDD>或者是<HHMMDD> 所以需要改成finall for 逐一取代
        date_formats:List[str] = re.findall(r'<(.*?)>', self)
        if date_formats:
            # date_format = date_format.group(1)
            for date_format in date_formats:
            # 依照字串裡面的格式轉換
                data_format_regex:str = date_format
                if 'HH' in date_format:
                    date_format = date_format.replace('HH', '%H')
                if 'MM' in date_format:
                    date_format = date_format.replace('MM', '%m')
                if 'DD' in date_format:
                    date_format = date_format.replace('DD', '%d')
                self= self.replace(f"<{data_format_regex}>", datetime.now().strftime(date_format))
            # 輸出日期格式
            return self
        
        return self
    
    def regex_format(self):
        if "*" in self:
            replace_str = self.regex_convert["*"]

            return self.replace("*", replace_str)
        
        return self

    def have_XXXX(self,target:str)->str:
        if "╳╳╳╳" in self:
            return self.replace("╳╳╳╳", target)

        return self


    
if __name__ == "__main__":
    # contension_string = "FuturesDay_2*.zip"
    contension_string = "IAN1_<HHMMDD>_ABC_<MMDD>*.zip"
    contension_strings:list = ["FuturesDay_2*ZXC<MMDD>ABC<MMDD>.zip",
                        "FuturesDay_3*.zip", "FuturesDay_3*asd.msg", "FuturesDay_4*<MMDD>ABCDE.zip", "IAN1<MMDD>*.zip", "IANA<MMDD>*.zip,IANA<MMDD>*.msg"
                        ,"IAN1<MMDD>*.zip"]
    def now():return time.time()
    start = now()
    new_strings: list = CheckCommaList(contension_strings)
    new_string: str = ComplexString(contension_string).complex_str()  # type: ignore
    
    # def is_match_regex_file(file:str, regex_strings:list)->bool:
    #     import re
    #     for regex in regex_strings:
    #         # IAN10208.*\\.zip
    #         print(fr"{regex}")
    #         if re.match(fr"{regex}", file):
    #             return True
    #     return False

    # file = "IAN10208.zip"

    # print(is_match_regex_file("0206每日通知單.zip", [".*\\.zip"]))

    print((now() - start)*1000)
    # print(new_strings)
    print(new_strings)
    
    # print(list(map(os.path.abspath, new_strings)))

