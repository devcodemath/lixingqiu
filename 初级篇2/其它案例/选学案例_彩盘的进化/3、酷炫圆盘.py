"""酷炫圆盘,请把coloradd.py放在和本程序同一个文件夹"""

from turtle import *
from coloradd import *
t = Turtle()
t.pensize(4)
t.screen.colormode(255)
t.screen.delay(0)
t.screen.bgcolor("white")
t.screen.title("酷炫圆盘")
color=(255,0,0)
for i in range(360):
    t.pencolor(color)
    t.fd(200)
    t.bk(200)
    t.right(1)
    color = addcolor(color,0.01)
    
