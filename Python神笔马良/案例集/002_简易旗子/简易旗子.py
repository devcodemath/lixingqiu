"""
   简易旗子.py
"""
import turtle          # 导入海龟模块

turtle.pensize(2)      # 设定画笔轨迹粗细为2
turtle.setheading(90)  # 设置方向为90度
turtle.fd(100)         # 海龟前进100个单位

for x in range(4):     # 在范围4内不断更新x
    turtle.fd(100)     # 海龟前进100个单位
    turtle.rt(90)      # 海龟右转90度
    
turtle.done()          # 海龟做完了(进入事件循环)
