"""
   晃悠悠的海龟.py
"""
import time                     # 导入时间模块
import math                     # 导入数学模块
import turtle                   # 导入海龟模块

turtle.delay(0)                 # 设定绘画延时为0毫秒
turtle.speed(0)                 # 设定动作速度为最快
turtle.setup(480,360)           # 设定窗口大小
turtle.color('yellow')          # 设定海龟颜色
turtle.bgcolor('black')         # 设定背景色为黑 
turtle.shape('turtle')          # 设定造型为turtle
turtle.shapesize(5)             # 造型缩放 
turtle.penup()                  # 抬笔
turtle.left(90)                 # 海龟左转90度 

while 1:
    for angle in range(360):
        r = math.radians(angle) # 角度转换成弧度值
        h = 100 *  math.sin(r)  # 算出正弦值乘以100
        turtle.setx(h)          # 把h设为海龟的x坐标
        time.sleep(0.01)
