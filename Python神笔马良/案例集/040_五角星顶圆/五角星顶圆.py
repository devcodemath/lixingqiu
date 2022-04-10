"""
   五角星顶圆.py
"""
import turtle

def draw_circle(d):
    turtle.left(90)
    for _ in range(10):
        turtle.fd(d)
        turtle.rt(36)
    turtle.right(90)

turtle.width(2)
for _ in range(5):
    turtle.fd(180)
    draw_circle(5)
    turtle.right(144)

turtle.ht()
turtle.done()
