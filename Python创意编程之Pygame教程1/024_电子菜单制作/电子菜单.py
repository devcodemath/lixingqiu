"""
   电子菜单制作，本程序设计了Button类，菜单则由一个组完成。
   每个实例化的按钮有两个造型，以便当碰到鼠标指针时会切换造型。
   
"""
import pygame
from pygame.locals import *

class Button(pygame.sprite.Sprite):
    """
       按钮类型，它有两个造型，当碰与未碰到鼠标指针时会切换到不同造型
    """
    def __init__(self,size,pos,title,bgcolors):
        """
           size：宽高二元组,pos：渲染坐标
           title：标题，bgcolor：背景颜色
           本函数新建两个image，把title贴到这两个image的中心位置。
           
        """
        pygame.sprite.Sprite.__init__(self)
        self.bgcolors= bgcolors           # 两种颜色轮换
        self.index = 0                    # 相当于造型索引
        self.image0 = pygame.Surface(size)# 新建第一个造型
        self.image0.fill(bgcolors[0])
        self.image1 = pygame.Surface(size)# 新建第二个造型
        self.image1.fill(bgcolors[1])
        # 由于两个造型大小相同，这里让它们共用一个中心点
        self.rect = self.image0.get_rect(center=pos)
        x = self.rect.width//2           # 矩形对象中心点x坐标
        y = self.rect.height//2          # 矩形对象中心点y坐标
        
        r = title.get_rect()             # 标题的矩形对象
        r.center = (x,y)                 # 把标题的中心点设为(x,y)
        
        self.image0.blit(title,r)        # 把标题渲染到image0中心
        self.image1.blit(title,r)        # 把标题渲染到image1中心
        self.images = self.image0,self.image1
        self.image = self.images[self.index]         
        self.clicked = False
        
    def update(self):
        """
           更新造型
        """        
        mpos = pygame.mouse.get_pos()      # 获取指针坐标
        if self.rect.collidepoint(mpos):   # 碰到鼠标指针
            ms = pygame.mouse.get_pressed()
            self.index = 1
            self.image = self.images[self.index]          
            if ms[0] and not self.clicked:
                self.clicked = True
        else:
            self.index = 0
            self.image = self.images[self.index]            
            self.clicked = False
            
def enter_game():
    '''
       进入游戏循环中，这里只是显示几个字来进行示意。
       本函数引用了全局变量myfont、width、height。
    '''
    ingame = myfont.render('游戏中...',True,(128,250,250))
    rect = ingame.get_rect(center=(width//2,height//2))
    running = True      
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running = False      
        screen.fill((101,120,20))
        screen.blit(ingame,rect)
        pygame.display.update()
    pygame.quit()
    
size = width,height = 480,360
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame电子菜单制作by lixingqiu")

start_name = '开始游戏'
help_name = '帮助help'
exit_name = '关闭窗口'

myfont = pygame.font.Font("msyh.ttf",16)
help_info = myfont.render('按方向箭头操作方块移动',True,(200,200,200))
start_title = myfont.render(start_name,True,(255,0,0))
help_title  = myfont.render(help_name,True,(25,0,255))
exit_title = myfont.render(exit_name,True,(0,0,255))

# 实例化开始按钮
pos = width//2,100
bgcolors = [(128,132,251),(80,232,51)]
start_button = Button((120,40),pos,start_title,bgcolors)

# 实例化帮助按钮
pos = width//2,150
help_button = Button((120,40),pos,help_title,bgcolors)

# 实例化结束按钮
pos = width//2,200
exit_button = Button((120,40),pos,exit_title,bgcolors)

menu = pygame.sprite.Group()    # 新建菜单组
menu.add(start_button)
menu.add(help_button)
menu.add(exit_button)

start_game = False              # 标志游戏开始的逻辑变量
running = True                  # 标志while循环开始的逻辑变量
while running:
    for event in pygame.event.get():
        if event.type == QUIT:running = False

    menu.update()               # 菜单组更新
    screen.fill((0,0,0))
    menu.draw(screen)
    if help_button.clicked :    # 如果单击了帮助按钮
        screen.blit(help_info,(160,300))
    if exit_button.clicked :    # 如果单击了结束按钮
        running = False
    if start_button.clicked:    # 如果单击了启动按钮
        start_game = True
        running = False
    pygame.display.update()
    
if start_game == False:
    pygame.quit()
else:
    enter_game()






