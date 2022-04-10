"""
   说话泡泡.py,这是李白与杜甫斗诗的预备程序.
"""
import pygame
from pygame.locals import *
   
class Pao(pygame.sprite.Sprite):
    """说话泡泡类,继承自角色类"""
    pygame.init()
    fnt = pygame.font.Font("msyh.ttf",18)  # 字体对象
    hmargin = 10     # 垂直间隙
    wmargin = 10     # 水平间隙
    bmargin = 30     # 顶下间隙
    def __init__(self,string,pos):
        """初始化方法,string:要说的话,pos:坐标
           把string转换成surface,贴在泡泡中间
        """
        # 字符串的surface,准备贴在image的(wmargin,hmargin)
        self.string = Pao.fnt.render(string,True,(200,200,200))
        w,h = self.string.get_size()      # 字符串的宽度和高度
        width = 2 * Pao.wmargin + w       # image的宽度
        height = 2 * Pao.hmargin + h + Pao.bmargin
        toph = 2 * Pao.hmargin + h        # 说话泡泡三角上面的高度
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
        pygame.draw.polygon(self.image,(180,180,180),points,3)
        self.image.blit(self.string,(Pao.wmargin,Pao.hmargin))
        self.rect = self.image.get_rect(center=pos)

def main():
    """主要函数"""
    size = 480,360
    center = size[0]//2,size[1]//2
    screen = pygame.display.set_mode(size)
    p = Pao('飞流直下三千尺',center)
    screen.blit(p.image,p.rect)
    pygame.display.update()

if __name__ == "__main__":

    main()


        
