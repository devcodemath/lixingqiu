"""
   生成图像到磁盘.py
"""
import pygame
from random import randint

width,height = 480,360
image = pygame.Surface((width,height))
image.fill((211,150,130))

# 打一些杂点
for i in range(1000):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    x = randint(0,width)
    y = randint(0,height)
    image.set_at((x,y),(r,g,b))

# 画一个圆形
center = width//2,height//2
pygame.draw.circle(image,(255,0,0),center,50)
pygame.image.save(image,"abcd.png")
    
