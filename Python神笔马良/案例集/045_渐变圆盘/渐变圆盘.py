"""
   本程序需要coloradd模块支持,安装方法
   pip install coloradd
   技术支持微信 scratch8
"""
import turtle
from coloradd import coloradd

turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.colormode(255)      # 设定颜色模式为255

c = (255,0,0)
for _ in range(360):
    turtle.fd(100)         # 前进100个单位
    turtle.bk(100)         # 倒退100个单位
    c = coloradd(c,0.01)   # 颜色增加0.01
    turtle.color(c)        # 把c设为海龟画笔颜色
    turtle.rt(1)           # 右转1度
    
turtle.done()              # 事件循环
