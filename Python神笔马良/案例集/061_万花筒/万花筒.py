"""
  万花筒.py
 
  本程序需要coloradd模块支持,安装方法:
  pip install coloradd
  技术支持微信scartch8,QQ:406273900

"""
import turtle
from coloradd import colorset
from winsound import PlaySound,SND_ASYNC,SND_LOOP

# 使用coloradd模块前需要把颜色模式设为255
turtle.colormode(255)          
turtle.bgcolor('black')
turtle.hideturtle()              # 隐藏海龟 
turtle.setheading(90)            # 设置方向为90度

def changecolor():
    x = turtle.xcor()
    y = turtle.ycor()
    c = colorset(abs(x)+abs(y))  # 把整数转换成RGB值
    turtle.color(c)
    
def draw_circle(i):
    """画图案"""
    turtle.left(90)              # 左转90度
    for _ in range(36):
       changecolor()             # 改变颜色
       turtle.fd(i/7)
       turtle.right(10)
    turtle.right(90)

PlaySound('BGM1.wav',SND_ASYNC|SND_LOOP)# 循环异步播放音乐

for i in range(10,90):
    for _ in range(8):        
        turtle.fd(i*2)
        draw_circle(i)
        turtle.bk(2*i)
        turtle.right(45)
turtle.done()
