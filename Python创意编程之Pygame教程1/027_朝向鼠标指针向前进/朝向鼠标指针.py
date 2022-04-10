"""
   朝向鼠标指针的Arrow类
"""
import math
import pygame
from pygame.locals import *

class Arrow(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        """
          image:图形,pos:坐标
        """
        pygame.sprite.Sprite.__init__(self)
        self.rotate_center = pos         # 旋转中心
        self.rawimage = image            # 保留原始图形
        self.angle = 0                   # 和x轴的夹角
        self.rotate()                    # 旋转图形  

    def rotate(self):
        """根据和x轴的角度旋转图形"""
        self.image = pygame.transform.rotate(self.rawimage,self.angle)
        self.rect = self.image.get_rect(center=self.rotate_center)

    def update(self):
        """计算和鼠标指针的方向,更新image和rect"""
        p = pygame.mouse.get_pos()        # 获取鼠标指针坐标
        dy = self.rotate_center[1] -p[1]  # 和箭头的垂直距离
        dx = p[0] - self.rotate_center[0] # 和箭头的水平距离 
        degree = math.atan2(dy,dx)        # 计算夹角,代表方向
        self.angle = math.degrees(degree) # 转换为角度
        self.rotate()                     # 生成旋转后的image

    def forward(self,distance):
        """朝着它的方向前进一定的距离"""
        r = math.radians(self.angle)       # 转换成弧度值
        dx = distance * math.cos(r)        # 计算水平位移量
        dy = - distance * math.sin(r)      # 计算垂直位移量
        x = self.rotate_center[0] + dx     # 新的x坐标
        y = self.rotate_center[1] + dy     # 新的y坐标
        self.rotate_center = x,y           # 新的旋转中心
        self.rect.center = self.rotate_center
        
    def backward(self,distance):
        """朝着它的反方向移动一定的距离"""
        self.forward(-distance)
        
    fd = forward                          # 定义别名
    bk = back = backward                  # 定义别名
    
def main():
    """主要函数"""
    size = width,height = 480,360
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("面向鼠标指针旋转的箭头by lixingqiu")
    image = "arrow1-a.png"
    image = pygame.image.load(image).convert_alpha() # 转为每像素模式

    p = Arrow(image,(width//2,height//2))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running=False
            if event.type == KEYDOWN:
                if event.key == K_UP:   p.fd(10)
                if event.key == K_DOWN: p.bk(10)
                    
        screen.fill((255,255,255))
        p.update()
        screen.blit(p.image,p.rect)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":

    main()
