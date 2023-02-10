import shutil
import os

src_path = r"D:\CODE\test.jpg"
dst_path = r"D:\CODE\new folder\test1.jpg"

if not os.path.exists(dst_path):
    result = shutil.copy2(src_path, dst_path)

    os.startfile(result)