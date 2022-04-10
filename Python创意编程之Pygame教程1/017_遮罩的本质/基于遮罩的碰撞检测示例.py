"""
   创建圆环和实心圆，把它们渲染到screen上的同一个坐标。
   这样，小圆是在大圆里面，它们是没有碰撞在一起的。
   本例是用基于mask的overlape命令,从而检测出它们是没有重叠的。
"""
import pygame
from pygame.locals import *

red = (255,0,0)
blue = (0,0,255)
w,h, = size = 480,360
pygame.init()
screen = pygame.display.set_mode(size)

# 创建大的圆环
radius1 = 50
width1,height1 = 2*radius1,2*radius1
hollow_circle = pygame.Surface((width1,height1),SRCALPHA)
pos = width1//2,height1//2                # 画圆中心坐标
rect1 = hollow_circle.get_rect(center=(w//2,h//2))
pygame.draw.circle(hollow_circle,red,pos,radius1,10)
mask1 = pygame.mask.from_surface(hollow_circle)
screen.blit(hollow_circle,rect1)

# 创建小的实心圆
radius2 = 10
width2,height2 = 2 * radius2,2 * radius2
solid_circle = pygame.Surface((width2,height2),SRCALPHA)
pos = width2//2,height2//2                # 画圆中心坐标
rect2 = solid_circle.get_rect(center=(w//2,h//2))
pygame.draw.circle(solid_circle,blue,pos,radius2)
mask2 = pygame.mask.from_surface(solid_circle)
screen.blit(solid_circle,rect2)

offset = rect2.x - rect1.x ,rect2.y - rect1.y
p = mask1.overlap(mask2,offset)
print(p)
pygame.display.update()
 
