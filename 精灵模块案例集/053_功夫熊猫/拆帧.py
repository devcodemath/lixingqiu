"""
   拆帧,首先要安装pillow模块,安装方法:
   pip install pillow
"""
from PIL import Image,ImageSequence

im = Image.open('tenor.gif')   # 打开gif文件

index = 0
# 迭代图形对象中的每一帧
for f in ImageSequence.Iterator(im):  
    #  保存此帧到images文件夹
    f.save('frames/' + str(index) + '.png')
    index = index + 1
 
