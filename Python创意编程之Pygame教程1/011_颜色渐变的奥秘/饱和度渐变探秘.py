"""
   饱和度渐变探秘.py
   本程序演示如何让颜色的饱和度部分产生渐变。
"""

import pygame

def satadd(color,ds):
    """
       color：pygame.Color实例化后的颜色
       ds：一个int,饱和增加的值
    """
    h,s,v,a = color.hsva  
    s = s + ds             # 色相增加
    s = min(100,s)         # 不能超过100
    s = max(0,s)           # 不能小于0
    color.hsva = h,s,v,a   # 设定颜色的hsva值 
    return color

width,height = 480,360
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("pygame饱和渐变探秘www.lixingqiu.com")

color = pygame.Color(255,0,0) # 饱和度已经是100了
radius = 50
for i in range(361):
    cors = i+radius,height//2
    pygame.draw.circle(screen,color,cors,radius)
    pygame.display.update()
    color = satadd(color,-1)
    print(color)

while not pygame.event.get(pygame.QUIT):
    pygame.display.update()
pygame.quit()

