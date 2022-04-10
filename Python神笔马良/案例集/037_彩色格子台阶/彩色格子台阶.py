"""
   彩色格子台阶.py
"""
import turtle
from random import random

turtle.speed(0)
turtle.penup()                    # 抬笔
turtle.goto(-200,250)             # 坐标定位
turtle.delay(0)                   # 延时为0毫秒 
turtle.pendown()                  # 落笔

for x in range(1,11):
    
    for y in range(x):
        r = random()              # 产生0到1之间的小数
        g = random()
        b = random()
        turtle.fillcolor(r,g,b)   # 设定填充颜色
        
        turtle.begin_fill()       # 开始填充
        for _ in range(4):
            turtle.fd(50)
            turtle.rt(90)
        turtle.end_fill()         # 结束填充
        
        turtle.fd(50)
        
    turtle.bk(50* x )             # 倒退
    y = turtle.ycor() - 50        # 把海龟的y坐标减50
    turtle.sety(y)                # 设定海龟的y坐标
turtle.done()
