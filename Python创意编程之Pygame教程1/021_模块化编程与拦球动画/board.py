"""
   Board类的代码,跟随鼠标指针左右移动的矩形。
"""

import pygame

class Board(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        """初始化方法,size:宽高,pos:坐标"""
        pygame.sprite.Sprite.__init__(self) # 初始化父类
        self.image = pygame.Surface(size)   # 新建图形
        self.image.fill((13,223,223))       # 填充图形
        self.rect = self.image.get_rect(center=pos)
  
    def update(self):
        """更新拦板的坐标"""
        mpos = pygame.mouse.get_pos() # 获取鼠标指针坐标
        self.rect.centerx = mpos[0]   # 设置矩形中央x坐标      

if __name__ == "__main__":

    pass
