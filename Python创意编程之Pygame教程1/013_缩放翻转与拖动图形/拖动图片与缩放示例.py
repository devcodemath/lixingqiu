"""
   拖动图片与缩放示例
   稍微改下这个程序就能制作一个图片查看器了.
   
"""

import pygame
from pygame.locals import *

width,height = 680,660
pos = [width//2,height//2]
image = 'beauty.jpg'

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("拖动图片与缩放示例www.lixingqiu.com")
image = pygame.image.load(image).convert_alpha()
rect = image.get_rect(center=pos)
image2 = image

w,h = image.get_width(),image.get_height()
k = h/w                                   # 高度和宽度之比
step = 10
start_drag = 0
running = True
while running:
    for event in pygame.event.get():
              
        if event.type == QUIT:running = False
        
        if event.type == MOUSEBUTTONDOWN:

            if event.button ==4 :            # 向上滚动变大
                w = w + step
                h = int(w * k)
                image2 = pygame.transform.scale(image,(w,h))
                rect = image2.get_rect(center=pos)                
            if event.button ==5 :          # 向下滚动变小
                w = w - step
                w = max(1,w)
                h = int(w * k)
                image2 = pygame.transform.scale(image,(w,h))
                rect = image2.get_rect(center=pos)
            if event.button == 1:
                start_drag = 1                # 开始拖动
                
        if event.type == MOUSEBUTTONUP:
            start_drag = 0                    # 结束拖动
        if event.type == MOUSEMOTION:
            c = rect.collidepoint(event.pos)  # 鼠标指针在图像rect内
            if start_drag == 1 and c:
                pos[0] += event.rel[0]        # 水平方向相对移动量
                pos[1] += event.rel[1]        # 垂直方向相对移动量
                rect.center = pos                    

        screen.fill((0,0,0))
        screen.blit(image2,rect)
        pygame.display.update()

pygame.quit()
            
