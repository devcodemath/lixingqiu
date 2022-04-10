"""
   按左右方向箭头设置整体透明度.py。
   本程序按左键透明度会增加,按右键透明度会减小。
   
"""
import pygame
from random import randint
from pygame.locals import *

width,height = 480,360

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("surface整体透明度测试程序")

# ultraman做为背景
ultraman = pygame.image.load('ultraman.png').convert()
superman = pygame.image.load("superman.jpg").convert()
width2 = superman.get_width()//2
height2 = superman.get_height()//2
# 把超人贴到屏幕中央坐标
center = width//2 - width2,height//2 -height2

alpha = 127
superman.set_alpha(alpha)    # 设置整体透明度

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:         # 如果按下某键
            if event.key == K_LEFT:
                alpha -= 1
                alpha = max(0,alpha)
                superman.set_alpha(alpha) # 设置整体透明度
                pygame.display.set_caption(str(alpha))
            if event.key == K_RIGHT:
                alpha += 1
                alpha = min(alpha,255)
                superman.set_alpha(alpha) # 设置整体透明度
                pygame.display.set_caption(str(alpha))
                
        if event.type == QUIT : running = False
    
    screen.blit(ultraman,(0,0))   # 奥特曼合成到screen
    screen.blit(superman,center)  # 超人合成到screen
    pygame.display.update()

pygame.quit()

