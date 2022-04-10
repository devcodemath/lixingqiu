"""
   星汉灿烂.py
   本程序是太阳系百科知识集锦,先会有一个序幕,然后会有封面,
   最后是八大行星出现。如果本程序在未来的Python版本中挂了,
   请自行修改程序.
"""
import os
from gifplay import *
from fadeshow import *
from planet import * 

width,height = 480,360
bgmusic = "光田康典_梦的岸边.wav"

os.environ['SDL_VIDEO_CENTERED'] = '1' # 窗口居中显示
print('播放序幕,返回屏幕对象')
screen = playgif('序幕.gif',width,height,bgmusic)
pygame.display.set_caption("星汉灿烂Python版,作者:李兴球")

print("淡入封面图形") 
cover = pygame.image.load("封面.png").convert()
fade_in_image(screen,cover)

print("等待任意按键") 
clock = pygame.time.Clock()
while not pygame.event.get(KEYDOWN):clock.tick(30)
   
print("淡出封面")  
fade_out_image(screen,cover)

print("淡入背景")
background = pygame.image.load("images/太阳.png")
fade_in_image(screen,background)

print("显示行星,等待单击各行星")
show_planet(screen,background)
