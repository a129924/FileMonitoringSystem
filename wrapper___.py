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
