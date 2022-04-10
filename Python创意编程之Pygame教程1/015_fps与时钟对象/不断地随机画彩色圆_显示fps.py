
"""
   不断地随机画彩色圆_显示fps
   本程序会在屏幕上不断地画彩色的圆圈，并且会显示fps值。
"""
import pygame
from random import randint

def random_draw_circle(surface,pos):
    """
       在surface上不断地画彩色圆圈
    """
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    radius = randint(1,100)
    pygame.draw.circle(surface,(r,g,b),pos,radius)
    
width,height = 480,360
pygame.init() 
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("不断地随机画彩色圆_显示fps")
sur = pygame.Surface((width,height))

myfont = pygame.font.Font("msyh.ttf",32)
title = myfont.render("FPS是：",True,(255,0,0))
w,h = title.get_size()

running = True
clock = pygame.time.Clock()
while running:    
    fps = clock.get_fps()             # 得到fps    
    for event in pygame.event.get():  # 遍历每个事件 
        if event.type == pygame.QUIT:running = False
    
    pos = randint(0,width),randint(0,height)
    random_draw_circle(sur,pos)      # 随机画圆
    title = myfont.render("FPS是：" + str(fps),True,(255,0,0))
    w,h = title.get_size()                
    
    screen.fill((0,0,0))             # 填充背景颜色
    screen.blit(sur,(0,0))
    screen.blit(title,(width//2-w//2,height//2-h//2)) 
    pygame.display.update()
    clock.tick(60)                  # 设定fps
    
pygame.quit()
