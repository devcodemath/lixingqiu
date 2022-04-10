"""批量复制.py"""

import os

def copyfile(src,dst):
    f = open(src,mode='rb')
    fc = f.read()
    f.close()
    f = open(dst,mode='wb')
    f.write(fc)
    f.close()
    
path1 = os.getcwd() + os.sep + "测试文件夹"
path2 = os.getcwd() + os.sep + "test"
if not os.path.exists(path2):
    os.mkdir(path2)

for file in os.listdir(path1):
    srcfile = path1 + os.sep + file
    dstfile = path2 + os.sep + file
    copyfile(srcfile,dstfile) 
