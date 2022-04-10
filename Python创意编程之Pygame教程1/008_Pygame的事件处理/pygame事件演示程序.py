"""
   pygame事件演示程序.py
"""
import pygame
from pygame.locals import *

width,height = 480,360
screen = pygame.display.set_mode((width,height))

running = True
while running:
    for event in pygame.event.get(): # 遍历每个事件
        print(event)        # 打印此事件的字符串形式
        print(event.type,'\n' * 3)

        if event.type == QUIT: running = False

    screen.fill((0,0,0))

    pygame.display.update()

pygame.quit()
