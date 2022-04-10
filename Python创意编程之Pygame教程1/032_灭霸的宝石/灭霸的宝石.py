"""
   灭霸的宝石,这是一个简单的接物小游戏。
   在这个游戏中，宝石用彩色的圆圈表示，它们会不断地落下来。
   用鼠标指针左右操作灭霸去接这些宝石，当接到一定数量的宝石后，
   游戏就应该结束，请自行设计结束游戏代码。
"""

import pygame
from pygame.locals import *
from random import randint

def random_color():
    """产生随机RGB颜色"""
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)    
    return r,g,b

def random_circle():
    """产生一个圆形图"""
    radius = randint(10,20)                # 随机半径
    image = pygame.Surface((radius*2,radius*2))
    image.set_colorkey((0,0,0))
    # 随机RGB颜色 
    color = random_color()
    pygame.draw.circle(image,color,(radius,radius),radius)
    return image
    
class Gemstone(pygame.sprite.Sprite):
    """宝石类，继承自角色类"""
    def __init__(self,screen,group):
        """
           screen：所在屏幕,group：所在组
        """        
        pygame.sprite.Sprite.__init__(self)    # 初始化父类
        self.sw = screen.get_width()           # 屏幕宽席
        self.sh = screen.get_height()          # 屏幕高度        
        self.image = random_circle()           # 宝石的图像      
        self.rect = self.image.get_rect()      # 获取矩形对象
        position = randint(0,self.sw),randint(-200,-50)
        self.rect.center = position            # 定矩形的位置
        self.dx = 0                            # 水平方向单位位移
        self.dy = randint(9,15)                # 垂直方向单位位移 
        self.add(group)                        # 加入到组中 

    def update(self):
        """更新坐标"""
        self.rect.move_ip(self.dx,self.dy)     # 移动矩形
        self.bottom_detect()                   # 碰到底检测
        
    def bottom_detect(self):
        """碰到边缘就从组中移除自己"""
        if self.rect.top>self.sh : self.kill()


class Player(pygame.sprite.Sprite):
    """
       玩家类，继承自角色类
    """
    
    def __init__(self,image,screen):
        """
           image：图像，screen：所在屏幕
        """        
        pygame.sprite.Sprite.__init__(self)    # 初始化父类
        self.sw = screen.get_width()           # 屏幕宽席
        self.sh = screen.get_height()          # 屏幕高度        
        self.image = image                     # 代表它的图形        
        self.rect = self.image.get_rect()      # 获取矩形对象
        position = 0,self.sh - 40              # 初始坐标
        self.rect.center = position            # 定矩形的位置      

    def update(self):
        """更新坐标，用鼠标操作玩家"""
        pos = pygame.mouse.get_pos()          # 获取鼠标指针坐标  
        self.rect.centerx = pos[0]            # 设定矩形中央x坐标 
 
         
def main():
    """主要函数"""
    score = 0                                # 得分
    frame_counter = 0                        # 帧计数器
    width,height = 843,463                   # 定义宽高
    white = (250,250,250)                    # 定义白色 
    background = "星空背景.png"              # 背景图片
    player_image = "灭霸x.png"               # 玩家图片 

    pygame.init() 
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("灭霸的宝石")
    background = pygame.image.load(background)    
    player_image = pygame.image.load(player_image)    
    
    stone_group = pygame.sprite.Group()     # 创建宝石组
    player = Player(player_image,screen)    # 创建玩家

    fnt = pygame.font.Font("msyh.ttf",28)   # 创建字体对象
    score_image = fnt.render("得分：" + str(score),True,white )
    
    clock = pygame.time.Clock()            # 时钟对象
    running = True                         # 控制循环的逻辑变量    
    while running :
        # 以下是不定时产生宝石
        frame_counter += 1
        if frame_counter % randint(20,40) == 0 :
            Gemstone(screen,stone_group)
        
        event = pygame.event.poll()       # 从事件队列中取一个事件
        if event.type == QUIT:running = False 
 
        stone_group.update()                     # 更新宝石       
        player.update()                          # 更新player
        
        # 和每个宝石的碰撞检测
        stone = pygame.sprite.spritecollideany(player,stone_group) 
        if stone:
            stone.kill()
            score += 10
            score_image = fnt.render("得分：" + str(score),True,white)            
                                           
        screen.blit(background,(0,0))            # 画背景图   
        stone_group.draw(screen)                 # 重画所有宝石           
        screen.blit(player.image,player.rect)    # 重画玩家图片
        screen.blit(score_image,(width//2-50,40))# 重画得分

        pygame.display.update()                  # 更新屏幕显示
        clock.tick(30)   
    
    pygame.quit()    
    
if __name__ == "__main__":

    main()

        

    
        
        
