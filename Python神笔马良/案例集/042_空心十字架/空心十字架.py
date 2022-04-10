"""
   空心十字架.py
"""
import turtle

def draw_pattern(length):
    
    for _ in range(3):
        turtle.fd(length)
        turtle.rt(90)
    turtle.right(180)   # 向后转

turtle.width(2)
for _ in range(4):      
    draw_pattern(50)

turtle.ht()             # 隐藏海龟
turtle.done()           # 事件循环
