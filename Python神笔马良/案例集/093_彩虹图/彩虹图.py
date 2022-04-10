"""
   彩虹图.py
"""
import turtle

def draw_semi_circle(radius):
    """画半圆函数"""
    turtle.penup()
    turtle.fd(radius)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(radius,180)
    turtle.penup()
    turtle.left(90)
    turtle.fd(radius)
    
cs = 'red','orange','yellow','green','cyan','blue','purple'

w = 22
turtle.pensize(w)
for c in range(7):
    r = 20 + c * 20        # 设定半径
    turtle.color(cs[c])    # 设定颜色
    draw_semi_circle(r)    # 画半圆
    
turtle.ht()
turtle.done()
