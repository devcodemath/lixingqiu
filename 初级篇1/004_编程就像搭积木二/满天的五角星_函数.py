"""随机在屏幕上打白色小星星.
"""
from turtle import *
from random import randint

width,height = 600,600
screen = Screen()                       
screen.title("满天的星星")         
screen.bgcolor("black")
screen.setup(width,height)  
screen.delay(0)

def drawStar(g,length):
    t.pendown()
    g.begin_fill()
    for x in range(5):
        g.fd(length)
        g.left(144)
    g.end_fill()
    t.penup()

t = Turtle()
t.color("white")
 
t.penup()
for i in range(600):
    fx = randint(1,360)
    t.setheading(fx)
    t.fd(randint(1,300))    
    drawStar(t , randint(5,10))    
    t.home()    
 
drawStar(t , 100)  
   



 

