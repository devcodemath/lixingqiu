"""
    孙悟空的72变Pygame版。
    本程序做为Pygame的引入程序。
    它会每隔3秒显示一张图片。
"""
import glob
import pygame
from winsound import * 
from time import sleep

bg = pygame.image.load("花果山.png")   # 加载背景图

images = glob.glob("images/*.gif")     # 所有的图像

# 下面是加载所有的图形到内存中
images = [pygame.image.load(im) for im in images]

# 新建一个窗口,尺寸为480x360
screen = pygame.display.set_mode((480,360))

# 异步无限播放背景音乐
PlaySound("西游记片头.wav",SND_ASYNC|SND_LOOP)

while True:
   for image in images:              # 迭代每张图片
      event = pygame.event.poll()    # 获取一个事件
      screen.blit(bg,(0,0))          # 把背景贴在屏幕上
      screen.blit(image,(100,100))   # 把图像贴在屏幕上  
      pygame.display.update()        # 更新屏幕的显示
      sleep(3)                       # 等待3秒钟
        
