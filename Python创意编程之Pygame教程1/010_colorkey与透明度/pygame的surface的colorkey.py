"""
   pygame的surface的colorkey.py
   当一个图像要渲染到另一个图像上时,我们可以选择某种颜色不渲染。
   这种颜色就叫colorkey。
   如果图像是每像素格式，那么设置的colorkey无效。
   
"""
import pygame
from random import randint
from pygame.locals import *
    
screen = pygame.display.set_mode((480,360))
pygame.display.set_caption("colorkey测试程序")

# ultraman做为背景
ultraman = pygame.image.load('ultraman.png').convert()
superman = pygame.image.load("superman.jpg").convert()

superman.set_colorkey((0,0,0))  # 设置不渲染的颜色
pos = 80,00
ultraman.blit(superman,pos)     # 把超人贴到ultraman上
screen.blit(ultraman,(0,0))     # 把ultraman贴到screen上
pygame.display.update()         # 更新显示



