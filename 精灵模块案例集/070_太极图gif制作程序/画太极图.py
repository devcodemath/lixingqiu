"""
   太极图gif制作演示程序
"""
from sprites import *

def draw_circle(tom,x,y,radius,degrees):
    """
       tom：精灵对象
       x,y：圆的中心点
       radius：半径
       degrees: 度数
    """
    tom.goto(x,y)
    tom.fd(radius)
    tom.left(90)
    tom.pendown()
    tom.begin_fill()
    tom.circle(radius,degrees)
    tom.end_fill()
    tom.penup()
    tom.right(90)
    tom.bk(radius)
    
screen = Screen()
screen.delay(10)
s = Sprite()
s.speed(8)

s.setheading(90)
draw_circle(s,0,0,150,180)
s.color('black','white')
draw_circle(s,0,0,150,180)

s.color('white')
draw_circle(s,0,-75,75,180)

s.color('black')
draw_circle(s,0,75,75,180)

s.color('white')
draw_circle(s,0,75,25,360)

s.color('black')
draw_circle(s,0,-75,25,360)

s.hide()

