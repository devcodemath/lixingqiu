"""
   中途岛海战飞行阵列之椭圆，
   本程序新建敌机类,然后让敌机绕着椭圆的轨迹不断地移动。
"""
import math
import pygame
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    """
       绕椭圆飞行的敌机类
    """
    def __init__(self,image,a,b,rotate_center):
        """
           image:图形,a:长半轴,b:短半轴,rotate_center:旋转中心点
        """
        pygame.sprite.Sprite.__init__(self)
        self.rc = rotate_center  # 飞机的旋转中心
        self.rawimage = image    # 记录原始图像
        self.a = a               # 长半轴
        self.b = b               # 短半轴
        self._angle = 0          # 和x轴的夹角
        self.rotate_image()
        
    def setposition(self):
        """设置坐标"""
        r = math.radians(self._angle)   # 把角度值转为弧度值
        x = self.a * math.cos(r)        # 根据椭圆参数方程算x值
        y = -self.b * math.sin(r)
        self.rect.center = self.rc[0] + x , self.rc[1] + y
        
    def rotate_image(self):
        """根据和x轴的角度旋转图形"""
        rotate = pygame.transform.rotate # 定义别名
        self.image = rotate(self.rawimage,self._angle)
        self.rect = self.image.get_rect()

    def update(self):
        """更新"""
        self._angle += 1
        if self._angle >= 360 :
            self.kill()
        else:
            self.rotate_image()
            self.setposition()

def main():
    """主要函数"""
    bg = 'sea.png'
    image = "Raven_128x128_red.png"
    width,height = size = 800,600
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("中途岛海战飞行阵列之椭圆by lixingqiu")
    bg = pygame.image.load(bg)
    
    # 下面准备把图像缩小
    image = pygame.image.load(image)
    w,h = image.get_size()
    image = pygame.transform.scale(image,(w//3,h//3))
    group = pygame.sprite.Group()

    pygame.time.set_timer(USEREVENT,1000) # 设置自定义事件定时器
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running=False
            if event.type == USEREVENT:
                p = Enemy(image,350,200,(width//2,height//2))
                group.add(p)                
        group.update()
        screen.blit(bg,(0,0))       # 渲染背景
        group.draw(screen)          # 画每架飞机
        pygame.display.update()     # 更新显示
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":

    main()



    
    
