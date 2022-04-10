"""
   天空之眼.py
"""
import math
import turtle

def draw_square(length,level):
    if level>0:
        for _ in range(4):
            turtle.fd(length)
            turtle.lt(90)
        b = length/2
        turtle.fd(b)            # 前进到边长的一半处
        d = math.sqrt(2*b*b)    # 计算出边长的值
        turtle.left(45)
        draw_square(d,level-1)  # 画边长为d的正方形

turtle.pensize(2)               # 画笔粗细
turtle.color('blue')            # 设定颜色
draw_square(200,8)              # 调用函数
turtle.ht()                     # 隐藏海龟 
turtle.done()                   # 事件循环
        
