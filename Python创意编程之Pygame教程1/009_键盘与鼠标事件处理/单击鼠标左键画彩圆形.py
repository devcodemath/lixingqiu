"""
   单击鼠标左键画彩色圆形.py
   简单的pygame示例程序,供大家学习。
"""
import pygame
from pygame.locals import *
from random import randint

screen = pygame.display.set_mode((480,360))
pygame.display.set_caption("单击鼠标左键画彩色圆形")

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT: running = False
        # 如果鼠标按下事件发生
        if event.type == MOUSEBUTTONDOWN:            
            if event.button == 1 :      # 如果是左键
                x,y = event.pos
                r = randint(0,255)      # 红色份量
                g = randint(0,255)      # 绿色份量
                b = randint(0,255)      # 蓝色份量
                radius = randint(10,50) # 半径
                pygame.draw.circle(screen,(r,g,b),(x,y),radius)   
      
    pygame.display.update()
pygame.quit()
