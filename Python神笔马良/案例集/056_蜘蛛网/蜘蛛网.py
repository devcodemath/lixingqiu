"""
   蜘蛛网.py
"""
import turtle

def draw_circle(pos,r):
    """
       pos:圆的中心点
       r:半径
       本函数以pos为中心点画半径为r的圆形。
    """
    turtle.penup()
    turtle.goto(pos)
    turtle.fd(r)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(r,360,8)     # 半径为r,度数为360度，步长为8
    turtle.penup()
    turtle.right(90)
    turtle.bk(r)

turtle.hideturtle()
turtle.bgcolor('black')
turtle.color('yellow')

turtle.delay(0)
turtle.speed(0)
for r in range(1,480,38):
    draw_circle((0,0),r)

turtle.pendown()
for _ in range(8):
    turtle.fd(500)
    turtle.bk(500)
    turtle.rt(45)

turtle.done()
