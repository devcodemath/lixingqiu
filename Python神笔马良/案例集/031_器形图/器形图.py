"""
   器形图.py
   采用前进，倒退，左转，右转命令制作的一个图形。
"""
import turtle

def draw_square():
    """
       左转45度后再画一个正方形
    """
    turtle.left(45)
    for _ in range(4):
        turtle.fd(50)
        turtle.rt(90)
    turtle.right(45)

turtle.pensize(2) 
for _ in range(4):
    turtle.left(135)
    turtle.fd(50)
    draw_square()
    turtle.bk(50)
    turtle.rt(135)
    
    turtle.fd(50)
    turtle.rt(90)

turtle.done()
