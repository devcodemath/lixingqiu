"""
   NPC多造型角色_可爱的Pico的AnimatedSprite类。
   本程序会演示一个小人物走来走去，它碰到屏幕边缘会反弹。
   
"""
import time
import pygame
from pygame.locals import *
from random import randint

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self,images,pos,screen):        
        pygame.sprite.Sprite.__init__(self)
        self.sw = screen.get_width()
        self.sh = screen.get_height()
        self.amounts = len(images)        # 造型数量
        self.right_frames = images
        t = pygame.transform.flip
        self.left_frames = [t(im,True,False) for im in images]
        # 向左造型所有的矩形对象
        self.left_rects = [im.get_rect(center=pos) for im in self.left_frames]
        # 向右造型所有的矩形对象
        self.right_rects = [im.get_rect(center=pos) for im in self.right_frames]
        self.heading = 0                   # 朝向,默认为右
        self.index = 0                     # 默认造型编号为0
        self.images = [self.right_frames,self.left_frames]
        self.rects = [self.right_rects,self.left_rects]
        self.set_costume()                 # 设置造型
        self.start_time = time.time()
        self.dx = 10                       # 也可随机选择一个数        
    def set_costume(self):

        self.image = self.images[self.heading][self.index] 
        self.rect = self.rects[self.heading][self.index]
        
    def update(self):
        if time.time() - self.start_time  > 0.1 :  # 超时则前进,换造型

           self.rect.move_ip(self.dx,0)
           old_center = self.rect.center
           self.index = self.index + 1
           self.index = self.index % self.amounts
           self.set_costume()
           self.rect.center = old_center
           if self.rect.right >= self.sw :
               self.heading=1
               self.dx = -10
           if self.rect.left <= 0 :
               self.heading = 0
               self.dx = 10
           self.start_time = time.time()
           
def main():

    background = "blue sky.png"
    width,height = 480,360
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("NPC多造型角色_可爱的Pico的AnimatedSprite类by lixingqiu")
    background = pygame.image.load(background)
    images = [f"pico/right_{i}.png" for i in range(4)]
    images = [pygame.image.load(im) for im in images]

    p = AnimatedSprite(images,(width//2,height-50),screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running=False
        p.update()
        screen.blit(background,(0,0))
        screen.blit(p.image,p.rect)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":

    main()
    
