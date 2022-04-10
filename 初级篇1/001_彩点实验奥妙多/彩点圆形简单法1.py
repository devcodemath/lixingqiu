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

radius = 100
while True:
    step = randint(1,100)
    t.setheading(randint(1,360))
    t.fd(step)    
    t.pencolor(choice(color_list)) 
    t.dot(10)
    t.bk(step)
  
