"""
   矩形包含关系示例程序_跟随鼠标移动的矩形.py
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

    c1 = r1.left > r2.left       
    c2 = r1.right < r2.right
    c3 = r1.bottom  < r2.bottom
    c4 = r1.top > r2.top
    
    if  c1 and c2 and c3 and c4:
        pygame.display.set_caption("完全在里面了")
    else:
        pygame.display.set_caption("不完全在里面")
    
    screen.fill((0,0,0))        # 填充为黑色
    pygame.draw.rect(screen,(180,180,0),r1,2)
    pygame.draw.rect(screen,(180,0,130),r2,2)
    
    pygame.display.update()

pygame.quit()

    
