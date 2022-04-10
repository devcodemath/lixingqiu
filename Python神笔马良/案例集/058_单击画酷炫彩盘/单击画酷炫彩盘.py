"""
   单击画酷炫彩盘.py
  
"""

from turtle import Turtle              # 导入海龟类
from random import randint
from coloradd import * 

def draw(x,y):
    """画一个彩色的圆圈"""
    global color
    t.goto(x,y)
    t.pendown()
    t.screen.tracer(0)                  # 关闭自动刷新          
    for i in range(1,randint(10,50)):        
        t.pencolor(color)               # 设定画笔颜色
        t.circle(i,180)                 # 画半圆，半径为i
        color = coloradd(color,0.01)    # 颜色增加
    t.screen.update()                   # 刷新屏幕
    t.penup()
    
color = (255,0,0)                       # RGB红色元组

t = Turtle(visible=False)               # 新建海龟

t.screen.title('风火轮编程')            # 写上窗口标题
t.screen.setup(800,600)                 # 设定窗口大小
t.screen.bgcolor('black')               # 背景颜色为黑
t.screen.colormode(255)                 # 颜色模式为RGB255 

t.pensize(4)                            # 画笔的笔迹大小为4
t.screen.onclick(draw)
t.screen.mainloop()
