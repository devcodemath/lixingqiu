"""
  迷宫.py
"""
import turtle       # 导入海龟模块
 
turtle.pensize(2)   # 设定画笔粗细为2
turtle.speed(0)     # 设定移动速度为最快

for i in range(50): # 在范围50内迭代i
    turtle.fd(i*8)  # 前进i*8个单位 
    turtle.rt(90)   # 右转90度

turtle.done()       # 做完了
