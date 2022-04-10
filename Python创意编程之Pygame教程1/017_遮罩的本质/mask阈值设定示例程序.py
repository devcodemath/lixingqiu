"""
   mask阈值设定示例程序
   从surface创建mask的时候能设置阈值,小于等于阈值的像素的mask位将被设定为0。
   表示不接受碰撞检测。
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((480,360))

width,height = 50,50
x1,y1 = 100,100
sur1 = pygame.Surface((width,height)).convert_alpha()
sur1.fill((255,100,100,60))                 # 60是透明度
sur1_rect = sur1.get_rect(topleft=(x1,y1))  # 获取矩形并定位

# 以下创建mask,设定阈值为50,即小于等于50的都会被设置为0
sur1_mask = pygame.mask.from_surface(sur1,50)  # 取掩膜
print(sur1_mask.get_at((1,1)))              # 取(1,1)掩膜值
screen.blit(sur1,sur1_rect)                 # 贴到屏幕
pygame.display.update()                     # 刷新屏幕显示
