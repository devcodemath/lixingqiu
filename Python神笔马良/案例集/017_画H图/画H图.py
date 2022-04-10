"""
   画H图.py
   可以把本程序改成递归图，要点为在下面的dot命令修改。
   相信你一定能完成。
"""
import turtle

def draw_H(d):
    turtle.fd(d)
    turtle.left(90)
    turtle.fd(2*d);turtle.dot()
    turtle.bk(4*d);turtle.dot()
    turtle.fd(2*d)
    turtle.left(90)
    turtle.fd(2*d)
    turtle.right(90)
    turtle.fd(2*d);turtle.dot()
    turtle.bk(4*d);turtle.dot()
    turtle.fd(2*d)
    turtle.right(90)
    turtle.fd(d)

turtle.pensize(2)
draw_H(50)
turtle.done()
