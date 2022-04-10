"""
  漂亮米.py
  注意亮度为0.5的时候最鲜艳
  本程序需要coloradd模块支持,安装方法:
  pip install coloradd
  技术支持微信scartch8,QQ:406273900
  程序运行需要很长时间,请耐心等待。
  可以把窗口最小化,然后就能以更快的速度画完。
"""
import turtle
from coloradd import lightset

def draw米():
    for _ in range(8):
        turtle.fd(100)
        turtle.bk(100)
        turtle.right(45)
   
        
turtle.colormode(255)             # 设定颜色模式为255 
turtle.bgcolor('black')           # 设定背景颜色为黑
turtle.hideturtle()               # 隐藏海龟
turtle.delay(0)                   # 设定绘画延时为0毫秒
turtle.speed(0)                   # 设定移动速度为0(最快)

ys = (15,150,0)
for r in range(50,0,-1):
    turtle.pensize(r)             # 画笔越来越细
    c = lightset(ys,0.5-r/100)    # 亮度越来越高
    turtle.color(c)               # 把c设为海龟颜色
    draw米()

turtle.done()                     # 事件循环
