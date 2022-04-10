"""
   灰度化图像.py
"""
import pygame
from random import randint

def gray_pixel(r,g,b):
    """灰度化像素"""

    h = int(r*0.299) + int(g*0.587) + int(b*0.114)
    
    return h,h,h

image = pygame.image.load('ultraman.jpg')
width,height = image.get_size()     # 获取宽高

for x in range(width):
    for y in range(height):
        pixel = image.get_at((x,y)) # 获取像素值        
        r,g,b,a = pixel             # 解包
        r,g,b = gray_pixel(r,g,b)   # 灰度化像素
        image.set_at((x,y),(r,g,b)) # 设定像素值

pygame.image.save(image,'ultraman_h.jpg') # 保存到文件



    
