"""
   每隔1秒印一个彩色格子,自定义事件,按行和列数均分矩形对象函数。
   当然下面的程序直接设置等待1秒钟也可以实现同样的功能,但是这样就阻塞了程序的运行.
   在游戏循环中是不可取的,设置定时器才是最佳方案。
   
"""
import pygame
from pygame.locals import * 
from random import randint

def split_rect(rect,rows,cols):
    """
     均分矩形对象，rect是四元组，rect[0]是左上角x坐标，
     rect[1]是左上角y坐标， rect[2]是宽度，rect[3]是高度
     rect：源矩形，rows：行数，cols：列数
     返回列表
     """
    rect_list = [] 
    width = rect[2]
    height = rect[3]
    row_height = height//rows   # 行高
    col_width = width//cols     # 列宽
    x = 0
    y = 0
    for r in range(0,rows):
        for c in range(0,cols):           
            rect = (x,y,col_width,row_height)
            rect_list.append(rect)
            x = x +  col_width 
        x = 0
        y = y +  row_height 
    return rect_list

def save_image_frame(image,index):
    """保存图像帧，用来做gif"""
    pygame.image.save(image,"frames/" + str(index) + ".png")
    
width,height = 400,400
rows,cols = 20,20
amounts = rows * cols
rect = (0,0,width,height)
rect_list = split_rect(rect,20,20)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("自定义事件_每隔1秒印一个彩色格子")

image = pygame.Surface((width,height))

STAMPEVENT = USEREVENT + 2            # 自定义事件
pygame.time.set_timer(STAMPEVENT,10) # 设置定时器

index = 0                             # 也可以不用index
running = True                        # 直接pop(0)，直到为空
while running:
    for event in pygame.event.get():
        if event.type == QUIT:running = False
        if event.type == STAMPEVENT and index < amounts:
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            print('index=',index)
            rect = rect_list[index]
            image.fill((r,g,b),rect=pygame.Rect(*rect))
            save_image_frame(image,index)
            screen.blit(image,(0,0)) # 没必要每帧都贴下到screen
            pygame.display.update()  # 没必要每帧都更新screen
            index = index + 1
            if index == amounts :
                pygame.time.set_timer(STAMPEVENT,0) # 取消定时器
                print('印彩色格子完毕！')    

pygame.quit()
            
pygame.image.save(image,"c:/每隔一秒印彩色格子动画演示.png")
