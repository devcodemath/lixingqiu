"""
   按鼠标滚轮缩放图像pygame示例
"""

import pygame
from pygame.locals import *

width,height = 680,660
pos = width//2,height//2
image = 'beauty.jpg'

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("按鼠标滚轮缩放图像pygame示例 www.lixingqiu.com")
image = pygame.image.load(image).convert_alpha()
rect = image.get_rect(center=pos)
image2 = image

w,h = image.get_width(),image.get_height()
k = h/w                                   # 高度和宽度之比
step = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:running = False
        if event.type == MOUSEBUTTONDOWN:

            if event.button ==4 :        # 向上滚动变大
                w = w + step
                h = int(w * k)
                image2 = pygame.transform.scale(image,(w,h))
                rect = image2.get_rect(center=pos)
                
            if event.button ==5 :         # 向下滚动变小
                w = w - step
                w = max(1,w)
                h = int(w * k)
                image2 = pygame.transform.scale(image,(w,h))
                rect = image2.get_rect(center=pos) 
    
    screen.fill((0,0,0))
    screen.blit(image2,rect)
    pygame.display.update()

pygame.quit()
            
