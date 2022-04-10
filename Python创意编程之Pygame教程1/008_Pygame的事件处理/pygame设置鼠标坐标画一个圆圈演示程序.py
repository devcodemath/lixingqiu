"""
   pygame控制鼠标坐标不断画一个彩色圆圈演示程序.py
"""
import math
import pygame
from pygame.locals import *
from random import randint

angle = 0
radius = 100
color = (255,0,0)
width,height = 480,360
wc,hc = width//2,height//2          # 屏幕中心点坐标
screen = pygame.display.set_mode((width,height))
image = pygame.Surface((width,height))

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get(): # 遍历每个事件
        if event.type == KEYDOWN: running = False

    x = wc + radius * math.cos(math.radians(angle))
    y = hc + radius * math.sin(math.radians(angle))
    x,y = int(x),int(y)
    pygame.mouse.set_pos((x,y))      # 控制鼠标
    pygame.draw.circle(image,color,(x,y),1)

    screen.fill((0,0,0))
    screen.blit(image,(0,0))
    pygame.display.update()
    angle = angle + 1
    if angle % 360 ==0 :
        image.fill((0,0,0))
        color = randint(0,255),randint(0,255),randint(0,255)
        angle = 0
    clock.tick(60)

pygame.quit()
