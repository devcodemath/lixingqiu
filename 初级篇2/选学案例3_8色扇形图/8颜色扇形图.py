"""8颜色扇形图.py"""
from turtle import *

width,height = 480,360
colors = 'red','orange','yellow','green','cyan','blue','purple','magenta'

screen = Screen()          # 新建屏幕对象
screen.setup(width,height) # 设定屏幕的宽高

t = Turtle(visible=False)  # 新建不可见海龟对象
t.penup()                  # 抬笔

for i in range(8):         # 重复8次
    t.setheading(i*45)     # 设定起始方向
    t.color(colors[i])     # 设定画笔和填充颜色
    t.begin_fill()         # 开始填充
    t.fd(100)              # 前进100
    t.left(90)             # 左转90度
    t.circle(100,45)       # 画1/8的弧
    t.goto(0,0)            # 回到原点
    t.end_fill()           # 结束填充
    
screen.exitonclick()       # 单击屏幕关闭窗口
    
    
