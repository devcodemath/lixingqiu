"""春晓多媒体语文课件.py"""

from turtle import *
from time import sleep
from winsound import PlaySound,SND_ASYNC

ziti = ("",24,"bold")
music = '春晓.wav'
背景表=["001.png","002.png","003.png","004.png"]
诗句 = ["春晓","----孟浩然","春眠不觉晓","处处闻啼鸟","夜来风雨声","花落知多少"]

screen = Screen()
screen.setup(700,500)
screen.title("春晓")

index=0
def alt_background():
    """切换背景"""
    global index
    screen.bgpic(背景表[index])
    index = index + 1
    index = index % 4
    screen.ontimer(alt_background,100)
alt_background()

t = Turtle(visible = False)# 新建不可见海龟对象
t.penup()                  # 抬笔
t.color("cyan")            # 颜色为青色
t.goto(-100,200)           # 坐标定位
t.seth(90)                 # 设置方向为90
 
for 诗 in 诗句:            # 轮换诗句
   t.bk(50)                # 倒退50个单位
   t.write(诗,font=ziti)   # 写诗
   sleep(1)                # 延时1秒

PlaySound(music, SND_ASYNC) #异步播放音效
screen.exitonclick()
