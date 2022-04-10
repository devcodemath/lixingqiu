"""
  海龟绘图艺术画.py
 
  本程序需要coloradd模块支持,安装方法:
  pip install coloradd
  技术支持微信scartch8,QQ:406273900
  www.lixingqiu.com
  把窗口最小化可加快绘图速度。
"""
import time
import turtle
from coloradd import lightset
from winsound import PlaySound,SND_ASYNC,SND_LOOP

cs = [(25,150,250),(25,150,11),(250,12,2),
      (0,255,10),(123,241,33),(250,10,250)]

def  draw_pattern(d):
  turtle.tracer(0)
  for _ in range(16):
    for _ in range(4):
        for _ in range(18):            
            turtle.fd(d)
            turtle.left(5)
        turtle.right(180)
    turtle.right(360/16)
  turtle.tracer(1)
  
turtle.pensize(4)
turtle.speed(6)
turtle.delay(10)
turtle.colormode(255)
turtle.bgcolor('black')
turtle.setup(956,710)
turtle.bgpic('sparkling.png')
turtle.title('海龟绘图艺术www.lixingqiu.com')
turtle.hideturtle()

# 循环异步播放背景音乐
PlaySound('Werner_Condor-Unchained_Melody.wav',
          SND_ASYNC|SND_LOOP)
while True:
  for color in cs:
    # 画80个亮度越来越亮，步长越来越小的图形
    for r in range(80):
        c = lightset(color,0.5+r/160)  # 设置亮度
        turtle.color(c)
        draw_pattern((80-r)/10)
     
    turtle.clear()


