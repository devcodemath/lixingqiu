"""
   篱笆.py
"""
import turtle

def draw_triangle():
    """画正三角形函数"""
    for _ in range(3):
        turtle.fd(5)
        turtle.right(120)

turtle.delay(0)
turtle.speed(0)
turtle.setheading(90)
turtle.pensize(2)
for _ in range(10):
    # 下面是画正12边形，
    # 不过在移动之前先画了一个小三角形
    for _ in range(12):
        draw_triangle()
        turtle.fd(50)
        turtle.left(30)
    turtle.fd(5)

turtle.done()
