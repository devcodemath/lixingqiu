"""
   空心T字.py
"""
import turtle                # 导入海龟模块

turtle.pensize(2)            # 设定海龟画笔粗细为2
turtle.setheading(90)        # 设定方向为90度
turtle.color('black')        # 设定颜色为黑色
turtle.bgcolor('light cyan') # 设定背景色为淡青色

turtle.fd(50)                # 前进50个单位 
turtle.rt(90)                # 右转90度
turtle.fd(150)               # 前进150个单位
turtle.rt(90)                # 右转90度
turtle.fd(50)                # 前进50个单位
turtle.rt(90)                # 右转90度

turtle.fd(50)
turtle.lt(90)
turtle.fd(100)
turtle.rt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(50)
turtle.ht()                  # 隐藏海龟
turtle.done()                # 海龟做完了

