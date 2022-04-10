"""
   田字格.py
"""
import turtle           # 导入海龟模块

turtle.width(2)         # 设定画笔宽度为2

for _ in range(4):      # 迭代下划线4次
    for _ in range(4):  # 更新_4次
        turtle.fd(100)  # 海龟前进100
        turtle.lt(90)   # 海龟左转90度
    turtle.lt(90)

turtle.done()           # 进入事件循环
