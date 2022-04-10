"""
   重画矩形.py
"""

import pygame

RED = (255,0,0)
WIDTH,HEIGHT = 480,360

screen = pygame.display.set_mode((WIDTH,HEIGHT))

r1 = pygame.Rect(0,0,20,20)

dx ,dy = 20,20
for x in range(10):
    print(r1)
    pygame.draw.rect(screen,RED,r1) # 在screen上画矩形r1
    r1.move_ip(dx,dy)               # 水平位移dx和垂直位移dy
    pygame.display.update()         # 刷新屏幕显示
print(r1)                           # 打印最后r1

