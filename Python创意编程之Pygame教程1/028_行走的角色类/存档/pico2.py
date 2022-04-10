"""
   NPC多造型角色模拟状态机时走时停的增强型AnimatedSprite类。
   本程序模拟了状态机，会演示一个小人物走来走去，它碰到屏幕边缘会反弹。
   并且角色在走的过程中可能停下来。为了增强代码可读性，
   本程序角色所有造型共享一个矩形对象，不再设置矩形对象列表。
   
"""
import time
import pygame
from pygame.locals import *
from random import randint

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self,images,pos,screen):
        """
           images：帧序列，pos：坐标，screen：所在屏幕
        """
        pygame.sprite.Sprite.__init__(self)
        self.sw = screen.get_width()
        self.sh = screen.get_height()
        self.amounts = len(images)        # 造型数量
        self.right_frames = images
        t = pygame.transform.flip
        self.left_frames = [t(im,True,False) for im in images]
              
        self.heading = randint(0,1)        # 随机朝向,0为右，1为左
        self.index = 0                     # 默认造型编号为0
        self.images = [self.right_frames,self.left_frames]
        # 所有造型共享一个矩形对象
        self.rect = self.right_frames[0].get_rect(center=pos)         
        self.start_time = time.time()      # 行走的开始时间
        self.dx = -(self.heading*2 - 1 ) * 10   
        self.image = self.images[self.heading][self.index]
        self.decide()                      # 决定是走还是停
        
    def decide(self):
        """决定是站立还是行走"""
        self.behavior = randint(0,1)       # 0表示站,1表示走
        if self.behavior == 1:
            self.walk_time = randint(100,500)
        else:
            self.stand_time = randint(30,100)
        
    def update(self):
        """根据行为来决定更新方法"""
        if self.behavior == 1 :            
            self.walk()
            self.walk_time -= 1
            if self.walk_time ==0 :self.decide()            
        else:            
            self.stand()
            self.stand_time -= 1
            if self.stand_time == 0 :self.decide()
            
    def stand(self):
        """站立方法，什么也不干。"""
        pass
        
    def walk(self):
        """超时就行走并换造型"""
        if time.time() - self.start_time  > 0.1 :  # 超时则前进,换造型
           self.rect.move_ip(self.dx,0)            # 矩形对象水平位移           
           self.index = self.index + 1
           self.index = self.index % self.amounts
           self.image = self.images[self.heading][self.index]            
           if self.rect.right >= self.sw :         # 到了最右边,转向 
               self.heading=1               
           if self.rect.left <= 0 :                # 到了最左边,转向
               self.heading = 0
           self.dx = -(self.heading*2 - 1 ) * 10
           self.start_time = time.time()
           
def main():

    background = "stripes.png"
    width,height = 480,360
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("NPC多造型角色模拟状态机时走时停的增强型AnimatedSprite类")
    background = pygame.image.load(background)
    images = [f"pico/right_{i}.png" for i in range(4)]
    images = [pygame.image.load(im) for im in images]

    group = pygame.sprite.Group()      # 新建角色组
    for x in range(50,350,50):         # 生成一些角色
       p = AnimatedSprite(images,(x,height-x),screen)
       group.add(p)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running=False
        group.update()
        screen.blit(background,(0,0))
        group.draw(screen)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":

    main()
    
