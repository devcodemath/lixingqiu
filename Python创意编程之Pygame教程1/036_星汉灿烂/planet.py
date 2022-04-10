"""
   宇宙类作品_星汉灿烂的核心程序，
   playnet.py模块。
   ,本程序会显示太阳星空背景,八大行星会出现,等待单击.
   单击后,它们的介绍图片会从右侧出现,再次单击,
   则图片又会从左到右慢慢消失。如果某天本模块由于Python
   或操作系统升级原因导致挂了，请自行修改源码，这里提供
   的是基础思想。
"""

import pygame
from pygame.locals import *

class Intro(pygame.sprite.Sprite):
    """介绍页类，它是行星描述信息的包装,继承自pygame的角色类"""
    def __init__(self,image,screen,group,行星类):
        """image：图像，screen：所在屏幕，
           group：组，行星类：本模块的行星类"""
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.sw = screen.get_width()
        self.rect = image.get_rect(topleft=(self.sw,0))
        self.visible = False
        self.dx = -1
        self.group = group
        self.group.add(self)
        self.Planet = 行星类         # 注意这里传递了类
        
    def update(self):
        """实时更新，如果visible为真，并且dx是-1，则往左移"""
        if self.visible and self.dx == -1:
            if self.rect.x > 0 :     # 没到最左边,一直往左移
               self.rect.move_ip(self.dx,0)
            else:                    # 否则就移动完毕,等待鼠标左键按下
               clicked = pygame.mouse.get_pressed()
               if clicked[0] : self.dx = 1                  
        else:
            if self.rect.x < self.sw:# 单击后x坐标小于屏幕宽度往右移
                self.rect.move_ip(self.dx,0)
            else:                    # 移完了,复原各个变量
                if self.visible:
                   print("显示完毕")
                   self.visible = False
                   self.dx = -1
                   self.Planet.show = False
        
class Planet(pygame.sprite.Sprite):
    """行星类,继承自pygame的角色类"""
    show = False                 # 类变量,控制只能同时显示一个介绍
    def __init__(self,image,pos,intro,group):
        """image:图形,pos:坐标,intro:介绍对象,group：组"""
        pygame.sprite.Sprite.__init__(self)
        self.intro = intro
        self.image = image
        w,h = image.get_size()    # 得到宽度和高度
        self.image_big = pygame.transform.scale(image,(w+5,h+5))
        self.rect = image.get_rect(center=pos)
        self.rect_big = self.image_big.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_big = pygame.mask.from_surface(self.image_big)
        self.images = [self.image,self.image_big]
        self.masks = [self.mask,self.mask_big]
        self.rects = [self.rect,self.rect_big]        
        self.group = group
        self.group.add(self)
        
    def update(self):
        """更新，行星碰到鼠标指针并且按下了鼠标左键时，
           就把它的介绍页的可见性设为True。然后把类变量show
           的值也设为True，这样就阻止了再次单击其它行星时把
           其它介绍页也显示出来。
           
        """
        mp = pygame.mouse.get_pos()        
        dx = mp[0] - self.rect.x
        dy = mp[1] - self.rect.y
        # 如果鼠标指针在行星的矩形范围内
        if dx >= 0 and dx < self.rect.width and \
           dy >=0 and dy < self.rect.height:
               flag = self.mask.get_at((dx,dy))
               clicked = pygame.mouse.get_pressed()
               # 如果单击左键,并且当前没有任何一个行星介绍
               # 那么才把自己的介绍显示出来
               if clicked[0] and Planet.show==False :
                   self.intro.visible = True
                   Planet.show = True   # 这样再单击其它行星就失效了
                                        # 直到介绍页显示完毕后,它的值
                                        # 才会变成False。
        else:
            flag = 0
        self.image = self.images[flag]
        self.rect = self.rects[flag]
        self.mask = self.masks[flag]
        
