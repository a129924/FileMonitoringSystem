import argparse
import time

from typing import List , Dict, Any


class CmdParser(argparse.ArgumentParser):
    def __init__(self, description:str ,args_setting:List[Dict[str, Any]]):
        self.args_setting = args_setting
        self.description = description


    
    

        
def loop(num:int, wait_time:int = 1):
    num = int(num)
    wait_time = int(wait_time)
    
    while num < 100:
        time.sleep(wait_time)
        print(num)

        num += 1



if __name__ == "__main__":
    # num = sys.argv # $ py .\get_bat_variable.py 1 2 3
    # print(num) # ['.\\get_bat_variable.py', '1', '2', '3']
    cmd_parser = argparse.ArgumentParser(description="Example Command")
    cmd_parser.add_argument("-n", "--num", type=int, help="初始值", default= 1)
    cmd_parser.add_argument("-wait_time", type=int ,help=None, default=1)
    args = cmd_parser.parse_args()
    # loop(args.n, args.wait_time)
    print(args.wait_time)