"""
   简易封面制作一例
   这个程序显示一个非常简单的游戏封面。
   按空格键可以“进入游戏”。
   本程序还主要演示了字体对象的使用方法。
   字体对象可以通过pygame.font.Font新建一个。
   它有render方法，把文字渲染后实际成了一个surface。
   正确运行本程序需要有msyh.ttf微软雅黑字体文件。
   还要准备一张图片，做个样子。
   
"""

import pygame
from pygame import *

def display_cover():
    """显示封面函数"""
    font_title = pygame.font.Font("msyh.ttf",32)
    font_little = pygame.font.Font("msyh.ttf",16)

    # 渲染标题到screen上
    title = font_title.render("风火轮编程游戏",True,GREEN)
    title_width = title.get_width()
    x = WIDTH//2-title_width//2
    y = 100
    screen.blit(title,(x,y))  # 把title合成到screen上

    # 渲染提示信息到screen上
    tip = font_little.render("按任意键开始游戏",True,GRAY)
    tip_width = tip.get_width()
    x = WIDTH//2 - tip_width//2
    y = HEIGHT - 100
    screen.blit(tip,(x,y))    # 渲染提示信息到screen上
    pygame.display.update()   # 最后刷新显示

def press_space_to_continue():
    """按空格键继续"""
    running = True    
    while running:
        for e in pygame.event.get():pass
        keys = pygame.key.get_pressed()
        running = not keys[K_SPACE]
    screen.fill(BGCOLOR)      # 填充screen
    pygame.display.update()   # 更新屏幕显示
    
def enter_game():
    """进入游戏，这里是显示一个画面，一个示意而已"""
    pygame.display.set_caption("雷霆沙赞游戏开始")
    shazam = pygame.image.load('shazam.jpg')
    screen.blit(shazam,(0,0))
    pygame.display.update()
    while not pygame.event.get(QUIT):pass
    pygame.quit()    
        
RED = (255,0,0)
GREEN = (0,255,0)
GRAY = (160,160,165)
BGCOLOR = (32,76,150)

WIDTH,HEIGHT = 512,589
pygame.init()

# 新建屏幕对象，它是最底层的surface
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BGCOLOR)
pygame.display.set_caption("简易封面制作")

display_cover()             # 显示封面

press_space_to_continue()   # 按空格键开始

enter_game()                # 进入游戏 




