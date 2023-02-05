# import time

# now = lambda :time.time()

# start = now()
# src_path = r".\Auto\ProjectFoldddder1\folder\XXX.YYY"
# check_filepaths:list = [r".\Auto\ProjectFolder1", r".\Auto\ProjectFolder2", r".\Auto\ProjectFolder3"] * 1000
# create_same_len_src_paths = [src_path] * len(check_filepaths) * 1000

# def is_in_more_folder_need_move_file(src_path:str, check_filepath:str)->bool:
#     '''
#     src_filepath: 
#     '''
#     return check_filepath in src_path
# # map(function , function_arg1, function_arg2, ...)
# print(any(map(is_in_more_folder_need_move_file, create_same_len_src_paths, check_filepaths)))

# print(f"{(now() - start) * 1000}")

for i in range(1,10):
    if i == 2:
        continue
    print(i)