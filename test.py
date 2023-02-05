'''
1. 假設folder進來

'''

def to_same_path(path):
    import os
    return os.path.abspath(path)


monitoring_paths: list = ["D:\\ABC\\123", "D:\\ABC\\456", "D:\\ABC\\789"]
insert_fullpaths: list = ["D:\\ABC\\123\\123.txt", "D:\\ABC\\123\\456\\789.zip"]

monitoring_paths = list(map(to_same_path, monitoring_paths))
insert_fullpaths = list(map(to_same_path, insert_fullpaths))

for insert_path in insert_fullpaths:
    print(insert_path)
    
for monitor_path in monitoring_paths:
    print(monitor_path)
    
print("######################")
    
for insert_fullpath in insert_fullpaths:
    # print(insert_fullpath)
    for monitoring_path in monitoring_paths:
        # print(monitoring_path)
        if monitoring_path not in insert_fullpath:
            print(f"{monitoring_path} to {insert_fullpath} is not match")
        else:
            # do_something
            print(f"{monitoring_path} to {insert_fullpath} is match")
            
        
