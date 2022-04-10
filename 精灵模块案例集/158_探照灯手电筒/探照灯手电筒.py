"""
   探照灯手电筒.py
"""

from sprites import *            # 从精灵模块导入所有命令

screen = Screen()                # 新建屏幕对象
screen.bgcolor('black')          # 设定背景为黑色 
screen.setup(474,387)            # 设定屏幕分辨率

# 注意以下是先生成角色再增加背景,边界问题请自行添加判断代码解决

flashlight = Sprite(shape='flashlight2.png')
screen.bgpic('王子公主.jpg')

while 1:
    flashlight.goto(mouse_pos())
    screen.update()
