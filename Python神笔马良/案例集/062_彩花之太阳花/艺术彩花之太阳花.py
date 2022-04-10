"""
  彩花之太阳花.py
 
  本程序需要coloradd模块支持,安装方法:
  pip install coloradd
  技术支持微信scartch8,QQ:406273900

"""
import turtle
from coloradd import colorset
from winsound import PlaySound,SND_ASYNC,SND_LOOP

def draw_pattern():
    """画一个图案"""
    for _ in range(4):
        for _ in range(18):
            x = turtle.xcor()
            y = turtle.ycor()
            # 让颜色和距离产生关联
            c = colorset(abs(x) + abs(y))
            turtle.color(c)
            turtle.fd(7)
            turtle.left(5)
        turtle.right(180)
        
turtle.pensize(4)                  # 设置画笔粗细为4
turtle.colormode(255)              # 设置颜色模式为255    
turtle.bgcolor('black')            # 设置背景颜色为黑色 
turtle.hideturtle()                # 隐藏海龟

PlaySound('Jacek_Darabasz-M.wav',SND_ASYNC|SND_LOOP)
# 下面是画图案，画完一个图案后让海龟旋转22.5度
for i in range(16):
    draw_pattern()
    turtle.right(360/16)

turtle.done()

