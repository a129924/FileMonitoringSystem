import os

paths = {'D:\\TEST\\UserProfile\\Auto\\ProjectFolder\\TEST1.zip': 1073741824,
         'D:\\TEST\\UserProfile\\TEST1.zip': 1073741824}


data = {
    'E:\\Mail\\Jitingtsai\\Auto\\FuturesDay': 
        {
            '案件代碼': 'FuturesDay', 
            '品名': '永豐金證[紙本] 期貨日對帳單', 
            '作業人員': 'Jitingtsai', 
            '正式檔下載檔名': 'FuturesDay_2*.zip', 
            '作業目錄': 'E:\\DATA\\CHSTOT\\YFT\\<YYYYMMDD>-FuturesDay', 
            '案件主程式名稱(Excel)': 'E:\\DATA\\CHSTOT\\YFT\\FuturesDay-<YYYYMMDD>.xls'
            },
         
    'E:\\Mail\\Jitingtsai\\Auto\\OverSeasFutureDay': 
        {
            '案件代碼': 'OverSeasFutureDay', 
            '品名': '永豐金證[紙本] 國外期貨日對帳單', 
            '作業人員': 'Jitingtsai', 
            '正式檔下載檔名': 'OverSeasFutureDay_2*.zip', 
            '作業目錄': 'E:\\DATA\\CHSTOT\\OSFD\\<YYYYMMDD-1,2>',
            '案件主程式名稱(Excel)': 'E:\\DATA\\CHSTOT\\OSFD\\OverSeasFutureDay-<YYYYMMDD-1,2>.xls'
            },
        
    'E:\\MAIL\\Andrew\\Auto\\安聯人壽－每日補單': 
        {
            '案件代碼': 'IAN1', 
            '品名': '安聯人壽-每日PDF檔', 
            '作業人員': 'AndrewJiang', 
            '正式檔下載檔名': '*.zip,*.msg', 
            '作業目錄': 'E:\\DATA\\IAN\\IAN1\\<MMDD>', 
            '案件主程式名稱(Excel)': 'E:\\DATA\\IAN\\IAN1\\<MMDD>\\main_每日.xlsm'
            },
    'D:\\TEST\\UserProfile\\Auto\\ProjectFolder':
        {
            '案件代碼': 'TEST1',
            '品名': '測試一',
            '作業人員': 'AndrewJiang',
            '正式檔下載檔名': '*.zip,*.msg',
            '作業目錄': 'E:\\DATA\\IAN\\IAN1\\<MMDD>',
            '案件主程式名稱(Excel)': 'E:\\DATA\\IAN\\IAN1\\<MMDD>\\main_每日.xlsm'
        }
        } 

work_folder_paths = list(map(os.path.dirname, paths.keys()))


# print(work_folder_paths) # ['D:\\TEST\\UserProfile\\Auto\\ProjectFolder', 'D:\\TEST\\UserProfile']

match_folders = [
    work_folder_path for work_folder_path in work_folder_paths if work_folder_path in data.keys()]
print(match_folders) # ['D:\\TEST\\UserProfile\\Auto\\ProjectFolder']


data1 = {
    '品名': '安聯人壽-每日PDF檔', 
    '作業人員': 'Andrew', 
    '正式檔下載檔名': '*.zip,*.msg,*.pdf', 
    '目的路徑': 'E:\\MAIL\\Andrew\\Auto\\安聯人壽－每日補單', 
    '作業目錄': 'E:\\DATA\\IAN\\IAN1\\<MMDD>TST', 
    '案件主程式名稱(Excel)': 'E:\\DATA\\IAN\\IAN1\\<MMDD>\\main_每日.xlsm', 
    '專案來檔壓縮密碼': 89283591, 
    '專案來檔是否直接放到路徑': False, 
    '壓縮檔是否直接解壓縮到路徑': False, 
    '來檔壓縮檔特殊處裡': 'MoveSameFileByFolder', 
    'VBA主程式路徑': 'E:\\DATA\\IAN\\IAN1\\back\\main_每日.xlsm', 
    'VBA主程式放置路徑': 'E:\\DATA\\IAN\\IAN1\\<MMDD>', 
    '回檔壓縮檔名稱': '<MMDD>IAN1TST每日(安聯人壽-收費科).zip', 
    '回檔壓縮檔密碼': 8482, 
    '需回傅檔列表': None, 
    'OK檔路徑': None, 
    'OK檔數量': None, 
    '上機檔案': None, 
    '上機檔案路徑': None}