"""
   画绿树.py
"""
import turtle               # 导入海龟模块

turtle.speed(0)             # 设定海龟移动速度为最快
turtle.pensize(4)           # 设定画笔尺寸为4  
turtle.shape('triangle')    # 设定海龟造型为三角形
turtle.fillcolor('lime')    # 设定填充颜色为亮绿

turtle.setup(360,480)       # 设定屏幕大小为360x480
turtle.screensize(1,1)      # 设定画布大小为1x1
turtle.bgcolor('light cyan')# 设定屏幕背景色为淡青色 
turtle.left(90)             # 海龟左转90度
 
turtle.bk(10)               # 海龟倒退10个单位
turtle.shapesize(2,1,2)     # 设定海龟造型宽度长度及边框厚度
turtle.stamp()              # 盖图章

turtle.bk(30)               # 海龟倒退30个单位
turtle.shapesize(3,2,2)     # 设定海龟造型宽度长度及边框厚度
turtle.stamp()              # 盖图章

turtle.bk(48)               # 海龟倒退48个单位
turtle.shapesize(5,3,2)     # 设定海龟造型宽度长度及边框厚度
turtle.stamp()              # 盖图章

turtle.hideturtle()         # 隐藏海龟 
turtle.goto(0,0)            # 到原点
turtle.bk(150)              # 退150个单位
turtle.done()               # 事件循环
