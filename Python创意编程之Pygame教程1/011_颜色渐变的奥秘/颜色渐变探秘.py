"""
   颜色渐变探秘.py
   本程序演示如何让颜色的色相部分产生渐变。
"""

import pygame

def coloradd(color,dh):
    """
       颜色增加函数，本函数把颜色的色相进行增加。其它指标不变。
       color：pygame.Color实例化后的颜色
       dh：一个int,色相增加的值
    """
    h,s,v,a = color.hsva  ; print(color,' = ',h,s,v,a)
    h = h + dh             # 色相增加
    h = h % 360            # 不能超过360
    color.hsva = h,s,v,a   # 设定颜色的hsva值 
    return color

width,height = 480,360
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("pygame颜色渐变探秘www.lixingqiu.com")

color = pygame.Color('red')
radius = 50
for i in range(361):
    cors = i+radius,height//2
    pygame.draw.circle(screen,color,cors,radius)
    pygame.display.update()
    color = coloradd(color,1)

while not pygame.event.get(pygame.QUIT):
    pygame.display.update()
pygame.quit()

