"""
   surface整体透明度测试程序.py
   用surface的set_alpha设定透明度。
   这种情况的透明度只能给图像设置一个整体透明度。
   不象每像素透明度设置那样可以精确到每一个像素的a值来给图像设置透明度。
"""
import pygame
from random import randint
from pygame.locals import *
    
screen = pygame.display.set_mode((480,360))
pygame.display.set_caption("surface整体透明度测试程序 www.lixingqiu.com")

# ultraman做为背景
ultraman = pygame.image.load('ultraman.png').convert()
superman = pygame.image.load("superman.jpg").convert()
width2 = superman.get_width()//2
height2 = superman.get_height()//2
superman.set_alpha(127)    # 设置整体透明度

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT : running = False

    ms = pygame.mouse.get_pos()   # 获取鼠标指针坐标
    center = ms[0] - width2,ms[1] - height2
    
    screen.blit(ultraman,(0,0))   # 奥特曼合成到screen
    screen.blit(superman,center)  # 超人合成到screen
    pygame.display.update()

pygame.quit()

