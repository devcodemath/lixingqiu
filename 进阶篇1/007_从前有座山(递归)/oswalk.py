"""oswalk.py，本程序遍历某路径下面所有的文件名称"""

import os

def walk(path):
    """递归遍历路径，打印所有文件的全路径名"""
    for dirpath,dirnames,filenames in os.walk(path):
        for name in filenames:
            f = os.path.join(dirpath, name)
            print(f)
            
path = "C:\\ffmpeg"
walk(path)
