"""
   打点法画圆球.py
"""
import turtle
import random

turtle.delay(0)                  # 设定绘画延时为0毫秒 
turtle.speed(0)                  # 设定移动速度为最快
turtle.penup()                   # 抬笔
turtle.color('blue')             # 设定颜色为蓝色
turtle.bgcolor('light cyan')     # 设定背景颜色为淡青色

while True:                      # 重复执行 
    angle = random.randint(1,360)# 产生1到360范围内的值
    turtle.seth(angle)           # 设定方向为angle
    d = random.randint(1,200)    # 产生1到200范围内的值
    turtle.fd(d)                 # 朝其方向前进d 
    turtle.dot(2)                # 打点
    turtle.home()                # 回家
