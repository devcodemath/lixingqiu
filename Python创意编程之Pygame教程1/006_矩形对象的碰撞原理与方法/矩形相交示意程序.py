"""
   矩形相交示意程序.py
"""
import pygame
from pygame.locals import *

WIDTH,HEIGHT = 480,360
screen = pygame.display.set_mode((WIDTH,HEIGHT))

r1 = pygame.Rect(0,0,100,100)  # 左上角为(0,0),宽高为(100,100)的矩形

r2 = pygame.Rect(0,0,200,200)  # r2先在左上角的位置
r2.center = (WIDTH//2,HEIGHT//2)

running = True
while running :
    event = pygame.event.poll()  # 从事件队列中取一个事件
    if event.type == QUIT:running = False

    x,y = pygame.mouse.get_pos()
    r1.center = x,y              # 跟随鼠标移动的矩形


    # 以下意思是说r2没有包括r1,但是r2和r1重叠了
    if  not r2.contains(r1) and r2.colliderect(r1):
        pygame.display.set_caption("相交")
    else:
        pygame.display.set_caption("不相交")
    
    screen.fill((0,0,0))        # 填充为黑色
    pygame.draw.rect(screen,(180,180,0),r1,2)
    pygame.draw.rect(screen,(180,0,130),r2,2)
    
    pygame.display.update()

pygame.quit()

    
