
from turtle import Turtle
from random import randint

colors = ['red','orange','yellow','green','cyan','blue','purple','pink','brown','magenta']

t = Turtle()
t.screen.bgcolor("black")
t.pensize(2) 
t.penup()
 
i = 0
while i < 200:
    color = colors[i % len(colors)]
    fx = randint(1,360)
    t.setheading(fx)
    distance = randint(10,300)
    t.fd(distance)
    t.dot(distance,color)
    t.bk(distance)   
  
    i = i + 1
    




