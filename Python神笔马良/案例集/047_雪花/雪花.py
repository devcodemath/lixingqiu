"""
   雪花.py
"""
import turtle

def draw_branch(d):
    for _ in range(2):
        turtle.fd(d)
        turtle.lt(45)
        turtle.fd(d)
        turtle.bk(d)
        turtle.rt(90)
        turtle.fd(d)
        turtle.bk(d)
        turtle.lt(45)
    turtle.bk(2*d)

turtle.pensize(2)
for _ in range(6):
    draw_branch(30)
    turtle.rt(60)
    
turtle.done()
