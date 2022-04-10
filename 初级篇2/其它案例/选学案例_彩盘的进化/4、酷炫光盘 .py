"""酷炫光盘,请把coloradd.py放在和本程序同一个文件夹"""

from turtle import *
from coloradd import *

t = Turtle()
t.penup()
t.pensize(5)
t.screen.colormode(255)
t.screen.delay(0)
t.screen.bgcolor("black")
t.screen.title("酷炫光盘")
color=(255,0,0)
for i in range(360):
    t.pencolor(color)
    t.fd(50)
    t.pendown()
    t.fd(150)
    t.penup()
    t.bk(200)
    t.right(1)
    color = addcolor(color,0.01)
t.screen.exitonclick()
    
