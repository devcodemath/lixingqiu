"""批量调整图像文件大小.py,本程序需要安装pillow模块,安装方法如下:
pip3 install pillow """

import os
from PIL import Image

def 调整大小(image,newsize,outfilename):
    """image是打开的图形对象,newsize是宽高元组"""
    print(newsize)
    im = image.resize(newsize)          # 用图形对象的resize方法调整文件大小
    im.save(outfilename)                # 保存这个文件
    im.close()

folder = os.getcwd()  + os.sep + "images"
for file in os.listdir(folder):
    filename = folder + os.sep + file   # 文件夹加上分隔符加上文件名 
    im = Image.open(filename)           # 打开文件,返回im
    ratio = im.height/im.width          # 高度和宽高的比值
    new_width = 100                     # 新的宽度
    new_height = int(new_width * ratio) # 新的高度
    outfilename = folder + os.sep + str(new_width) + "x" + str(new_height) + "_" + file
    调整大小(im,(new_width,new_height),outfilename)
