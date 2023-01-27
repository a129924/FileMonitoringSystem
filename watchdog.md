---
title: WatchDog筆記
Date: 2023/01/22
---

# 檔案動作
預設 監控資料夾:list = [r"D:\TEST\UserProfile", r"D:\TEST\ProjectFolder"]
如果檔案從D:\TEST 這邊 會觸發 on_modified() 要注意 
## on_moved(self, event)
從沒有被監控的資料夾中`複製貼上` `剪下貼上`檔案會觸發


## on_created(self, event)
如果該檔沒有在被監控的資料夾 或者是上一層 則會觸發


## on_deleted(self, event)
如果檔案被`剪下貼上`或者是`刪除` 會觸發


## on_modified(self, event)
如果檔案從未被監控的資料夾中`複製貼上` 就會持續觸發 到移動完畢為止

# 觸發順序

## 複製貼上
on_created -> on_modified 

## 剪下貼上
on_moved -> on_modified

## 刪除
on_deleted -> on_modified