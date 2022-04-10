"""
   反弹原理_简.py
"""
import time
import turtle

width,height = 480,360
screen = turtle.getscreen()   # 获取屏幕
screen.setup(width,height)

turtle.speed(0)
turtle.penup()
turtle.shape('circle')

dx = 2                                # 水平速度
dy = 2                                # 垂直速度 

while True:
    x = turtle.xcor() + dx            # 水平坐标增加dx
    y = turtle.ycor() + dy            # 垂直坐标增加dy
    turtle.goto(x,y)                  # 到达x,y
    if x >= 240 or x <=-240:dx = -dx  # 如果到达了左右边界，dx取反
    if y >= 180 or y <=-180:dy = -dy  # 如果到达了上下边界，dy取反
    time.sleep(0.01) 
    
