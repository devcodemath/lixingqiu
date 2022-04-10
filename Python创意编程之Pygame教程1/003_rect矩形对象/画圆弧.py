"""
   画圆弧.py
"""

import pygame         # 导入Pygame模块
from math import pi   # 导入pi

MAGENTA = (255,0,255)

WIDTH,HEIGHT = 480,360

left,top,width,height = 0,0,100,100
r1 = pygame.Rect(left,top,width,height)
r1.center = WIDTH//2,HEIGHT//2     # 重设矩形对象的中心点坐标

screen = pygame.display.set_mode((WIDTH,HEIGHT))

start_angle = 0
end_angle = pi/2
pygame.draw.arc(screen,MAGENTA,r1,start_angle,end_angle,2)

pygame.display.update()
