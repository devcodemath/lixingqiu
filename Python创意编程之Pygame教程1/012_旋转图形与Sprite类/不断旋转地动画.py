"""
   pygame不断旋转地动画练习答案。
   
"""
import pygame
   
image = "girl.png"
width,height = 480,360
中心点 = width//2,height//2
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("pygame不断旋转的动画")

image = pygame.image.load(image).convert_alpha()
image_rect = image.get_rect(center=中心点) # 获取矩形对象
screen.blit(image,image_rect)              # 渲染在screen上
pygame.display.update()                    # 更新显示

angle = 1
while not pygame.event.get(pygame.QUIT):
    
    image2 = pygame.transform.rotate(image,angle) # 逆时针旋转angle度
    image2_rect = image2.get_rect(center=中心点)

    screen.fill((0,0,0))                       # 擦掉原先图像
    screen.blit(image2,image2_rect)            # 渲染在screen上
    pygame.display.update()                    # 更新显示

    angle = angle + 0.05                       # 旋转0.05度

pygame.quit()
