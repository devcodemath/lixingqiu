"""
   行走的角色,本程序主要编写了AnimatedSprite类。
   它会让一个多造型的小人走来走去,小人碰到屏幕边缘会反向。
   
"""
import time
import pygame
from pygame.locals import *
from random import randint

class AnimatedSprite(pygame.sprite.Sprite):
    """
       继承自Sprite类的动画角色类
    """
    def __init__(self,right_frames,left_frames,pos,screen):
        """
           right_frames：向右行走造型，left_frames:向左行走造型列表,
           pos：坐标，screen：所在屏幕
        """
        pygame.sprite.Sprite.__init__(self)
        self.sw = screen.get_width()      # 屏幕宽度
        self.sh = screen.get_height()     # 屏幕高度
        self.amounts = len(right_frames)  # 造型数量
        self.right_frames = right_frames  # 向右序列帧
        self.left_frames = left_frames    # 向左序列帧
        self.frames = [self.right_frames,self.left_frames]
        # 下句是定义方向属性      
        self.heading = randint(0,1)       # 随机朝向,0为右，1为左
        self.index = 0                    # 默认造型编号为0
        self.image = self.frames[self.heading][self.index]
        # 所有造型共享一个矩形对象
        self.rect = self.right_frames[0].get_rect(center=pos)         
        self.start_time = time.time()      # 行走的开始时间
        self.dx = (1-self.heading*2) * 10
        
    def next_costume(self):
        """切换到下一个造型"""
        self.index = self.index + 1
        self.index = self.index % self.amounts
        self.image = self.frames[self.heading][self.index]

    def bounce_on_edge(self):
        """碰到边缘就反弹"""
        if self.rect.right >= self.sw :     # 到了最右边,转向 
               self.heading=1               
        if self.rect.left <= 0 :            # 到了最左边,转向
               self.heading = 0
        self.dx = (1-self.heading*2) * 10
           
    def update(self):
        """超时就行走并换造型"""
        if time.time() - self.start_time > 0.1:  # 超时则前进,换造型
           self.rect.move_ip(self.dx,0)          # 矩形对象水平位移           
           self.next_costume()                   # 切换到下一个造型           
           self.bounce_on_edge()                 # 碰到边缘就反弹
           self.start_time = time.time()         # 重设造型切换起始时间 
           
def main():
    """主要函数"""
    
    background = "stripes.png"
    width,height = 480,360
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("AnimatedSprite类")
    background = pygame.image.load(background)
    # 向右行走序列图形
    images = [f"pico/right_{i}.png" for i in range(4)]
    right_frames = [pygame.image.load(im) for im in images]
    t = pygame.transform.flip         # 仅为了缩短下行代码
    # 批量生成向左序列帧
    left_frames = [t(im,True,False) for im in right_frames]
    
    group = pygame.sprite.Group()      # 新建角色组
    for x in range(50,350,50):         # 生成一些角色
       y = height - x
       p = AnimatedSprite(right_frames,left_frames,(x,y),screen)
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
    
