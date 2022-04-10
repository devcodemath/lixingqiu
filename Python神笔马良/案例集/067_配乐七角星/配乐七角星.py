"""
  配乐七角星.py
 
  本程序需要coloradd模块支持,安装方法:
  pip install coloradd
  技术支持微信scartch8,QQ:406273900
  www.lixingqiu.com
"""
import turtle
from coloradd import coloradd
from winsound import PlaySound,SND_ASYNC,SND_LOOP

turtle.colormode(255)
turtle.bgcolor('black')
turtle.hideturtle()
turtle.pensize(4)
turtle.setheading(90)

PlaySound('Devastating_MC.wav',SND_ASYNC|SND_LOOP)

size = 10
c = (255,0,0)
while True:
    c = coloradd(c,0.01)
    turtle.color(c)
    turtle.fd(size)             # 前进size的距离
    turtle.right(154)
    size += 0.5                 # size越来越大
