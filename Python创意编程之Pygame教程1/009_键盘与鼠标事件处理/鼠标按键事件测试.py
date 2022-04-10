"""
   鼠标按键事件测试程序.py
"""
import pygame
from pygame.locals import *

screen = pygame.display.set_mode((480,360))
pygame.display.set_caption("鼠标按键事件测试")

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT: running = False
        
        if event.type == MOUSEMOTION: print("鼠标指针坐标：",event.pos)
        
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 : print('左键按下')
            if event.button == 2 : print('中键按下')
            if event.button == 3 : print('右键按下')
            if event.button == 4 : print('向上滚动开始')
            if event.button == 5 : print('向下滚动开始')
            
        if event.type == MOUSEBUTTONUP:
            if event.button == 1 : print('左键弹起')
            if event.button == 2 : print('中键弹起')
            if event.button == 3 : print('右键弹起')
            if event.button == 4 : print('向上滚动结束')
            if event.button == 5 : print('向下滚动结束')
            
    m1,m2,m3 = pygame.mouse.get_pressed()
    if m1 : print("按了鼠标左键")
    if m2 : print("按了鼠标中键")
    if m3 : print("按了鼠标右键")

    # x,y = pygame.mouse.get_pos()
    # print("鼠标指针坐标为：(",x,",",y,")")    
      
    pygame.display.update()
pygame.quit()
