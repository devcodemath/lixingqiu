"""
   刮刮乐趣味小游戏单图版。
   这是一个有趣的小游戏,在游戏启动时是全黑色的，
   但是可以通过拖动鼠标指针来把相片给“刮”出来。
"""
__author__ = "李兴球"
__date__  = "2018/11/26"

import pygame
from pygame.locals import * 

size = width,height= 800,600             # 定义屏幕尺寸变量
透明色 = (0,0,0,0)                       # 全透明色
pygame.init()                            # 初始化pygame模块
screen = pygame.display.set_mode(size)   # 建立显示屏幕
pygame.display.set_caption("刮刮乐趣味小游戏单图版") # 标题
background = pygame.image.load("图片/鸟.png")  # 加载图像

# 建立每像素模式的surface，用来蒙住它下面的图片。
black_mask = pygame.Surface(size).convert_alpha()  
running = True
while running:
    event =  pygame.event.wait()
    if event.type == QUIT:running = False
    m_left,m_middle,m_right = pygame.mouse.get_pressed()
    mx,my = pygame.mouse.get_pos()        # 获取鼠标指针坐标 
    
    # 按左键，在black_mask上面画半透明的圆形。
    if m_left:pygame.draw.circle(black_mask,透明色,(mx,my),20)
    if m_right:black_mask.fill((0,0,0))  # 按右键填充黑色
    if m_middle:running = False          # 按中键退出循环
    
    # 渲染图形，注意顺序
    screen.blit(background,(0,0))        # 在screen上渲染图片
    screen.blit(black_mask,(0,0))        # 用于"盖"住background
    pygame.display.update()
pygame.quit()
