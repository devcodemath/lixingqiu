from turtle import *
from random import randint,choice

colorList = ["red","orange","yellow","green","cyan","blue","purple","black"]


t = Turtle()
t.penup()
t.pensize(4) 

for i in range(360):
    t.pencolor(choice(colorList))
    t.fd(30)   
    t.pendown()
    t.fd(70)
    t.penup()
    t.fd(-100)
    t.right(1) 
