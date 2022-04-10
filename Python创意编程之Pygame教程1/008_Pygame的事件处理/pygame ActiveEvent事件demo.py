"""
   ActiveEvent事件demo.py
"""
import pygame
from pygame.locals import *

width,height = 480,360
screen = pygame.display.set_mode((width,height))

running = True
while running:
    for event in pygame.event.get(): # 遍历每个事件
        if event.type == ACTIVEEVENT :
            if event.gain == 0 :
                pygame.display.set_caption("鼠标指针不在窗口内")
            if event.gain == 1 :
                pygame.display.set_caption("鼠标指针在窗口内")            

        if event.type == QUIT: running = False

    screen.fill((0,0,0))

    pygame.display.update()

pygame.quit()
