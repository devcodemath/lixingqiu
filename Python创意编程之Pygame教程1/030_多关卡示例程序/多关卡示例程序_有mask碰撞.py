"""
   最简采用mask进行碰撞检测的多关卡示例程序
"""

import pygame
from pygame.locals import *

width,height = size = 480,360
screen = pygame.display.set_mode(size)
pygame.display.set_caption("最简采用mask进行碰撞检测的多关卡示例程序by李兴球")

# 背景与其mask代码段
level_index = 0
level_images = [f"levels/level{i}.png" for i in range(5)]
level_images = [pygame.image.load(im) for im in level_images]
level_masks = [pygame.mask.from_surface(im) for im in level_images]
level_amounts = len(level_images)
bg_image = level_images[level_index]
bg_mask = level_masks[level_index]

# 蓝球角色代码段
sprite = "basketball.png"      # 需要操作的蓝球角色
sprite = pygame.image.load(sprite)
sprite_mask = pygame.mask.from_surface(sprite)# 角色的mask
pos = (25,280)
sprite_rect = sprite.get_rect(center=pos)
dx, dy = 0, 0                  # 水平和垂直速度

# 游戏主循环代码段
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:running=False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:dx,dy = 1,0
            if event.key == K_LEFT:dx,dy = -1,0
            if event.key == K_UP:dx,dy = 0,-1
            if event.key == K_DOWN:dx,dy = 0,1
        if event.type == KEYUP:dx,dy = 0,0
        
    sprite_rect.move_ip(dx,dy)    # 水平和垂直方向移动矩形对象
    
    # 下面是进行mask的overlap检测
    offset = sprite_rect.topleft
    cor = bg_mask.overlap(sprite_mask,offset)
    pygame.display.set_caption(str(offset) + ":" + str(cor))
    if cor : sprite_rect.move_ip(-dx,-dy)
        
    if sprite_rect.left>= width : # 超过最右边界
        level_index += 1          # 关卡索引号加1
        if level_index < level_amounts:
            bg_image = level_images[level_index] # 更换背景
            bg_mask = level_masks[level_index]   # 更换掩膜
            sprite_rect.left = 0
        else:
            running = False
    screen.fill((250,250,220))
    screen.blit(bg_image,(0,0))
    screen.blit(sprite,sprite_rect)
    pygame.display.update()
pygame.quit()

        
            
    
