"""
   海龟螺旋图.py
  
"""
import turtle
from random import randint

screen = turtle.getscreen()
screen.bgcolor('light cyan')
screen.colormode(255)             # 颜色模式为255
screen.delay(20)                  # 绘画延时为20毫秒
screen.title('海龟螺旋图')        # 设定窗口标题

turtle.penup()                    # 抬笔
turtle.speed(1)                   # 移动速度为最慢
turtle.shape('turtle')            # 设定造型为turtle
turtle.shapesize(0.5)             # 缩小
d = 10
for _ in range(50):
    turtle.stamp()                # 盖章
    turtle.fd(d)                  # 前进
    turtle.right(20)              # 右转20度 
    d = d + 1
    # 下面改变海龟的颜色
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    turtle.color('black',(r,g,b)) # 设定画笔和填充颜色
turtle.done()
