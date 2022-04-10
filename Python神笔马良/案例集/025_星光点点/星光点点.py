"""
   星光点点.py
"""
import random                    # 随机模块
import turtle                    # 海龟模块

turtle.ht()                      # 隐藏海龟
turtle.setup(480,360)            # 设置宽高  
turtle.bgcolor('black')          # 背景颜色
turtle.color('dark blue')        # 设定颜色 
turtle.delay(0)                  # 绘画延时
turtle.width(100)                # 画笔宽度
turtle.penup()                   # 抬起笔来
turtle.goto(-240,-150)           # 坐标定位 
turtle.pendown()                 # 落下画笔
turtle.setx(480)                 # 水平坐标
turtle.penup()                   # 抬起笔来
turtle.color('white')            # 画笔颜色 
for _ in range(30):              # 重复次数
    x = random.randint(-240,240) # x 随机数
    y = random.randint(-100,150) # y 随机数
    turtle.goto(x,y)             # 到达坐标
    turtle.dot(3)                # 画小圆点
turtle.done()                    # 事件循环
