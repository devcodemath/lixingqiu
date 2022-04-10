"""请给本程序每行代码添加注释"""

from turtle import Turtle,Screen
from random import randint

def line(a,b):
    y = lambda x:a*x + b
    return y

a = randint(1,3)
b = randint(1,10)

f = line(a,b)

startx = -100
starty = f(startx)

endx = 100
endy = f(endx)

screen = Screen()
screen.delay(0)
screen.setup(800,800)

t = Turtle(visible=False)
t.penup()
t.goto(startx,starty)
t.write(str(startx) + "," + str(starty))
t.pendown()
t.goto(endx,endy)
t.write(str(endx) + "," + str(endy))
