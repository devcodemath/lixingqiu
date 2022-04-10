"""递归画正方形.py"""
from turtle import *

t= Turtle()
t.screen.delay(50)
t.speed(8)
t.pensize(4)

def draw_square(g,bc):
    """g代表海龟，bc代表边长"""
    for i in range(4):
       if bc > 50:             # 如果边长大于50
           draw_square(g,bc/4) # 画一个边长/4的正方形
       g.fd(bc)                # 画完后继续前进
       g.right(90)             # 右转90度
       
draw_square(t,100)
    
