"""散开的小球2.py   参考答案 """

from turtle import *
from random import randint

def rc():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b

screen = Screen()
screen.delay(0)
screen.bgcolor("white")
screen.colormode(255)

t = Turtle(shape='circle')
t.penup()
t.color("cyan")

balls = [t]
[balls.append(t.clone()) for i in range(35)]
[balls[i].setheading(i*10) for i in range(36)]
[balls[i].color(rc()) for i in range(36)]

index = 0
while True:
    balls[index].fd(2)
    index = index + 1
    index = index % 36
