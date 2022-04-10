"""
  爆炸图.py
"""
import turtle
import random

def scatter(c,length):
    """
       散射条函数
       这个函数会设定画颜色，然后根据length
       来决定需要前进的距离。
    """
    turtle.color(c)
    turtle.pensize(length)
    for _ in range(150):
        d = length * random.randint(50,120)
        f = random.randint(1,360)
        turtle.seth(f)                    # 设置方向为f 
        turtle.fd(d)
        turtle.goto(0,0)                  # 回到原点
   
turtle.bgcolor('black')                   # 设定背景颜色为黑
turtle.delay(0)                           # 设定绘画延时为0
turtle.speed(0)                           # 设定移动速度为最快
turtle.pensize(4)                         # 设定画笔粗细为4
    
scatter('blue',4)                         # 调用函数画蓝线条 
scatter('purple',3)
scatter('red',2)
scatter('yellow',1)                       # 调用函数画黄线条 

turtle.done()                             # 进入事件循环

