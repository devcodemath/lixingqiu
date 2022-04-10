from turtle import *
from random import randint,choice

colorList = ["red","orange","yellow","green","cyan","blue","purple","black"]

t = Turtle()
t.pensize(4)

for i in range(4):
    t.pencolor(choice(colorList))
    t.fd(100)            
    t.fd(-100)
    t.right(90)

t.screen.exitonclick()
