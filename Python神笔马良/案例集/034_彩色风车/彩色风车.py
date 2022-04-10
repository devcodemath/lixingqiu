"""
   彩色风车.py
"""

import turtle

cs = ['red','orange','yellow','green',
      'cyan','magenta','lime','blue']

turtle.bgcolor('black')

for i in range(8):
    turtle.color(cs[i])
    turtle.goto(0,0)
    turtle.pensize(1)
    turtle.pendown()
    # 重复14次，移动右转并且画笔越来越粗
    for x in range(2,16):
        turtle.fd(6)
        turtle.rt(3)
        turtle.pensize(x*2)
    turtle.rt(3)         # 45 - 14*3
    turtle.penup()
turtle.done()
