"""
   鼠标移动蓝色圆形动态碰撞检测示例程序。
   本例是用基于mask的overlape命令,从而检测出两个圆形有没有碰撞的。
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
# 新建全透明图形
hollow_circle = pygame.Surface((width1,height1),SRCALPHA)
pos = width1//2,height1//2                # 画圆中心坐标
rect1 = hollow_circle.get_rect(center=(w//2,h//2))
pygame.draw.circle(hollow_circle,red,pos,radius1,10)
mask1 = pygame.mask.from_surface(hollow_circle)

# 创建小的实心圆
radius2 = 10
width2,height2 = 2 * radius2,2 * radius2
solid_circle = pygame.Surface((width2,height2),SRCALPHA)
pos = width2//2,height2//2                # 画圆中心坐标
rect2 = solid_circle.get_rect(center=(w//2,h//2))
pygame.draw.circle(solid_circle,blue,pos,radius2)
mask2 = pygame.mask.from_surface(solid_circle)

running = True
while running:
    for event in pygame.event.get():
        if event.type in [KEYDOWN,QUIT,]:running=False
        
    mpos = pygame.mouse.get_pos()        # 获取鼠标指针
    rect2.center = mpos                  # 把rect2中心点设为mpos
    offset = rect2.x - rect1.x ,rect2.y - rect1.y # 计算偏移值
    p = mask1.overlap(mask2,offset)      # 计算是否重叠
    if p:
        pos = rect1.x + p[0],rect1.y + p[1]
        info = str(p)+ ",碰撞点相对于屏幕的坐标:"+ str(pos)
        pygame.display.set_caption(info)
    else:
        pygame.display.set_caption('没有碰撞')
    screen.fill((0,0,0))
    screen.blit(hollow_circle,rect1)
    screen.blit(solid_circle,rect2)    
    pygame.display.update()
pygame.quit()
 
