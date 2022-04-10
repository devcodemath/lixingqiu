"""
   动画原理.py
   本程序描述了在Python海龟画图中动画原理。
"""
import time                      # 导入时间模块
import turtle                    # 导入海龟模块

turtle.tracer(0,0)               # 关闭自动刷新，设定绘画延时为0毫秒
turtle.speed(0)                  # 让海龟的动作最快
turtle.hideturtle()              # 隐藏海龟
turtle.penup()                   # 抬笔
turtle.bk(200)                   # 倒退200 

turtle.pensize(2)                # 画笔粗细为2
turtle.pendown()                 # 落笔

while True:
    turtle.clear()               # 清除以前所画

    # 下面是重新绘制正方形
    for _ in range(4):
        turtle.fd(100)
        turtle.rt(90)

    turtle.update()              # 刷新显示
    time.sleep(0.01)
    turtle.fd(1)                 # 前进1个单位   
