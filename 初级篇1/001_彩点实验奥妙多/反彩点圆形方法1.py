from turtle import *
import math
from random import randint,choice

color_list = ['red','orange','yellow','green','cyan','blue','purple']
width ,height = 600,600
screen = Screen()
screen.setup(width,height)
screen.bgcolor("black")
screen.delay(0)

t = Turtle()
t.pencolor("white")
t.hideturtle()
t.penup()

while True:
    x = randint(-width/2,width/2)
    y = randint(-height/2,height/2)
    if math.sqrt(x*x + y*y)>100:
        t.pencolor(choice(color_list))
        t.goto(x,y)
        t.dot(10)
