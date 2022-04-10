"""
  彩花之花蝴蝶.py
 
  本程序需要coloradd模块支持,安装方法:
  pip install coloradd
  技术支持微信scartch8,QQ:406273900
  www.lixingqiu.com
"""
import turtle
from coloradd import colorset
from winsound import PlaySound,SND_ASYNC,SND_LOOP

turtle.pensize(2)
turtle.colormode(255)                 # 设定颜色模式为RGB255
turtle.bgcolor('black')               # 设定背景颜色为黑色 
turtle.hideturtle()                   # 隐藏海龟
turtle.setheading(90)                 # 设置方向为90度

def changecolor():
    """让海龟的颜色和到原点的距离产生关联"""
    x = turtle.xcor()
    y = turtle.ycor()
    c = colorset(abs(x)+abs(y))
    turtle.color(c)
    
def draw_miao(length):
    """画一个类似小芽苗的图形"""
    for _ in range(7):
       changecolor()
       turtle.fd(length)
       turtle.right(15)
    for _ in range(7):
       changecolor()
       turtle.left(15)
       turtle.bk(length)
    for _ in range(7):
       changecolor()
       turtle.fd(length)
       turtle.left(15)
    for _ in range(7):
       changecolor() 
       turtle.right(15)
       turtle.bk(length)

def draw_pattern(length):
    """画步长为length的图案"""
    for i in range(4):
        draw_miao(length)       
        turtle.right(90)
    
PlaySound('11.wav',SND_ASYNC|SND_LOOP)

# 画若干步长不一样的图案
for d in range(1,50):
    draw_pattern(d)

turtle.done()
