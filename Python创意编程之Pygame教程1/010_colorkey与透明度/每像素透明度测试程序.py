"""
   pygame每像素透明度效果测试程序.py
   本程序中地球越往右透明度越低。
   它的透明度指标就是像素值中最后一个值。
   这个四元组中的这个值最大为255。
   越大，越不透明。那么在合成的时候它占的分量达到了100%。
   本程序充份说明了每像素透明度的概念。
"""
import pygame
from random import randint
from pygame.locals import *

def set_transparence(image):
    """给图像设置透明度"""
    width,height = image.get_size()
    
    for x in range(width):
        for y in range(height):         
            pixel = image.get_at((x,y))
            r,g,b,a = pixel
            if a > 0 : 
                a = x % 255    # 设置透明度值
                image.set_at((x,y),(r,g,b,a))
    
screen = pygame.display.set_mode((480,360))
pygame.display.set_caption("pygame每像素透明度效果测试程序")

# 转换为每个像素透明度都起作用的模式
ultraman = pygame.image.load('ultraman.jpg').convert_alpha()
earth = pygame.image.load("earth.png").convert_alpha()
width2 = earth.get_width()//2
height2 = earth.get_height()//2
set_transparence(earth)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT : running = False

    ms = pygame.mouse.get_pos() # 鼠标指针坐标
    center = ms[0] - width2,ms[1] - height2
    
    screen.blit(ultraman,(0,0))
    screen.blit(earth,center)
    pygame.display.update()

pygame.quit()

