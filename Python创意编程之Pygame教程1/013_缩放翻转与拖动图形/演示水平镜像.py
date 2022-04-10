"""
   演示水平镜像。
   
"""
import pygame

def press_any_key_to_continue():
    """
       不断检测有没有单击鼠标键，如果按了则退出while循环
    """
    while not pygame.event.get(pygame.MOUSEBUTTONDOWN):
        pass
    
image = "girl.png"
width,height = 480,360
中心点 = width//2,height//2
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("pygame演示水平镜像")

# 原始图像
image = pygame.image.load(image).convert_alpha()
image_rect = image.get_rect(center=中心点) # 获取矩形对象
screen.blit(image,image_rect)              # 渲染在screen上
pygame.display.update()                    # 更新显示

press_any_key_to_continue()                # 按任意键继续

# 水平镜像
image2 = pygame.transform.flip(image,True,False) # 水平镜像
image2_rect = image2.get_rect(center=中心点)
image2_rect.right = image_rect.right + image_rect.width 

screen.blit(image2,image2_rect)            # 渲染在screen上
pygame.display.update()                    # 更新显示

press_any_key_to_continue() 

pygame.quit()
