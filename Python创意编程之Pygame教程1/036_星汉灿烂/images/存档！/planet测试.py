"""
   宇宙类作品_星汉灿烂的行星与介绍类测试程序，
   playnet.py模块。
   ,本程序单击地球,会从右到左出现一张介绍地球的图片,
   再次单击,则图片又会从左到右慢慢消失。
"""

import pygame
from pygame.locals import *

class Intro(pygame.sprite.Sprite):
    """介绍对象,继承自pygame的角色类"""
    def __init__(self,image,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.sw = screen.get_width()
        self.rect = image.get_rect(topleft=(self.sw,0))
        self.visible = False
        self.dx = -1
        
    def update(self):
        """实时更新"""
        if self.visible and self.dx == -1:
            if self.rect.x > 0 :
               self.rect.move_ip(self.dx,0)
            else:
               clicked = pygame.mouse.get_pressed()
               if clicked[0] : self.dx = 1                  
        else:
            if self.rect.x < self.sw:
                self.rect.move_ip(self.dx,0)
            else:
                if self.visible:
                   print("运行了这")
                   self.visible = False
                   self.dx = -1 
        
class Planet(pygame.sprite.Sprite):
    """行星类,继承自pygame的角色类"""
    
    def __init__(self,image,pos,intro):
        """image:图形,pos:坐标,intro:介绍对象"""
        pygame.sprite.Sprite.__init__(self)
        self.intro = intro
        self.image = image
        w,h = image.get_size()    # 得到宽度和高度
        self.image_big = pygame.transform.scale(image,(w+10,h+10))
        self.rect = image.get_rect(center=pos)
        self.rect_big = self.image_big.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_big = pygame.mask.from_surface(self.image_big)
        self.images = [self.image,self.image_big]
        self.masks = [self.mask,self.mask_big]
        self.rects = [self.rect,self.rect_big]
        
    def update(self):
        mp = pygame.mouse.get_pos()
        dx = mp[0] - self.rect.x
        dy = mp[1] - self.rect.y
        if dx >= 0 and dx < self.rect.width and \
           dy >=0 and dy < self.rect.height:
               flag = self.mask.get_at((dx,dy))
               clicked = pygame.mouse.get_pressed()
               # 如果单击左键,把自己的介绍显示出来
               if clicked[0] : self.intro.visible = True
        else:
            flag = 0
        self.image = self.images[flag]
        self.rect = self.rects[flag]
        self.mask = self.masks[flag]                 
        
if __name__ == "__main__":

    size = width,height = 480,360
    earth_intro = pygame.image.load("images/地球介绍.png")
    earth = pygame.image.load("images/地球.png")
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("宇宙类作品_星汉灿烂的行星与介绍类测试 by lixingqiu")
    earth_intro = Intro(earth_intro,screen) # 地球介绍包装
    e = Planet(earth,(180,180),earth_intro) # 地球角色 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running=False
        e.update()
        earth_intro.update()
        screen.fill((0,0,0))
        screen.blit(e.image,e.rect)
        if earth_intro.visible:
            screen.blit(earth_intro.image,earth_intro.rect)
        pygame.display.update()

    pygame.quit()
    

        
        
