
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
    x= randint(-100,100)
    y = randint(-100,100)    
    t.goto(x,y)
    t.stamp()
  
    i = i + 1
    




