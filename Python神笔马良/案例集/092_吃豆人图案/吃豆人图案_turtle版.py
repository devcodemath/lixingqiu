"""
   吃豆人图案_turlte版.py
"""
import turtle

turtle.pensize(10)
turtle.fillcolor('blue')    # 设定填充颜色
turtle.left(15)

turtle.begin_fill()         # 开始填充
turtle.fd(200)
turtle.left(90)
turtle.circle(200,315)      # 画圆，度数为315
turtle.home()
turtle.end_fill()           # 结束填充

turtle.ht()                 # 隐藏海龟
turtle.done()               # 事件循环
