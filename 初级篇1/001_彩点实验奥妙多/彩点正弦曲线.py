from turtle import *
from math import sin,radians
from random import randint,choice

color_list = ['red','orange','yellow','green','cyan','blue','purple']
width ,height = 720,600
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
    if y - 100 * sin(radians(x))  < 0 :              # 方程: y = a·sin(x)
        t.pencolor(choice(color_list))
        t.goto(x,y)
        t.dot(10)
  
