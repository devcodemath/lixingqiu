"""
   打点之斜正方.py
"""
import turtle
from random import randint

turtle.shape('circle')
turtle.shapesize(0.2)
turtle.colormode(255)             # 设定颜色模式为255
turtle.speed(0)                   # 设定移动速度最快
turtle.delay(0)                   # 设定绘画延时为0 
turtle.bgcolor('black')           # 设定背景色为黑   
turtle.penup()
while True:
    x = randint(-100,100)
    y = randint(-100,100)
    # 如果x和y的绝对值之和小于100
    if (abs(x)+abs(y))<100:
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        turtle.color(r,g,b)      # 设定颜色为r,g,b
        turtle.goto(x,y)         # 到达这个坐标  
        turtle.dot()             # 打点
