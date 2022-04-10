"""迪伽奥特曼动画演示.py"""

import os
from turtle import *
from time import sleep
from winsound import PlaySound,SND_ASYNC,SND_LOOP

music = "迪迦奥特曼主题曲.wav"
PlaySound(music, SND_ASYNC|SND_LOOP)  # 重复地异步播放音效
bgimages = []                         # 存储所有背景图列表
frame_folder = os.getcwd() + os.sep + "奥特曼动画帧"

screen = Screen()                     # 新建屏幕对象
screen.bgcolor("black")               # 设定背景颜色
screen.title("奥特曼打怪兽_作者:李兴球")

for i in range(23):
    filename = "0" * (4-len(str(i))) + str(i) + ".png"
    pic = frame_folder + os.sep + filename
    bgimages.append(pic)
    
index = 0                   # 设定索引号从0开始
while True:
    image = bgimages[index] # 选择索引为index的图片
    screen.bgpic(image)     # 把这张图片设为背景图
    index=index + 1         # 索引加1
    index=index % 23        # 索引对23求余
    sleep(0.1)              # 延时0.1秒
    screen.update()         # 屏幕刷新

     
