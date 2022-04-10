"""
  调皮田彩格.py
 
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
turtle.pensize(2)
turtle.speed(0)
turtle.delay(0)
turtle.screensize(1,1)         # 设置画布尺寸为1x1
turtle.setup(360,480)
turtle.title('调皮田彩格www.lixingqiu.com')

PlaySound('笨蛋.wav',SND_ASYNC|SND_LOOP)

n = 1
while True:
    c = (255,0,0)
    size = 1
    for _ in range(120):
        for _ in range(4):
           c = coloradd(c,0.01)       # 把c这种颜色增加0.01
           turtle.color(c)            # 设置c为海龟画笔及填充颜色
           turtle.fd(size)            # 前进size个单位
           size += 0.1                # size增加0.1 
           turtle.right(n * 90)       # 旋转90度
        turtle.right(n * 91)          # 旋转91度
    while turtle.undobufferentries(): # 当有可撤销的动作的时候
        turtle.undo()                 # 撤销这个动作
    turtle.clear()                    # 清空所画的
    n = -n
    
