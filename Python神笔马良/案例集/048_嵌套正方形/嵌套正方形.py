"""
   嵌套正方形.py
"""
import turtle

def draw_square(length,level):
    if level<1:return
    for _ in range(4):
       draw_square(length//4,level-1)
       turtle.fd(length)
       turtle.rt(90)

turtle.pensize(2)                    # 画笔粗细
draw_square(200,3)                   # 调用函数
turtle.ht()                          # 隐藏海龟
turtle.done()                        # 事件循环
