"""
   pygame旋转图像最简示例_按任意键继续执行.py
   本程序会显示一个女孩的图像,按任意键会旋转她。
   再按任意键会关闭Pygame窗口。
   
"""
import pygame

def press_any_key_to_continue():
    """
       不断检测有没有按任意键，如果按了则退出while循环
    """
    while not pygame.event.get(pygame.KEYDOWN):
        pass
    
image = "girl.png"
width,height = 480,360
中心点 = width//2,height//2
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("pygame旋转图像最简示例")

image = pygame.image.load(image).convert_alpha()
image_rect = image.get_rect(center=中心点) # 获取矩形对象
screen.blit(image,image_rect)              # 渲染在screen上
pygame.display.update()                    # 更新显示

press_any_key_to_continue()                # 按任意键继续
    
image2 = pygame.transform.rotate(image,90) # 逆时针旋转90度
image2_rect = image2.get_rect(center=中心点)

screen.fill((0,0,0))                       # 擦掉原先图像
screen.blit(image2,image2_rect)            # 渲染在screen上
pygame.display.update()                    # 更新显示

press_any_key_to_continue() 

pygame.quit()
