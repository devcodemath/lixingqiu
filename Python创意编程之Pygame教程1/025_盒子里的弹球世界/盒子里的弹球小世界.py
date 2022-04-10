"""
   盒子里的弹球小世界。本程序会在屏幕上画两个矩形，然后矩形里有一些弹球。
   这些弹球永远不会弹出矩形的范围之内。
"""
import pygame
from random import randint
from pygame.locals import *

RED = (255,0,0)
BLUE = (0,0,255)

class Ball(pygame.sprite.Sprite):
    """
       球类,继承自角色类,它会在一个矩形范围内受重力移动。
    """
    def __init__(self,radius,box,color):
        """
           radius:半径,box:所在的盒子,color：颜色
        """
        pygame.sprite.Sprite.__init__(self)
        self.radius = radius
        self.image = pygame.Surface((radius*2,radius*2))
        self.image.set_colorkey((0,0,0))   # 设置不渲染颜色
        pygame.draw.circle(self.image,color,(radius,radius),radius)
        pos = box.rect.center
        self.rect = self.image.get_rect(center=pos)
        self.speed = [randint(-5,5),randint(-5,5)]
        self.gravity = 0.5                 # 重力加速度
        self.box = box                     # 保存自己的盒子
        self.set_boundary()                # 设置反弹边界值

    def set_boundary(self):
        """设置反弹的边界"""
        self.left_boundary = self.box.rect.left     # 左边界
        self.right_boundary = self.box.rect.right   # 右边界
        self.top_boundary = self.box.rect.top       # 上边界
        self.bottom_boundary = self.box.rect.bottom # 下边界
        
    def update(self):
        """更新坐标，碰到边缘就反弹。"""        
        self.rect.move_ip(*self.speed)             # 移动矩形对象
        if self.rect.left <= self.left_boundary or \
           self.rect.right >= self.right_boundary:
               self.speed[0] = -self.speed[0]
               
        # 下面通过加上高度，从而对碰到下边缘进行预判
        if self.rect.bottom + self.rect.height >= self.bottom_boundary:
            self.speed[1] = -self.speed[1]
        else:
            self.speed[1] = self.speed[1] + self.gravity 

class Box:
    """
       盒子类，一个盒子就是一张图片，在边缘画了个矩形。
    """
    def __init__(self,width,height,pos):
        """
           width：宽度，height：高度
        """
        self.image = pygame.Surface((width,height))
        self.rect = self.image.get_rect(center=pos)
        pygame.draw.rect(self.image,(255,0,0),(0,0,width,height),1)    


def main():
    """主要函数，新建屏幕，新建对象，进入主循环"""
    
    size = width,height= 640,380
    screen = pygame.display.set_mode(size) 
    pygame.display.set_caption("盒子里的弹珠世界by lixingqiu")

    # 新建第一个盒子，把球加进去
    pos = 150,150
    box1 = Box(200,200,pos)
    balls1 = pygame.sprite.Group()  # 新建组
    [balls1.add(Ball(5,box1,RED)) for x in range(5)]

    # 新建第二个盒子，把球加进去
    pos = 450,150
    box2 = Box(200,200,pos) 
    balls2 = pygame.sprite.Group() # 新建组
    [balls2.add(Ball(5,box2,BLUE)) for x in range(5)]

    clock = pygame.time.Clock()    # 建立时钟对象
    running = True                 # 控制while结束的逻辑变量 
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running=False
            
        balls1.update()
        balls2.update()
        screen.fill((20,30,0))
        screen.blit(box1.image,box1.rect)
        screen.blit(box2.image,box2.rect)
        
        balls1.draw(screen)         # 画小球
        balls2.draw(screen)         # 画小球
        
        pygame.display.update()     # 渲染好了更新显示
        clock.tick(30) 

    pygame.quit()

if __name__ == "__main__":

    main()
