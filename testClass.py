import os
import re
import time
from datetime import datetime

class MyString(str):
    def __new__(cls, string):
        return str.__new__(cls, string)
    def add(self,value):
        return MyString(self + value)

    def plus(self, value, num):
        return MyString(self + value * num)
    
    def __repr__(self):
        return f"__str__ : {self}"
    
    


# TODO 正則要改成符合符號 ["&", "!", "#", "%", "^", "-", "=",]


class CheckCommaList(list):
    def __init__(self, iterator: list):
        super(CheckCommaList, self).__init__(map(self.main, iterator))

    @staticmethod
    def have_comma_string_to_list(
        string: str) -> list: return string.split(",")

    @staticmethod
    def is_have_comma_string(string: str) -> bool: return "," in string

    def main(self, string: str):
        '''
        強制把含有逗號的字串 轉換成list 
        並把LIST中每個字串 轉換成ComplexString型態 
        '''
        if self.is_have_comma_string(string):
            strings = self.have_comma_string_to_list(string)

            return list(map(ComplexString, strings))
        else:
            return ComplexString(string)


class ComplexString(str):
    def __new__(cls, string):
        return str.__new__(cls, string)
    
    @property
    def regex_convert(self) -> dict:
        # return {
        #     "*": '[.\\w\\d\\S]+\\',
        # }
        return {
            "*": r'.*\\',
        }

    # 主要print字串輸出
    def __str__(self):
        return self.complax_string()

    def __repr__(self):
        return self.complax_string()
    
    def complax_string(self,):
        self = ComplexString(self.regex_format()).date_format()
        
        return self
    
    def date_format(self):
        # 找到<>中的字串
        date_format = re.search(r'<(.*?)>', self)
        if date_format:
            date_format = date_format.group(1)
            data_format_regex: str = re.findall(r"<.*>", self)[0]

            # 依照字串裡面的格式轉換
            if 'HH' in date_format:
                date_format = date_format.replace('HH', '%H')
            if 'MM' in date_format:
                date_format = date_format.replace('MM', '%m')
            if 'DD' in date_format:
                date_format = date_format.replace('DD', '%d')

            # 輸出日期格式
            return self.replace(data_format_regex, datetime.now().strftime(date_format))

        return self

    def regex_format(self):
        if "*" in self:
            return self.replace("*", self.regex_convert["*"])

        return self


if __name__ == "__main__":
    def is_match_regex_file(file: str, regex_strings: list) -> bool:
        import re
        for regex in regex_strings:
            if re.match(fr"{regex}", file):
                return True
        return False
    
    # # contension_string = "FuturesDay_2*.zip"
    # contension_string = "IAN1<MMDD>*.zip"
    contension_strings: list = ["FuturesDay_2*.zip",
                                "FuturesDay_3*.zip", "FuturesDay_3*asd.msg", "FuturesDay_4*<MMDD>ABCDE.zip", "IAN1<MMDD>*.zip", "IANA<MMDD>*.zip,IANA<MMDD>*.msg", "IAN1<MMDD>*.zip"]

    # def now(): return time.time()
    # start = now()
    new_strings: list = CheckCommaList(contension_strings)
    # new_string = ComplexString(contension_string)
    # print((now() - start)*1000)
    # # print(new_strings)
    print(new_strings)
    # # print(list(map(os.path.abspath, new_strings)))
    print(is_match_regex_file("FuturesDay_31asd.msg", new_strings))
