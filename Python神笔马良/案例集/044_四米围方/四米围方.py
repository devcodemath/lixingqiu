"""
   四米围方.py
"""
import turtle

def draw_mi():
    """画米字图形"""
    for _ in range(8):
        turtle.fd(15)
        turtle.bk(15)
        turtle.rt(45)

turtle.pensize(2)
for _ in range(4):
    turtle.fd(100)
    draw_mi()          # 画米字图形
    turtle.rt(90)

turtle.ht()            # 隐藏海龟
turtle.done()
