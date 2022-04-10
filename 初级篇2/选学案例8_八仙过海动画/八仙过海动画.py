"""八仙过海动画.py"""

from glob import glob
from time import sleep
from turtle import Screen,Turtle
from winsound import PlaySound,SND_ASYNC,SND_LOOP

music = "horizon.wav"
width,height = 718,700
eight_images = glob("images/*.gif")  # 返回images文件夹下所有gif文件

screen = Screen()
screen.delay(4)
screen.setup(width,height)
screen.bgpic("8xian.png")            # 设置屏幕背景图
screen.title("八仙过海,各显神通")
screen.update()

for i in range(8):
    screen.addshape(eight_images[i]) # 添加八仙图到屏幕的形状列表

t = Turtle(visible=False)
t.penup()
index = 0
PlaySound(music,SND_ASYNC|SND_LOOP)  # 重复播放背景音乐
while True:    
    dx = -2 if index % 2 == 0 else 2 # 也可写成 (index%2)*4 -2         
    t.shape(eight_images[index])     # 设定海龟的形状
    t.showturtle()                   # 显示出来
    sleep(1)
    for i in range(300):             # 重复300次,向右或左移动
        t.fd(dx)
    t.hideturtle()                   # 隐藏海龟
    t.goto(0,0)                      # 回到原点
    index = index + 1                # 下一个索引号
    index = index % 8                # 对8求余
    sleep(1)
