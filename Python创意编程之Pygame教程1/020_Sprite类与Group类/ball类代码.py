"""
   Ball类示例代码
"""
import pygame
from random import randint
from pygame.locals import *

class Ball:
    def __init__(self,screen):
        """
           screen:所在的屏幕
        """
        r = randint(30,50)
        self.radius = r
        self.sw = screen.get_width()       # 获取屏幕宽度
        self.sh = screen.get_height()      # 获取屏幕高度
        self.image = pygame.Surface((r*2,r*2),SRCALPHA)
        pos = r,r                          # 设定圆心坐标
        color = randint(0,255),randint(0,255),randint(0,255)
        pygame.draw.circle(self.image,color,pos,r)
        self.rect = self.image.get_rect()  # 获取矩形对象
        self.rect.center = self.sh//2,self.sw//2
        self.speed = [randint(-5,5),randint(-5,5)]
        
    def update(self):
        """根据speed更新矩形对象"""
        self.rect.move_ip(self.speed)      # 移动矩形对象
        self.bounce_on_edge()              # 碰到边缘就反弹

    def bounce_on_edge(self):
        """碰到边缘就反弹"""
        # 如果矩形的最右边x坐标大于屏幕宽度或者最左边x坐标小于等于0        
        if self.rect.right>=self.sw or \
           self.rect.left<=0 : self.speed[0] = -self.speed[0]
           
        if self.rect.bottom>=self.sh or \
           self.rect.top<=0 : self.speed[1] = -self.speed[1]
           
def main():
    """
       主要函数
    """
    size = 480,360
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("碰到边缘就反弹的球类演示代码")
    
    balls = [Ball(screen) for i in range(10)] # 生成10个球
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running=False
            
        [ball.update() for ball in balls]
        
        screen.fill((110,10,60))
        [screen.blit(ball.image,ball.rect) for ball in balls]

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    
if __name__ == "__main__":

    main()
           
