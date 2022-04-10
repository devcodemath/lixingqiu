"""
   pygame.draw系列命令演示程序
"""

import pygame
from math import pi
 
# 初始化pygame引擎
pygame.init()
 
# 定义颜色常量
GRAY = (127,127,127)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)
BLUE =  ( 0,   0, 255)
GREEN = ( 0, 255, 0)
RED =  (255, 0, 0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
 
# 设置屏宽高
size = [400, 300]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("pygame.draw系列命令演示程序")
 
# 画一根线条,5个像素宽.
pygame.draw.line(screen, GREEN, [20, 20], [70,80], 5)

# 根据坐标点列表画一个不闭合的折线.
cors =[[0, 80], [50, 90], [200, 80], [220, 30]]
pygame.draw.lines(screen, GREEN, False, cors, 5)

# 画反锯齿线条
pygame.draw.aaline(screen, YELLOW, [0, 50],[50, 80], True)

# 画空心矩形,品红色
pygame.draw.rect(screen, MAGENTA, [75, 10, 50, 20], 2)
 
# 画一个填充白色的矩形
pygame.draw.rect(screen, WHITE, [150, 10, 50, 20])
 
# 画一个椭圆
pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2) 

# 画一个椭圆形
r = pygame.Rect(300, 10, 50, 20)
pygame.draw.ellipse(screen, RED,r) 

# 画一个多边形
pygame.draw.polygon(screen, GRAY, [[100, 100], [0, 200], [200, 200]], 5)

# 画4个弧形
pygame.draw.arc(screen, CYAN,[210, 75, 150, 125], 0, pi/2, 2)
pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)

# 画一个圆形,半径是50
pygame.draw.circle(screen, BLUE, [60, 250], 50)

# 更新显示
pygame.display.update()
