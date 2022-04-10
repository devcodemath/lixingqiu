"""画正多边形.py"""
import turtle

def draw_poly(turtle,number,length):
    """画正多边形的函数,参数分别为:海龟,边数,边长"""
    angle = 360 // number
    for _ in range(number):
        turtle.fd(length)
        turtle.rt(angle)
        
screen = turtle.Screen()
screen.colormode(255)
screen.delay(0)
screen.bgcolor(0,0,0)

t = turtle.Turtle()
t.color(255,255,255)
draw_poly(t,6,100)

screen.exitonclick()

