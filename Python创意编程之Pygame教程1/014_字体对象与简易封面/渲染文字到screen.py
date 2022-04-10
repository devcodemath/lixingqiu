"""
   渲染文字到screen
   
"""
import pygame
from pygame import *
        
RED = (250,60,15)
BGCOLOR = (32,76,150)
WIDTH,HEIGHT = 480,360

pygame.init()
# 新建屏幕对象，它是最底层的surface
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BGCOLOR)
pygame.display.set_caption("渲染文字到screen")

myfont = pygame.font.Font("msyh.ttf",32)
title = myfont.render("雷霆沙赞",True,RED)
w = title.get_width()         # 获取title宽度
x = WIDTH//2 - w//2           # 设定渲染的左上角x坐标
y = HEIGHT//2 -100            # 设定渲染的左上角y坐标
screen.blit(title,(x,y))      # 把title渲染到screen上  
pygame.display.update()       # 刷新屏幕显示



