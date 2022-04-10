"""
   李白与杜甫斗诗的一个有趣的pygame小程序。
   本程序会显示李白和杜甫的图像，他们你一言我一语的说起“诗”来。
"""
import time
import pygame
from pygame.locals import *
        
class Pao(pygame.sprite.Sprite):
    """说话泡泡类,继承自角色类"""
    pygame.init()
    fnt = pygame.font.Font("msyh.ttf",22)  # 字体对象
    hmargin = 10     # 垂直间隙
    wmargin = 10     # 水平间隙
    bmargin = 30     # 顶下间隙
    def __init__(self,string,pos):
        """初始化方法,产生包含字符的说话泡泡image
        """
        pygame.sprite.Sprite.__init__(self)       
        # 字符串的surface,准备贴在image的(wmargin,hmargin)
        self.string = Pao.fnt.render(string,True,(200,20,200))
        w,h = self.string.get_size()      # 字符串的宽度和高度
        width = 2 * Pao.wmargin + w       # image的宽度
        height = 2 * Pao.hmargin + h + Pao.bmargin
        toph = 2 * Pao.hmargin + h        # 说话泡泡三角上面的高度
        # 以下是确定泡泡每个顶点相对于image的坐标
        p1 = (0,0)
        p2 = (width,0)
        p3 = (width,toph)
        p4 = (width * 0.667,toph)
        p5 = (width * 0.5,height)
        p6 = (width * 0.333,toph)
        p7 = (0,toph)
        points = (p1,p2,p3,p4,p5,p6,p7)        
        # 下面新建的是说话泡泡的image
        self.image = pygame.Surface((width,height))
        self.image.set_colorkey((0,0,0))
        # 在image上画由points列表中的点组成的多边形
        pygame.draw.polygon(self.image,(180,180,180),points,3)
        self.image.blit(self.string,(Pao.wmargin,Pao.hmargin))
        self.rect = self.image.get_rect(center=pos)        
        
class Sprite(pygame.sprite.Sprite):
    """定义角色类,继承自pgyame.sprite.Sprite类"""
    def __init__(self,image,pos,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect(center=pos)
        self.group = group
        self.group.add(self)
        # 每个角色都有自己的说话泡泡组
        self.pao_group = pygame.sprite.Group()
        
    def render(self):
        """填充背景为白色,显示诗人和说话泡泡"""
        screen.fill((255,255,255))     # 填充白色背景
        self.group.draw(screen)        # 诗人组重画
        self.pao_group.draw(screen)    # 泡泡组重画
        pygame.display.update()        # 更新屏幕显示
        
    def speak(self,string,_time):
        """角色的说话功能,在头顶上显示一个说话泡泡"""
        x = self.rect.centerx
        y = self.rect.top - 50         # 在角色顶上50像素处
        pos = (x,y)
        self.pao = Pao(string,pos)     # 实例化一个泡泡
        self.pao_group.add(self.pao)   # 加入组中

        self.render()                  # 填充背景,显示图像
        # 下面仅仅是等待一定的时间
        running = True
        self.start_time = time.time()
        while time.time() - self.start_time <= _time and running:
            if pygame.event.get(QUIT) :running = False           
            
        self.pao.kill()               # 说话泡泡删除后(再渲染)
        self.render()                 # 重新填充背景,显示图像  
        if running == False:
            return False
        return True
        
def display_诗人(_time,sp_group):
    """短时间内显示两位诗人"""
    screen.fill((255,255,255))       # 填充白色背景 
    sp_group.draw(screen)            # 画两位诗人
    pygame.display.update()          # 更新屏幕显示
        
    running = True
    start_time = time.time()
    while time.time() - start_time <= _time and running:
        if pygame.event.get(QUIT) :running = False
        
    if running == False :
        pygame.quit()
        return False
    return True
    
def main():
    """主要函数"""
    import os
    global screen
    size = 660,520
    center = size[0]//2,size[1]//2
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("李白与杜甫斗诗by www.lixingqiu.com")
    诗 = [ '杜先生,敢与我斗诗否?','no problem',
           '飞流直下三千尺','我有三千黄花菜',
          '明月何时待我还','借你Q币忘了还',
          '我欲因之梦吴越','一夜回到解放前',
          '床前明月光','杜甫睡得香']

    index = 0
    amounts = len(诗)
    image1 = pygame.image.load("李白.png")
    image2 = pygame.image.load("杜甫.png")
    left = size[0]//2 - 150,size[1]//2+50  # 李白在左边
    right = size[0]//2 + 150,size[1]//2+90 # 杜甫在右边
    sp_group = pygame.sprite.Group()       # 两位诗人的组
    sprite1 = Sprite(image1,left,sp_group) # 角色1,李白
    sprite2 = Sprite(image2,right,sp_group)# 角色2,杜甫

    # 显示诗人后,短暂停留几秒钟,要不然说话太快
    go_on = display_诗人(2,sp_group)
    
    if go_on:
        while index < amounts-1:
            继续 = sprite1.speak(诗[index],3) # 李白说一句
            if not 继续:break
            index = index + 1
            继续 = sprite2.speak(诗[index],3) # 杜甫说一句
            if not 继续:break
            index = index + 1

        if not 继续:
            pygame.quit()
            return
        
        clock = pygame.time.Clock()
        # 直到按窗口关闭按钮才退出Pygame
        while not pygame.event.get(QUIT):clock.tick(30)
        pygame.quit()

if __name__ == "__main__":

    main()


        
