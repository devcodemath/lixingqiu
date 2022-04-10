"""
   pygame.event.poll demo获取事件演示程序.py
"""
import pygame
from pygame.locals import *

width,height = 480,360            #　设定分辨率
screen = pygame.display.set_mode((width,height))

running = True
while running:
    
    event = pygame.event.wait()   # 获取一个事件
    print(event)
    if event.type == QUIT:
        running = False
    
    screen.fill((0,0,0))          # 填充screen为黑色

    pygame.display.update()

pygame.quit()
