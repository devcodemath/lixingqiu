"""红太阳.py 本程序画一个红色的太阳"""

from turtle import *
from random import randint,choice

colorList = ["red","orange","yellow","green","cyan","blue","purple","magenta"]

t = Turtle()                 # 新建海龟对象
t.pencolor("red")            # 画笔颜色为红色
t.dot(100)                   # 打圆点
t.pensize(4)                 # 画笔宽为4
t.penup()                    # 抬笔

for i in range(10):
    t.color(choice(colorList))# 随机选择一种颜色
    t.fd(100)
    t.pendown()               # 落笔
    t.fd(100)                 # 前进,画线条
    t.penup()                 # 抬笔
    t.bk(200)                 # 退回原位
    t.right(36)               # 右转36度
t.screen.exitonclick()        # 单击关闭窗口
