"""
   反转像素_反相基本原理演示程序.py
"""
import pygame
from random import randint

def convert_pixel(r,g,b):
    """反转像素"""
    r = 255 - r
    g = 255 - g
    b = 255 - b
    return r,g,b

image = pygame.image.load('ultraman.jpg')
width,height = image.get_size()     # 获取宽高

for x in range(width):
    for y in range(height):
        pixel = image.get_at((x,y)) # 获取像素值        
        r,g,b,a = pixel             # 解包
        r,g,b = convert_pixel(r,g,b)# 反转像素
        image.set_at((x,y),(r,g,b)) # 设定像素值

pygame.image.save(image,'ultraman_c.jpg') # 保存到文件



    
