"""
   滚动的背景类，本程序会新建一个不断向后滚动背景。
   
"""
import pygame
from pygame.locals import * 

class ScrolledBackground:
    def __init__(self,image,dx,screen):
        """
           image:图像,dx:水平速度,screen:所在屏幕
        """
        self.dx = dx                  # 水平速度
        self.screen = screen          # 所在的屏幕
        self.sw = screen.get_width()  # 屏幕宽度 
        self.sh = screen.get_height() # 屏幕高度
        self.image0 = image           # 图像0
        self.image1 = image           # 图像1
        # 注意下面两个矩形相差了一个屏幕宽高的距离
        self.rect0 = image.get_rect(topleft=(0,0))
        self.rect1 = image.get_rect(topleft=(self.sw,0))

    def update(self):
        """更新两个矩形"""
        self.rect0.move_ip(self.dx,0)
        self.rect1.move_ip(self.dx,0)
        # 如果矩形最右边x坐标小于或等于0,则移到屏幕最右边。
        if self.rect0.right <= 0:self.rect0.left=self.sw
        if self.rect1.right <= 0:self.rect1.left=self.sw        
        
    def draw(self):
        """重画两个图像"""
        self.screen.blit(self.image0,self.rect0)
        self.screen.blit(self.image1,self.rect1)
        
def main():
    """滚动的背景测试函数"""
    bg = 'tunnel_.png'
    size = width,height = 480,360
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("滚动的背景类by lixingqiu")
    bg = pygame.image.load(bg)
    bg = ScrolledBackground(bg,-5,screen)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running=False
        bg.update()              # 更新坐标
        bg.draw()                # 重画图形
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':

    main()
