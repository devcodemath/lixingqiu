"""
   while循环与重画矩形.py
"""

import pygame

RED = (255,0,0)
WIDTH,HEIGHT = 480,360

screen = pygame.display.set_mode((WIDTH,HEIGHT))

r1 = pygame.Rect(0,0,20,20)

dx ,dy = 20,0
running = True
while running:
    print(r1)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,RED,r1) # 在screen上画矩形r1
     
    if r1.right < WIDTH:            # 如果r1最右边x小于屏幕宽度
        r1.move_ip(dx,dy)           # 水平位移dx和垂直位移dy
    else:
        running = False
    pygame.display.update()         # 刷新屏幕显示
print(r1)                           # 打印最后r1


