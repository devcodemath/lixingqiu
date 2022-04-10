"""
   小红伞.py
"""
import turtle

def draw_pattern():
    """
       画填充圆弧
    """
    turtle.begin_fill()       # 开始填充
    turtle.fd(100)            # 前进100个单位
    turtle.left(120)          # 左转120度
    turtle.circle(60,120)     # 画半径为60度数为120的圆弧
    turtle.end_fill()         # 结束填充  
    turtle.left(120)          # 左转120度

turtle.width(2)               # 设定画笔宽度为2
turtle.speed(1)               # 设定移动速度为1
turtle.color('red')           # 设定颜色为红色
draw_pattern()                # 画填充圆弧
turtle.fd(50)                 # 前进50个单位
turtle.right(90)              # 右转90度 
turtle.fd(100)                # 前进100个单位
turtle.circle(7,180)          # 画半圆
turtle.ht()                   # 隐藏海龟
turtle.done()                 # 事件循环 
