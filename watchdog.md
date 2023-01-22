---
title: WatchDog筆記
Date: 2023/01/22
---

# 檔案動作
預設 監控資料夾:list = [r"D:\TEST\UserProfile", r"D:\TEST\ProjectFolder"]
如果檔案從D:\TEST 這邊 會觸發 on_modified() 要注意 
## on_moved(self, event)


## on_created(self, event)
如果該檔沒有在被監控的資料夾 或者是上一層 則會觸發


## on_deleted(self, event)
如果檔案被`剪下貼上`或者是`刪除` 會觸發


## on_modified(self, event)

