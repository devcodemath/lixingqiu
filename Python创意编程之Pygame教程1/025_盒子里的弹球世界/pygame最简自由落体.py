"""
   最简单自由落体弹球实验,这个程序演示一个红色的小球掉到屏幕下方。
"""
import pygame
from pygame.locals import *

size = width,height = 480,360
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame最简自由落体运动")

radius = 20    # 小球半径
x = width//2   # 初始x坐标
y = 10         # 初始y坐标
dx = 0         # 水平速度
dy = 0         # 垂直速度
a =  1         # 加速度

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:running=False
    # 更新小球的坐标
    y = y + dy                # y坐标增加dy
    if y < height:            # 相当于到下边缘碰撞检测             
       dy = dy + a            # dy增加a
    else:
       dy = -dy
       
    screen.fill((0,0,0))      # 填充背景
    pygame.draw.circle(screen,(255,0,0),(x,y),radius)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
