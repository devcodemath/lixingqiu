"""
   画出矩形.py
"""

import pygame         # 导入Pygame模块

left,top,width,height = 10,10,100,100

# 新建一个左上角坐标为(10,10),宽高为(100,100)的矩形
r1 = pygame.Rect(left,top,width,height)

screen = pygame.display.set_mode((480,360))

pygame.draw.rect(screen,(255,0,0),r1,1)

pygame.display.update()
