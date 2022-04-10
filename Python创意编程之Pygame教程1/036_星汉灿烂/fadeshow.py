"""
   淡入淡出显示图形的两个函数,
   注意,在显示的过程中进行了事件检测,
   但是我们并没有去获取它返回的结果,
   这样做的原因是,可以避免窗口出现未响应状态。
"""

import pygame

def fade_in_image(screen,image):
    """淡入显示图像"""
    clock = pygame.time.Clock()
    for a in range(0,256):
        pygame.event.get()
        image.set_alpha(a)
        screen.fill((0,0,0))
        screen.blit(image,(0,0))
        pygame.display.update()
        clock.tick(100)
        
def fade_out_image(screen,image):
    """淡出显示图像"""
    clock = pygame.time.Clock()
    for a in range(255,-1,-1):
        pygame.event.get()
        image.set_alpha(a)
        screen.fill((0,0,0))
        screen.blit(image,(0,0))
        pygame.display.update()
        clock.tick(100)

if __name__ == "__main__":
        
    screen = pygame.display.set_mode((480,360))
    cover = pygame.image.load("封面.png").convert()
    fade_in_image(screen,cover)
    fade_out_image(screen,cover)
