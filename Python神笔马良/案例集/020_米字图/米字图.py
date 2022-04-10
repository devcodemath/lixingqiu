"""
  米字图.py
"""
import turtle           # 导入海龟模块

turtle.pensize(2)       # 设定画笔粗细

for x in range(8):      # 在范围8内迭代x
    turtle.fd(100)
    turtle.bk(100)      # 倒退100个单位
    turtle.left(45)     # 左转45度

turtle.done()           # 画完了 
