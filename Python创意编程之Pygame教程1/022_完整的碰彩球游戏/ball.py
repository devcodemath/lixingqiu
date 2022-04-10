"""
   碰彩球游戏的Ball类。
   本程序定义了Ball类，它每次会在屏幕的中央生成，
   生成后，会向四周移动，你可以用鼠标指针去碰它。
   碰到了它后，小球就消失，并且会统计数量。
   如果有一个小球逃出屏幕，那么游戏就结束。
"""

import pygame
from random import *
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
    counter = 0                # 统计碰到鼠标指针的球的数量
    endflag = -1               # 游戏成功或失败的标志,1成功,0失败
    touched_amounts = 10       # 设定碰到球的总数量
    def __init__(self,image,group,screen):
        """
           image:球的图形,group:所在的组,screen:所在的屏幕
        """
        pygame.sprite.Sprite.__init__(self)# 初始化父类
        self.screen_rect = screen.get_rect() # 得到屏幕的矩形对象
        self.sw = screen.get_width()       # 获取屏幕宽度
        self.sh = screen.get_height()      # 获取屏幕高度
        self.image = image                 # 设定造 型 图
        self.rect = self.image.get_rect()  # 获取矩形对象
        self.rect.center = self.sw//2,self.sh//2
        self.speed = [randint(-4,4),randint(-4,4)]
        self.add(group)
        
    def update(self):
        """根据speed更新矩形对象"""
        self.rect.move_ip(self.speed)      # 移动矩形对象
        mpos = pygame.mouse.get_pos()      # 获取鼠标坐标
        if self.rect.collidepoint(mpos):   # 如果矩形对象碰到点 
            self.kill()
            Ball.counter += 1
            if Ball.counter == Ball.touched_amounts:
                Ball.endflag = 1  # 1代表成功
        # 检测小球是否不在屏幕内了
        outside = not self.screen_rect.contains(self.rect)
        if outside :
            self.kill()           # 如果出去了,就自杀
            Ball.endflag = 0      # 标志着游戏失败

if __name__ == "__main__":

    pass

        
