"""
   虫子的柱状图,本程序体验列表推式，顺便了解下draw_rect命令。
   列表推导式是用for循环生成一个列表的语法糖(技巧)。
"""
from sprites import *                     # 从精灵模块导入所有命令
from random import randint                # 从随机模块导入randint命令 

screen = Screen()                         # 新建屏幕
screen.setup(800,600)                     # 设定宽高

datas=[randint(20,300) for x in range(30)]# 生成30个从20到300的整数

bug = Sprite()                            # 新建角色 
bug.goto(-280,-100)                       # 定位到坐标(-280,-100)

for height in datas:             # 把datas列表中的每个数据赋值给height
    bug.randomcolor()            # 随机设定颜色
    bug.pencolor('black')        # 设定画笔颜色为黑 
    bug.draw_rect(20,height)     # 画宽度为20,高度为height的矩形
    bug.fd(20)                   # 虫子前进20个单位

screen.mainloop()                # 进入主循环 
