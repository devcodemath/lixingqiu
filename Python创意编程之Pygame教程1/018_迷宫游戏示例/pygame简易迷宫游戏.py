"""
   简易迷宫游戏。本程序演示一个非常简单的迷宫游戏原理。
   采用mask进行碰撞检测,并且会打印出碰撞点的像素值。
"""
import pygame
from pygame.locals import *

RED = (255,0,0)
GREEN = (0,255,0)

pygame.init()

# 创建屏幕与迷宫
maze = pygame.image.load("maze.png")
w,h, = size = maze.get_size()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame简易迷宫游戏by lixingqiu")
rect1 = maze.get_rect()
mask1 = pygame.mask.from_surface(maze)

# 创建角色
radius2 = 5
width2,height2 = 2 * radius2,2 * radius2
sprite = pygame.Surface((width2,height2),SRCALPHA)
pos = width2//2,height2//2                # 画圆中心坐标
rect2 = sprite.get_rect(center=(w//2,h//2))
pygame.draw.circle(sprite,GREEN,pos,radius2)
mask2 = pygame.mask.from_surface(sprite)
dx ,dy = 0, 0 

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:running=False
        if event.type == KEYUP:
            dx ,dy = 0, 0
    keys = pygame.key.get_pressed()
    if keys[K_UP]   : dx = 0 ; dy = -2
    if keys[K_DOWN] : dx = 0 ; dy =  2
    if keys[K_LEFT] : dx = -2 ; dy = 0
    if keys[K_RIGHT] : dx = 2 ; dy =  0
    rect2.move_ip(dx,dy)

    offset = rect1.x - rect2.x ,rect1.y - rect2.y # 计算偏移值
    p = mask2.overlap(mask1,offset)               # 计算是否重叠
    
    if p:
        pos = rect2.x + p[0],rect2.y + p[1]       # 碰撞点坐标
        pygame.display.set_caption(str(p) + ",碰撞点坐标:" + str(pos))
        print("碰撞点RGB值:", maze.get_at(pos))# 检测像素值,如果是绿色则结束!
        rect2.move_ip(-dx,-dy)                   # 退回原处，所以不能穿墙
    else:
        pygame.display.set_caption('没有碰撞')
    screen.fill((255,255,255))
    screen.blit(maze,rect1)
    screen.blit(sprite,rect2)    
    pygame.display.update()
pygame.quit()
 
