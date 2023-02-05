import re
from datetime import datetime

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
        if self.is_have_comma_string(string):
            strings = self.have_comma_string_to_list(string)

            return list(map(ComplexString, strings))
        else:
            return ComplexString(string)

class ComplexString(str):
    def __init__(self, string:str):
        self.string = string
        
        self.string = self.date_format()
        self.string = self.regex_format()

        self.result = self.string
        
    @property
    def regex_convert(self)->dict:
        # return {
        #     "*": '[.\\w\\d\\S]+\\',
        # }        
        return {
            "*": '.*\\',
        }
    
    # 主要字串輸出    
    def __str__(self):
        return self.result
    
    def __repr__(self):
        return self.result
   
    def date_format(self):
        # 找到<>中的字串
        date_format = re.search(r'<(.*?)>', self.string)
        if date_format:
            date_format = date_format.group(1)
            data_format_regex:str = re.findall(r"<.*>", self.string)[0]
            
            # 依照字串裡面的格式轉換
            if 'HH' in date_format:
                date_format = date_format.replace('HH', '%H')
            if 'MM' in date_format:
                date_format = date_format.replace('MM', '%m')
            if 'DD' in date_format:
                date_format = date_format.replace('DD', '%d')
            
            # 輸出日期格式
            return self.string.replace(data_format_regex, datetime.now().strftime(date_format))
        
        return self.string
    
    def regex_format(self):
        if "*" in self.string:
            return self.string.replace("*", self.regex_convert["*"])
        
        return self.string
    
if __name__ == "__main__":
    # contension_string = "FuturesDay_2*.zip"
    contension_string = "IAN1<MMDD>*.zip"
    contension_strings:list = ["FuturesDay_2*.zip",
                        "FuturesDay_3*.zip", "FuturesDay_3*asd.msg", "FuturesDay_4*<MMDD>ABCDE.zip", "IAN1<MMDD>*.zip", "IANA<MMDD>*.zip,IANA<MMDD>*.msg"
                        ,"IAN1<MMDD>*.zip"]
    def now():return time.time()
    start = now()
    new_strings: list = CheckCommaList(contension_strings)
    print((now() - start)*1000)
    print(new_strings)

