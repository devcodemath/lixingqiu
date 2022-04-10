"""
   创建圆环和实心圆，把它们渲染到screen上的同一个坐标。
   这样，小圆是在大圆里面，它们是没有碰撞在一起的，但
   用矩形碰撞命令来进行检测的时候，会显示它们是重叠的。
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
print(hollow_circle.get_at((1,1)))
pos = width1//2,height1//2                # 画圆中心坐标
rect1 = hollow_circle.get_rect(center=(w//2,h//2))
pygame.draw.circle(hollow_circle,red,pos,radius1,10)
screen.blit(hollow_circle,rect1)

# 创建小的实心圆
radius2 = 10
width2,height2 = 2 * radius2,2 * radius2
solid_circle = pygame.Surface((width2,height2),SRCALPHA)
pos = width2//2,height2//2                # 画圆中心坐标
rect2 = solid_circle.get_rect(center=(w//2,h//2))
pygame.draw.circle(solid_circle,blue,pos,radius2)
screen.blit(solid_circle,rect2)

collision = rect2.colliderect(rect1)
print("碰撞=",collision)
pygame.display.update()
 
