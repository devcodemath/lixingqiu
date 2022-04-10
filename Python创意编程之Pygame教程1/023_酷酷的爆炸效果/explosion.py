"""
   酷酷的爆炸效果类_Pygame版
"""
import time
import pygame
from random import randint
from pygame.locals import *

class Explosion(pygame.sprite.Sprite):
    """
       爆炸效果类,继承自Sprite
    """
    def __init__(self,pos,frames,interval,group):
        """
           frames：帧图，interval：帧播放间隔时间
        """
        pygame.sprite.Sprite.__init__(self)
        self.frames = frames
        # 下面的列表保存了每个帧图的矩形对象,同时设置了中心位置
        self.rects = [f.get_rect(center=pos) for f in frames]        
        self._index = 0               # 帧起始索引
        self._amounts = len(frames)   # 帧数
        self._interval = interval     # 每帧播放的时间
        self.start_time = time.time() # 起始时间
        self.set_costume()        
        self.add(group)               # 增加自己到组中

    def set_costume(self):
        """设置造型"""
        self.image = self.frames[self._index]
        self.rect = self.rects[self._index]

    def update(self):
        """
           如果超时了,就切换到下一个造型
        """
        if time.time() - self.start_time >= self._interval:
            if self._index < self._amounts-1:
                self._index += 1
                self.set_costume()
                self.start_time = time.time()
            else:
                self.kill()          # 造型切换完毕自杀

def main():
    """
       主调用函数,本函数新建screen,
       每隔一定时间产生一个爆炸效果
    """
    
    width,height = size = 960,720
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("酷酷的爆炸效果类Pygame版 by lixingqiu")

    images = [f"frames/{i}.gif" for i in range(6)]
    images = [pygame.image.load(im) for im in images]

    pygame.time.set_timer(USEREVENT,randint(10,100)) 
    clock = pygame.time.Clock()

    group = pygame.sprite.Group()    # 爆炸组
    running = True
    while running:
        e = pygame.event.poll()      # 从事件列表中取个事件
        if e.type == QUIT:running = False
        if e.type == USEREVENT:
            x = randint(0,width)
            y = randint(0,height)
            # 新建一个爆炸效果,坐标,帧图,间隔,组            
            Explosion((x,y),images,0.1,group)
            pygame.time.set_timer(USEREVENT,randint(10,100))
        group.update()
        screen.fill((60,0,160))
        group.draw(screen)
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    
if __name__ == "__main__":

    main()

    
            
        
            
    
        
                
            
            
        
