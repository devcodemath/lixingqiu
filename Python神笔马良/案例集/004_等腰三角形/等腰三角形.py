"""
   等腰三角形.py
"""
import turtle

angle = 70               # 底角
length = 200             # 定义等腰三角形腰长 
turtle.speed(1)          # 设定移动速度为最慢
turtle.pensize(2)        # 画笔粗细

turtle.left(angle)       # 左转
turtle.fd(length)        # 前进
turtle.right(2*angle)    # 右转
turtle.fd(length)        # 前进 

turtle.home()            # 回家
turtle.hideturtle()      # 隐藏海龟
turtle.done()            # 进入事件循环 
