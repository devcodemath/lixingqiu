"""
   3D红球.py
   本程序不断地打直径越来越小，亮度越来越高的圆点。
   最后就形成了有种3D效果的圆球。
"""
import turtle
from coloradd import lightset

turtle.colormode(255)              # 设定颜色为255
turtle.bgcolor('black')            # 设定背景颜色 
turtle.hideturtle()                # 隐藏海龟

red = (255,0,0)
for r in range(200,0,-1):
    c = lightset(red,1-r/200)      # 设置亮度
    turtle.color(c)                # 设置海龟颜色为c
    turtle.dot(r)                  # 打直径为r的圆点 
    
turtle.done()
