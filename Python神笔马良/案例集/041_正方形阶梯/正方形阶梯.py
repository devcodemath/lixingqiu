"""
   正方形阶梯.py
"""
import turtle

def draw_square(length):
    for _ in range(6):
        turtle.fd(length)
        turtle.right(90)
    turtle.right(90)        # 右转，变成向上了
    turtle.fd(length/2)     # 前进1半的距离
    turtle.right(90)        # 右转，变成向右了

turtle.pensize(2)           # 设定画笔粗细
d = 100
for _ in range(4):          # 重复4次
    draw_square(d)          # 调用draw_square函数
    d = d / 2

turtle.hideturtle()         # 隐藏海龟
turtle.done()               # 事件循环

    
