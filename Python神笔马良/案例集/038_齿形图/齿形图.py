"""
   齿形图.py
"""
import turtle

def draw_one():
    turtle.left(90)
    turtle.fd(30)
    turtle.bk(30)
    turtle.rt(90)

turtle.pensize(2)  
for _ in range(10):
    turtle.fd(20)
    draw_one()
turtle.fd(20)

turtle.done()
