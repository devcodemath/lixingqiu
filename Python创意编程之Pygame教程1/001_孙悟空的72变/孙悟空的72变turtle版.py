"""
    孙悟空的72变turtle版。
    本程会每隔3秒显示一张图片。
    其实质上是不断地变换海龟的造型图片。
"""
import glob
import turtle
from winsound import * 
from time import sleep

bg = "花果山.png"                      # 背景图

images = glob.glob("images/*.gif")     # 所有的图像

# 新建一个窗口,尺寸为480x360
screen = turtle.Screen()
screen.setup(480,360)
screen.bgpic(bg)
[screen.addshape(im) for im in images]# 增加所有图像

# 异步无限播放背景音乐
PlaySound("西游记片头.wav",SND_ASYNC|SND_LOOP)

while True:
   for image in images:              # 迭代每张图片
      turtle.shape(image)            # 设定海龟的造型
      screen.update()                # 刷新屏幕显示
      sleep(3)                       # 等待3秒钟
        
