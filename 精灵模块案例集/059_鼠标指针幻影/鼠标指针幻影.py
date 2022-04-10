"""
   鼠标指针幻影效果,用Python的精灵模块非常简单的现实这种跟随鼠标指针效果。
   其主要原理是就利用盖图章命令，让图章在一定时间内自动消失。

"""
from sprites import *

screen = Screen()
screen.bgcolor('black')
screen.bgpic('bg.png')

c = Sprite('circle.png')  # 新建c角色
c.setalpha(128)           # 设为半透明

clock = Clock()           # 新建时钟对象
while True:
    c.goto(mouse_pos())
    item = c.stamp(0.6)       # 盖0.6秒后消失的图章    
    clock.tick(60)
