"""
   鼠标移动方块的mask碰撞检测原理示例程序
"""
import pygame
from pygame.locals import * 

pygame.init()
screen = pygame.display.set_mode((480,360))
pygame.display.set_caption("鼠标移动方块的mask碰撞检测原理示例程序by 李兴球")
# 静止不动的红色方块
width,height = 50,50
x1,y1 = 100,100
redsquare = pygame.Surface((width,height)).convert_alpha()
redsquare.fill((255,10,10,228))                # 最后的0代表完全透明
redsquare_rect = redsquare.get_rect(topleft=(x1,y1))  # 定位
redmask = pygame.mask.from_surface(redsquare)  # 取掩膜

# 用鼠标移动的蓝色方块
x2,y2 = pygame.mouse.get_pos()
bluesquare = pygame.Surface((width,height)).convert_alpha()
bluesquare.fill((10,10,255))
bluesquare_rect = bluesquare.get_rect(topleft=(x2,y2)) # 定位
bluemask = pygame.mask.from_surface(bluesquare) # 取掩膜

running=True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:running=False

    x2,y2  = pygame.mouse.get_pos()
    bluesquare_rect.topleft = (x2,y2 )
    offset = x1 -x2 , y1 - y2
    # 返回的p是相对于bluemask的偏移量
    p = bluemask.overlap(redmask,offset)
    if p:
        碰撞点 = bluesquare_rect.x + p[0],bluesquare_rect.y + p[1]
        info = "offset=" + str(offset) + ",p=" + str(p) + ",碰撞点坐标:" + str(碰撞点)
        pygame.display.set_caption(info)
    else:
        pygame.display.set_caption("无碰撞")
    screen.fill((0,0,0))
    screen.blit(redsquare,redsquare_rect)
    screen.blit(bluesquare,bluesquare_rect)     # 贴到屏幕

    pygame.display.update()

pygame.quit()

