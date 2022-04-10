"""
   绿叶.py
"""
import turtle               # 导入海龟模块

turtle.bgcolor('pink')      # 设定背景颜色
turtle.pensize(2)           # 设定画笔粗细
turtle.pencolor('white')    # 设定画笔颜色
turtle.fillcolor('green')   # 设定填充颜色

turtle.begin_fill()         # 开始填充 
for _ in range(2):
    for _ in range(9):
        turtle.fd(10)
        turtle.rt(10)
    turtle.rt(90)
turtle.end_fill()           # 结束填充 

turtle.done()               # 画完了
