"""
   两个矩形碰撞原理演示程序_跟随鼠标移动的矩形.py
"""
import pygame
from pygame.locals import *

WIDTH,HEIGHT = 480,360
screen = pygame.display.set_mode((WIDTH,HEIGHT))

r1 = pygame.Rect(0,0,100,100)
r1.center = (WIDTH//2,HEIGHT//2) # r1在屏幕中央,宽高为100

r2 = pygame.Rect(0,0,50,50)      # r2先在左上角的位置

running = True
while running :
    event = pygame.event.poll()  # 从事件队列中取一个事件
    if event.type == QUIT:running = False

    x,y = pygame.mouse.get_pos()
    r2.center = x,y              # 跟随鼠标移动的矩形

    c1 = r2.right<r1.left
    c2 = r2.bottom<r1.top
    c3 = r2.left>r1.right
    c4 = r2.top>r1.bottom
    
    if  c1 or c2 or c3 or c4:
        pygame.display.set_caption("没有重叠")
    else:
        pygame.display.set_caption("重叠了")
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(180,180,0),r1,2)
    pygame.draw.rect(screen,(180,0,130),r2,2)
    
    pygame.display.update()

pygame.quit()

    
