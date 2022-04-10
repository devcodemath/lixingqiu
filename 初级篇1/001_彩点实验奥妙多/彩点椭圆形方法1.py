from turtle import *
import math
from random import randint,choice

color_list = ['red','orange','yellow','green','cyan','blue','purple']
width ,height = 600,600
screen = Screen()
screen.title("椭圆方程打点实验")
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
    
    a = 10   ;  b = 6                   #请参数椭圆的标准方程
    expression = x*x / (a*a) + y * y / (b*b)   #换成减号变成双曲形图
    
    if expression < 300:
        
        t.pencolor(choice(color_list))
        t.goto(x,y)
        t.dot(10)
  
