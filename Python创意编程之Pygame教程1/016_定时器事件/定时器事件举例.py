"""
   定时器事件举例
   本程序会定义一个自定义事件,它会每隔1秒发生一次。
   由于不在屏幕上显示什么，所以连update都省了。
"""
import time
import pygame
from pygame.locals import *

width ,height = 480,360

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("定时器事件举例")

PRINTEVENT = USEREVENT + 1
pygame.time.set_timer(PRINTEVENT,1000) # 设置事件每隔1秒发生

running = True
while running:
    for event in pygame.event.get():
        if event.type == PRINTEVENT:  # 如果是PRINTEVENT事件
            print(time.ctime())
        if event.type == QUIT:running = False

pygame.quit()
