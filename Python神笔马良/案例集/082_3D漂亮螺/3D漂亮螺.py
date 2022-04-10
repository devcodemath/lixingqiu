"""
  3D漂亮螺.py
  注意亮度为0.5的时候最鲜艳
  本程序需要coloradd模块支持,安装方法:
  pip install coloradd
  技术支持微信scartch8,QQ:406273900
  程序运行需要很长时间,请耐心等待。
  可以把窗口最小化,然后就能以更快的速度画完。
  网址: www.lixingqiu.com
"""
import turtle
from coloradd import lightset

def draw_sprial():
    """画螺旋"""
    length = 0
    turtle.home()
    turtle.pendown()
    for _ in range(100):
        turtle.fd(length)
        turtle.rt(10)
        length += 0.2
    turtle.penup()
   
turtle.colormode(255)              # 设定颜色模式为255
turtle.bgcolor('black')            # 设定背景色为黑
turtle.hideturtle()                # 隐藏海龟
turtle.delay(0)                    # 绘画延时为0毫秒
turtle.speed(0)                    # 动作速度为最快
turtle.pensize(50)                 # 画笔粗细为50 
turtle.penup()                     # 抬笔

color = (15,180,0)
for r in range(50,0,-1):
    turtle.pensize(r)
    c = lightset(color,0.5-r/100)  # 设置亮度越来越高
    turtle.color(c)
    draw_sprial()                  # 画螺旋 
    
turtle.done()
