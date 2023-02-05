import os

if os.path.exists(r"E:\DATA\IAN\IAN1\0202TST") is False:
    print(True)
    os.mkdir(r"E:\DATA\IAN\IAN1\0202TST")
else:
    print(False)