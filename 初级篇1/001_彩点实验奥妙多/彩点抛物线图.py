from turtle import *
import math
from random import randint,choice

width ,height = 600,600
color_list = ['red','orange','yellow','green','cyan','blue','purple']

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
    if y - x*x/200 > 0 :              # 方程: y = a·x*x
        t.pencolor(choice(color_list))
        t.goto(x,y)
        t.dot(10)
  
