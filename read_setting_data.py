from ExcelDataParser import ExcelDataParser


setting_data = ExcelDataParser(
    r"D:\CODE\NEW\FileMonitoringSystem-main\Setting\ProjectSettingInfo新架構.xlsx",
    "檔案格式", is_convert = False)

data_ = setting_data.fillna(0, "first")

data_groupby = setting_data.groupby(0, data_)

print(data_groupby)