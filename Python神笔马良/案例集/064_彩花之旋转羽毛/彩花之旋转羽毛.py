"""
  彩花之旋转羽毛.py
 
  本程序需要coloradd模块支持,安装方法:
  pip install coloradd
  技术支持微信scartch8,QQ:406273900
  www.lixingqiu.com
"""
import turtle
from coloradd import colorset
from winsound import PlaySound,SND_ASYNC,SND_LOOP

turtle.colormode(255)
turtle.bgcolor('black')
turtle.hideturtle()
turtle.pensize(5)
turtle.setheading(90)

def changecolor():
    x = turtle.xcor()
    y = turtle.ycor()
    c = colorset(abs(x)+abs(y))
    turtle.color(c)
    
def draw_feather(c):
    """画羽毛图案"""     
    for _ in range(18):
       changecolor()
       turtle.fd(c)
       turtle.lt(5)
    turtle.left(180)
    for _ in range(18):
       changecolor()
       turtle.fd(c)
       turtle.rt(5)
       
PlaySound('DeColores.wav',SND_ASYNC|SND_LOOP)

for c in range(10,0,-1):
    for _ in range(12):        
        draw_feather(c)
        turtle.right(30)
turtle.done()
