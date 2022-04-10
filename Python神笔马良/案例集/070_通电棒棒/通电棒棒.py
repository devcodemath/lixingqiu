"""
  通电棒棒.py
  注意亮度为0.5的时候最鲜艳
  本程序需要coloradd模块支持,安装方法:
  pip install coloradd
  技术支持微信scartch8,QQ:406273900
  程序运行需要很长时间,请耐心等待。
  可以把窗口最小化,然后就能以更快的速度画完。
"""
import turtle
from coloradd import lightset,coloradd
        
turtle.colormode(255)               # 设定颜色模式为255
turtle.bgcolor('black')             # 设定背景颜色为黑色
turtle.hideturtle()                 # 隐藏海龟
turtle.delay(0)                     # 绘画延时为0毫秒 
turtle.speed(0)                     # 动作速度为最快

color = (255,10,250)                # 设定颜色三元组
for r in range(50,0,-1):            # r从50到1
    turtle.pensize(r)               # 设定画笔粗细
    color = coloradd(color,0.001)   # color颜色增加0.001
    c = lightset(color,1-r/100)     # color颜色设置亮度
    turtle.color(c)                 # 把c设置为海龟画笔与填充颜色
    turtle.fd(100)                  # 前进100个单位
    turtle.bk(100)                  # 倒退100个单位 

turtle.done()                       # 事件循环
