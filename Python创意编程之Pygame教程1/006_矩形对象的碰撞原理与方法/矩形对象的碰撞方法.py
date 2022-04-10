"""
   矩形对象的点与矩形碰撞.py
"""
import pygame
from pygame.locals import *

WIDTH,HEIGHT = 480,360
screen = pygame.display.set_mode((WIDTH,HEIGHT))

r = pygame.Rect(0,0,100,100)
r.center = (WIDTH//2,HEIGHT//2)

running = True
while running :
    event = pygame.event.poll()  # 从事件队列中取一个事件
    if event.type == QUIT:running = False

    x,y = pygame.mouse.get_pos()
    if x > r.left and x < r.right and y > r.top and y < r.bottom:
        print('在矩形范围')
    else:
        print("不在矩形范围内")

    pygame.draw.rect(screen,(100,0,0),r,2)
    pygame.display.update()

pygame.quit()

    
