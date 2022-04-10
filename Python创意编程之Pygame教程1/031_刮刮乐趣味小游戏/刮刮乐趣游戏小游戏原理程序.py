"""
   刮刮乐趣味小游戏原理程序。
   本程序运行较慢，这是由于逐像素修改所引起的。
   
   它的原理是把black_mask的像素改为透明像素。
   读者完全可以把它改造成自己的刮刮乐小游戏。
"""
__author__ = "李兴球"
__date__  = "2018/11/26"

def refresh():
    """刷新显示，在这个过程中无法关闭pygame。"""
    pygame.event.get()            # 加这句防窗口未响应
    screen.blit(background,(0,0)) # 在screen上渲染背景图
    screen.blit(black_mask,(0,0)) # 用于"盖"住background
    pygame.display.update()
    clock.tick(30)

import pygame
from pygame.locals import * 

size = width,height= 800,600             # 定义屏幕尺寸变量
透明色 = (0,0,0,0)                       # 全透明色
pygame.init()                            # 初始化pygame模块
screen = pygame.display.set_mode(size)   # 建立显示屏幕
pygame.display.set_caption("刮刮乐趣游戏小游戏原理程序") # 标题
background = pygame.image.load("图片/鸟.png")  # 加载图像

clock = pygame.time.Clock()
# 建立每像素模式的surface，用来蒙住它下面的图片。
black_mask = pygame.Surface(size).convert_alpha()
refresh()
# 下面开始填充矩形区域的像素为透明色
for x in range(300,601):
    for y in range(100,401):
        black_mask.set_at((x,y),透明色)
        refresh()

while not pygame.event.get(QUIT):clock.tick(30)   
pygame.quit()
