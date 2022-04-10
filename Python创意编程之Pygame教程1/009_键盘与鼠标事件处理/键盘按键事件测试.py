"""
   键盘按键事件测试程序.py
"""

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((480,360))
pygame.display.set_caption("键盘按键事件测试")

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:print("空格键")
            if event.key == K_RETURN:print("回车键")
            
        if event.type == QUIT:running = False
        
    keys = pygame.key.get_pressed()    # 按键表
    if keys[K_UP] : print("向上方向箭头")
    if keys[K_DOWN] : print("向下方向箭头")
    if keys[K_LEFT] : print("向左方向箭头")
    if keys[K_RIGHT] : print("向右方向箭头")

    pygame.display.update()
pygame.quit()
