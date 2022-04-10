"""
   最简单的爆炸效果,
   本程序的本质是连续显示一些图形。
"""
import time
import pygame
from pygame.locals import *

def main():
    """
       主调用函数,本函数新建screen,
       通过切换几张图片显示一个爆炸效果
    """    
    width,height = size = 960,720
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("最简单的爆炸效果程序")

    # 要显示的图形
    images = [f"frames/{i}.gif" for i in range(6)]
    images = [pygame.image.load(im) for im in images]
    pos = width//2,height//2             # 爆炸点中心坐标

    # 下面的列表存储每幅帧图的矩形对象,它们的中心点都在pos这里
    rects = [im.get_rect(center=pos) for im in images]    
           
    index = 0                            # 第一个帧图的索引号
    amounts = len(images)                # 造型总数量
    clock = pygame.time.Clock()          # 新建时钟对象
    start_time = time.time()             # 爆炸起始时间 
    running = True
    while running:
        # 超时就让索引增加1
        if time.time() - start_time >= 0.1 :
            index = index + 1
            if index == amounts-1 : running = False 
            start_time = time.time()            
        
        screen.fill((60,0,160))
        screen.blit(images[index],rects[index])    
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    
if __name__ == "__main__":

    main()
