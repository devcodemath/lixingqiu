"""
   时钟对象演示程序_获取fps。
   本程序会新建时钟对象,它会固定画面显示的fps,
   并且在标题栏上显示出来。
"""
import pygame

width,height = 480,360
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("时钟对象演示程序")
sur = pygame.Surface((480,360))

running = True
clock = pygame.time.Clock()
while running:
    
    for event in pygame.event.get():  # 遍历每个事件 
        if event.type == pygame.QUIT:running = False
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.circle(sur,(255,0,0),event.pos,5)
        if event.type == pygame.MOUSEBUTTONDOWN:
            sur.fill((0,0,0))
        if event.type == pygame.KEYDOWN:print(event.unicode)
    
    screen.fill((0,0,0))            # 填充背景颜色
    screen.blit(sur,(0,0))
    pygame.display.update()
    fps = clock.get_fps()           # 得到fps
    pygame.display.set_caption(str(fps))
    clock.tick(60)                  # 设定fps
    
pygame.quit()
