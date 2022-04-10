"""
   画线条.py
"""

import pygame         # 导入Pygame模块
from math import pi   # 导入pi

MAGENTA = (255,0,255)
WIDTH,HEIGHT = 480,360

screen = pygame.display.set_mode((WIDTH,HEIGHT))

start_pos = 100,100
end_pos1 = 200,100
end_pos2 = 200,200

pygame.draw.line(screen,MAGENTA,start_pos,end_pos1,5)
pygame.draw.aaline(screen,MAGENTA,start_pos,end_pos2)

pygame.display.update()
