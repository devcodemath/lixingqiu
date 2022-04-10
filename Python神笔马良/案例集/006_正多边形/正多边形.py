"""
   正多边形.py
"""
import turtle

turtle.pensize(2)

for n in range(3,10):
    for _ in range(n):
        turtle.fd(80)
        turtle.left(360/n) 

turtle.done()
