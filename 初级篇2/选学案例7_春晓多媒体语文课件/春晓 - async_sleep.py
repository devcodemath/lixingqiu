"""春晓多媒体语文课件-async_write.py"""

from turtle import *
from time import sleep,time
from winsound import PlaySound,SND_ASYNC

def async_write(second):
    """异步延时写字命令，参数为秒数"""
    index = 0
    begin_time = time()                    # 起始时间
    def delay_write():
        nonlocal index,begin_time          # 非本地变量
        if index < 5:                      # 如果索引号小于5
            if time() - begin_time >= second: # 时间到了就写诗
                t.bk(50)                   # 倒退50个单位
                t.write(诗句[index],font=ziti)   # 写诗
                index = index + 1          # 索引号加1        
                begin_time = time()        # 重新设定起始时间        
            screen.ontimer(delay_write,100)# 100毫秒后再次执行
    delay_write()

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

async_write(1)             # 异步写诗

PlaySound(music, SND_ASYNC) #异步播放音效
screen.exitonclick()
