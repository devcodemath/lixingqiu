"""
  爆炸图.py
"""
import turtle
import random

cs = ['yellow','red','purple','blue']

turtle.bgcolor('black')
turtle.delay(0)
turtle.speed(0)
turtle.pensize(4)
index = 0
for index in range(3,-1,-1):
    c = cs[index]
    turtle.color(c)
    turtle.pensize(index+2)
    
    for _ in range(150):
        d = (index+1) * random.randint(50,120)
        f = random.randint(1,360)
        turtle.seth(f)
        turtle.fd(d)
        turtle.goto(0,0)

turtle.done()