def make_planet(intro_group,planet_group,screen):
    """
       加载资源,形成行星介绍页与行星角色，把它们加入到相应的组中去。
       intro_group：介绍组，planet_group：行星组，screen：屏幕

    """
    mercury_intro = pygame.image.load("images/水星介绍.png")
    mercury = pygame.image.load("images/水星.png")

    venus_intro = pygame.image.load("images/金星介绍.png")
    venus = pygame.image.load("images/金星.png")
    
    earth_intro = pygame.image.load("images/地球介绍.png")
    earth = pygame.image.load("images/地球.png")

    mars_intro = pygame.image.load("images/火星介绍.png")
    mars = pygame.image.load("images/火星.png")

    mars_intro = pygame.image.load("images/火星介绍.png")
    mars = pygame.image.load("images/火星.png")

    jupiter_intro = pygame.image.load("images/木星介绍.png")
    jupiter = pygame.image.load("images/木星.png")

    saturn_intro = pygame.image.load("images/土星介绍.png")
    saturn = pygame.image.load("images/土星.png")

    uranus_intro = pygame.image.load("images/天王星介绍.png")
    uranus = pygame.image.load("images/天王星.png")

    neptune_intro = pygame.image.load("images/海王星介绍.png")
    neptune = pygame.image.load("images/海王星.png")

    gch_intro = pygame.image.load("images/观沧海.png")
    gch = pygame.image.load("images/观沧海标题.png")

    # 水星介绍实例化和水星角色实例化
    mercury_intro = Intro(mercury_intro,screen,intro_group,Planet)
    mercury = Planet(mercury,(70,180),mercury_intro,planet_group)

    # 金星介绍实例化和金星角色实例化
    venus_intro = Intro(venus_intro,screen,intro_group,Planet)
    venus = Planet(venus,(100,180),venus_intro,planet_group) 

    # 地球介绍实例化和地球角色实例化
    earth_intro = Intro(earth_intro,screen,intro_group,Planet)
    earth = Planet(earth,(140,180),earth_intro,planet_group)

    # 火星介绍实例化和火星角色实例化
    mars_intro = Intro(mars_intro,screen,intro_group,Planet)
    mars = Planet(mars,(190,180),mars_intro,planet_group)

    # 木星介绍实例化和木星角色实例化
    jupiter_intro = Intro(jupiter_intro,screen,intro_group,Planet)
    jupiter = Planet(jupiter,(245,180),jupiter_intro,planet_group)

    # 土星介绍实例化和土星角色实例化
    saturn_intro = Intro(saturn_intro,screen,intro_group,Planet)
    saturn = Planet(saturn,(335,180),saturn_intro,planet_group)

    # 天王星介绍实例化和天王星角色实例化
    uranus_intro = Intro(uranus_intro,screen,intro_group,Planet)
    uranus = Planet(uranus,(415,180),uranus_intro,planet_group)

    # 海王星介绍实例化和海王星角色实例化
    neptune_intro = Intro(neptune_intro,screen,intro_group,Planet)
    neptune = Planet(neptune,(475,180),neptune_intro,planet_group)
    
    # 观沧海介绍实例化观沧海实例化
    gch_intro = Intro(gch_intro,screen,intro_group,Planet) 
    gch = Planet(gch,(445,345),gch_intro,planet_group)
    

def show_planet(screen,background):
    """
       显示行星,等待单击各行星，
       screen：屏幕对象,background：背景图
    """

    intro_group = pygame.sprite.Group()          # 介绍组
    planet_group = pygame.sprite.Group()         # 行星组

    make_planet(intro_group,planet_group,screen) # 生成若干行星
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running=False
            
        planet_group.update()                    # 更新每个行星
        intro_group.update()                     # 更新每张介绍页
        
        screen.blit(background,(0,0))
        planet_group.draw(screen)
        # 如果介绍页是可见的才把它渲染出来
        [screen.blit(p.image,p.rect) for p in intro_group if p.visible]
        pygame.display.update()

    pygame.quit()
    
def main():
    """主调用函数"""
    size = width,height = 480,360    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("星汉灿烂的核心程序by lixingqiu")

    background = pygame.image.load("images/太阳.png")
    show_planet(screen,background)
    
if __name__ == "__main__":

    main()
    
        
        
