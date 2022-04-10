"""
   阴影丫字.py
"""
import turtle

turtle.delay(0)
turtle.speed(0)

def draw_ya(pos,ys):
    """
       pos:坐标
       ys:颜色
    """
    turtle.penup()
    turtle.goto(pos)
    turtle.color(ys)

    turtle.down()
    turtle.fd(100)
    turtle.left(60)
    turtle.fd(50)
    turtle.bk(50)
    turtle.right(120)
    turtle.fd(50)
    turtle.bk(50)
    turtle.left(60)
    turtle.bk(100)

turtle.left(90)
turtle.pensize(23)
draw_ya((0,0),'black')
draw_ya((-9,12),'blue')
turtle.done()
