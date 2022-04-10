"""
   整体透明度图像的mask测试程序.py
"""
import pygame
from random import randint
from pygame.locals import *

width,height = 480,360
xy = width//2,height//2

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("整体透明度图像的mask测试程序.py")

nezha = pygame.image.load('nezha.png').convert()
rect = nezha.get_rect(center=xy)
nezha.set_alpha(40)                 # 设置整体透明度
nezha.set_colorkey((255,255,255))   # 设置白色不渲染,此处mask为0
mask = pygame.mask.from_surface(nezha)
w,h = rect.size

screen.blit(nezha,rect)
pygame.display.update()

while True:
    x = randint(0,w - 1)
    y = randint(0,h - 1)
    print(mask.get_at((x,y)),end=' ')

"""
  结论:对于整体透明度图像来说,设置透明度对mask位值无影响.
  只有colorkey才会让相应的mask值为0
"""
