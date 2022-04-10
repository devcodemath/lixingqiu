"""
   三星连线.py
"""
import turtle

turtle.pensize(2)

for _ in range(3):
    turtle.right(120)
    for _ in range(5):
        turtle.fd(30)
        turtle.rt(144)
    turtle.left(120)
    turtle.fd(100)
    turtle.lt(120)

turtle.ht()
turtle.done()
