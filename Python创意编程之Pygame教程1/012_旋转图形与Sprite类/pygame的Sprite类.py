"""
   pygame的Sprite类。
   pygame面向对象编程最简学习示例代码。
   
"""
import pygame

class Sprite:
    def __init__(self,image,pos):
        """
          image：一个surface
          pos：中心点坐标
        """
        self.image = image          # image是一个surface
        self.rect = self.image.get_rect(center=pos)

image = "girl.png"
width,height = 480,360
center = width//2,height//2

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("pygame的Sprite类")
image = pygame.image.load(image).convert_alpha()

girl = Sprite(image,center)        # 实例化女孩
screen.blit(girl.image,girl.rect)  # 画在screen上
pygame.display.update()            # 更新显示 

# 按任意键继续...
while not pygame.event.get(pygame.KEYDOWN):pass

pygame.quit()
