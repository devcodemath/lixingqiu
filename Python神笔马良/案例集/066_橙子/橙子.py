"""
  橙子.py
  注意亮度为0.5的时候最鲜艳
  本程序需要coloradd模块支持,安装方法:
  pip install coloradd
  技术支持微信scartch8,QQ:406273900
  程序运行需要很长时间,请耐心等待。
  可以把窗口最小化,然后就能以更快的速度画完。
"""
import turtle
from coloradd import lightset

def draw8():
    """画一个8字"""
    for _ in range(10):
        turtle.fd(10)
        turtle.left(18)
    for _ in range(20):
        turtle.fd(10)
        turtle.right(18)
    for _ in range(10):
        turtle.fd(10)
        turtle.left(18)
        
def draw20_8():
    """画20个8字"""
    for _ in range(20):
        draw8()
        turtle.right(18)
        
turtle.colormode(255)
turtle.bgcolor('black')
turtle.hideturtle()
turtle.delay(0)
turtle.speed(0)

yanse = (195,150,0)
for r in range(50,0,-1):
    turtle.pensize(r)
    c = lightset(yanse,1-r/100) # 根据第二个参数，返回新的RGB三元组 
    turtle.color(c)             # 把c设置为海龟画笔的颜色
    draw20_8()

turtle.done()
