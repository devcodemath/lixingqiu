"""
   gif动图制作.py
   本程序演示了如何把虫子画图形的过程保存为gif动图。
   注意在本程序中使用了pillow模块的Image类。
   这是由于sprites模块已经给导入了。
   本程序用到了Python精灵模块，可以用下面命令在cmd窗口中快速安装。
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sprites  --upgrade
"""
import os
from sprites import *

frames = []                              # im帧列表，以便保存所有截的图形

screen = Screen()                        # 新建屏幕 
bug = Sprite()                           # 新建角色 
bug.color('red')                         # 画笔为红
bug.pensize(10)                          # 画笔粗细为10
bug.pendown()

# 下面是画图形，这里只是简单画一个红色的图，你可以修改为画其它图形，
# 每移动或旋转了角色，都可以保存当前的屏幕到frames列表。
for x in range(8):                       # 在范围8迭代x 
    for y in range(4):                   # 在范围4迭代y
        bug.fd(100)                      # bug前进100个单位
        frames.append(screen.save())     # 添加截屏为帧到列表中
        bug.rt(90)                       # 右转90度
        frames.append(screen.save())     # 添加截屏为帧到列表中
    bug.rt(45)                           # 右转45度  
    frames.append(screen.save())         # 添加截屏为帧到列表中
size = frames[0].size                    # 图像尺寸
print(size)

im = frames[0]                           # 第一帧
im.save('out.gif', save_all=True, append_images=frames[1:],
        optimize=False, duration=200, loop=0)

# 如果像下面这样，那么第一帧就是白色的。
#im = Image.new("RGBA",size,color=(255,255,255,0))  # 新建im图像对象  
#im.save('out.gif', save_all=True, append_images=frames)

screen.mainloop()
