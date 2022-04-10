"""
   碰到边缘就反弹.py
"""

import pygame

RED = (255,0,0)
WIDTH,HEIGHT = 480,360

screen = pygame.display.set_mode((WIDTH,HEIGHT))

r1 = pygame.Rect(0,0,20,20)

dx ,dy = 20,0

# 渲染第一帧
pygame.draw.rect(screen,RED,r1) # 在screen上画矩形r1
pygame.display.update()       

running = True
while running:
    print(r1)
    r1.move_ip(dx,dy)
    # 如果r1最右边x坐标大于或等于屏幕宽度 或最左x坐标小于0
    if r1.right >= WIDTH or r1.left <= 0 :  dx = -dx

    screen.fill((0,0,0))
    pygame.draw.rect(screen,RED,r1) # 在screen上画矩形r1
    
    pygame.display.update()         # 刷新屏幕显示
    
print(r1)                           # 打印最后r1


