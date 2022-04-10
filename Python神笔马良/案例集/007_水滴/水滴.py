"""
   水滴.py
"""
import turtle              # 导入海龟模块

turtle.ht()                # 隐藏海龟
turtle.color('blue')       # 设定颜色为蓝色
turtle.setheading(-90)     # 设定方向为向下

for s in range(1,100):     # 在1到100的范围内更新s
    turtle.pensize(s)      # 把s设为画笔粗细
    turtle.fd(1)           # 前进1个单位

turtle.done()              # 海龟做完了
