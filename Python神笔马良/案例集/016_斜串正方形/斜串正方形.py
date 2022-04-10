"""
   斜串正方形.py
"""
import turtle

def draw_square(length):
    """
       画边长为length的正方形
    """
    for _ in range(4):
        turtle.fd(length)
        turtle.rt(90)

turtle.penup()
turtle.goto(-100,100)
turtle.pensize(2)
turtle.pendown()
for x in range(6):        # 在范围6内迭代x
    draw_square(40)        # 画一个边长为40的正方形 
    turtle.fd(40)          # 海龟前进40个单位
    turtle.right(90)       # 海龟右转90度
    turtle.fd(40)          # 海龟前进40个单位  
    turtle.left(90)        # 海龟左转90度
    
turtle.done()              # 海龟做完了
