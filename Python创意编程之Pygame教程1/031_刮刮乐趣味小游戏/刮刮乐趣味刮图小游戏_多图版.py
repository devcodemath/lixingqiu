"""刮刮乐趣味小游戏,这是一个有趣的小游戏,把别人的相片给刮出来,单击左键刮图,右键换下一张图片"""

__author__ = "李兴球"
__date__  = "2018/11/26"

import os
import pygame
from pygame.locals import *
from random import choice

def isimage(image):
    """通过判断扩展名来略微判断一个文件是否是图像,只支持列表中的图像"""
    ext = os.path.splitext(image)[-1] 
    if ext.lower() in [".gif",".jpg",".png",".jpeg",".bmp"]:
        return True
    else:
        return False
    
running = True
size = width,height= 800,600                 # 宽和高度
WHITE = (255,255,255,27)                     # 半透明白色
pygame.init()                                # 初始化pygame模块
screen = pygame.display.set_mode(size)       # 建立显示屏幕
pygame.display.set_caption("刮刮乐刮图趣味小游戏_作者:李兴球_风火轮少儿编程")  

path = os.getcwd() + os.sep + "图片"
photos = [ pygame.image.load(path + os.sep + image) for image in os.listdir(path) if isimage(image)]  
amounts = len(photos)
index = 0

sur = pygame.Surface(size).convert_alpha()                 #全是0,表现为黑色,(0, 0, 0, 255)
 
while running:
    event =  pygame.event.wait()
    if event.type == QUIT:running = False
    m_left,m_middle,m_right = pygame.mouse.get_pressed()   # 获取左,中,右键状态
    mx,my = pygame.mouse.get_pos()
    
    if m_left:pygame.draw.circle(sur,WHITE,(mx,my),50)     #半透明白色
    if m_right:                                            #按右键填充黑色,并且切换到下一张图片
        sur.fill((0,0,0))
        index = index + 1
        index = index % amounts
    
    if m_middle:running = False              #按中键退出循环
    screen.blit(photos[index],(0,0))         #相当于背景图
    screen.blit(sur,(0,0))
    pygame.display.update()
pygame.quit()
