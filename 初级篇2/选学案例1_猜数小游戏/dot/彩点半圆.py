
from turtle import Turtle
from random import randint

colors = ['red','orange','yellow','green','cyan','blue','purple','pink','brown','magenta']

t = Turtle(shape='circle')
t.shapesize(0.2,0.2)
t.screen.bgcolor("black")
t.screen.delay(0)
t.pensize(2) 
t.penup()
 
i = 0
while True:
    color = colors[i % len(colors)]
    t.color(color)
    fx = randint(0,180)
    t.setheading(fx)
    distance = randint(0,100)
    t.fd(distance)
    t.stamp()
    t.bk(distance)   
  
    i = i + 1
    




