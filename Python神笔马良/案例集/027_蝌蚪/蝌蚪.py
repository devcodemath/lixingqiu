"""
    蝌蚪.py
"""
import turtle

turtle.bgcolor('yellow')             # 背景颜色
turtle.pensize(2)                    # 画笔粗细
turtle.penup()                       # 抬笔
turtle.bk(250)                       # 倒退250
 
for _ in range(5):
    turtle.penup()                   # 抬笔
    turtle.setheading(90)            # 设置方向为90
    turtle.sety(-200)                # 设置y坐标
    turtle.setx(turtle.xcor() + 100) # x坐标增加100
    turtle.pendown()                 # 落笔
    turtle.circle(630,10)            # 画弧形
    turtle.circle(-630,10)           # 画弧形
    turtle.dot(40)                   # 打圆点

turtle.done()                        # 事件循环
