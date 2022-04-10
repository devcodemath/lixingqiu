"""在鼠标单击处画一圈圈的圆.py ,单击鼠标左键后会在单击处画圆圈"""
from turtle import *

def draw_circle(x,y):
    """在鼠标单击处画圆"""
    t.penup()                    # 抬起笔来
    t.goto(x,y)                  # 定位到圆心
    for radius in range(10,100,10):
        t.fd(radius)             # 前进radius
        t.left(90)               # 左转90度
        t.pendown()              # 落下画笔
        t.circle(radius)         # 画个圆圈
        t.penup()                # 抬起笔来
        t.right(90)              # 右转90度
        t.bk(radius)             # 倒退radius
 
screen = Screen()                # 新建屏幕
screen.title("在鼠标单击处画一圈圈的圆")
screen.delay(0)                  # 屏幕延时

t = Turtle()                     # 新建海龟
screen.onclick(draw_circle)
screen.mainloop()                # 屏幕主循环
