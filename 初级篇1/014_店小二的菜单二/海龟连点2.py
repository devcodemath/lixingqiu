from random import randint
from turtle import *

width,height = 800,600
cors = []

screen = Screen()
screen.setup(width,height)
screen.bgcolor("black")

 
for i in range(100):
    x = randint(-400,400)
    y = randint(-300,300)
    cors.append((x,y))

t = Turtle()
t.penup()
t.color("yellow")
t.goto(cors[0])
t.pendown()
while cors:
    xy = cors.pop(0)
    t.goto(xy)
    t.dot(10,'cyan')

screen.exitonclick()
