"""
   pygame彩色渐变螺旋图.py
   本程序演示如何让颜色的色相部分产生渐变。
"""

import pygame
from math import *

def update_loop():
    """
       不断更新屏幕显示,直到按了关闭按钮就退出
    """
    while not pygame.event.get(pygame.QUIT):
        pygame.display.update()
    pygame.quit()

    
def coloradd(color,dh):
    """
       颜色增加函数，本函数把颜色的色相进行增加。其它指标不变。
       color：pygame.Color实例化后的颜色
       dh：一个int,色相增加的值
    """
    h,s,v,a = color.hsva   
    h = h + dh             # 色相增加
    h = h % 360            # 不能超过360
    color.hsva = h,s,v,a   # 设定颜色的hsva值 
    return color

width,height = 480,360
centerx,centery = width//2,height//2

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("pygame彩色渐变螺旋图www.lixingqiu.com")

color = pygame.Color('red')
radius = 1
angle = 0
for i in range(2200):
    x = centerx + radius * cos((radians(angle)))
    y = centery + radius * sin((radians(angle)))
    x,y = int(x),int(y)
    pygame.draw.circle(screen,color,(x,y),15)
    pygame.display.update()
    color = coloradd(color,1)
    radius += 0.1 
    angle += 1

update_loop()

