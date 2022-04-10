"""
   碰彩球游戏的显示函数，本模块定义了display_cover函数和display函数。
"""
import pygame
from pygame.locals import *

def display_cover(cover_image):
    """
      显示封面程序,本程序显示一幅像,
      根据玩家是按窗口的退出按钮,
      还是按任意键来决定是否进入游戏。
      由于只是显示静态图形，所以在while
      循环中并没有必要时刻更新画面。
    """
    cover_image = pygame.image.load(cover_image)
    size = cover_image.get_size()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("pygame静态封面显示标准示例模块by lixingqiu")
    clock = pygame.time.Clock()
    screen.blit(cover_image,(0,0)) # 渲染screen上
    pygame.display.update()        # 显示刷新
    enter_game = True              # 进入游戏标志     
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT: # 按关闭按钮将不进入游戏
                running=False
                enter_game = False
            if event.type in (KEYDOWN,MOUSEBUTTONDOWN):
                running=False                
        
        clock.tick(10)           # 设定fps
    if not enter_game:
        pygame.quit()
    else:
        screen.fill((25,123,23))
        pygame.display.update()
        return screen
    
def display(screen,image):
    """
       本函数只是显示一个image,
       直到按窗口关闭按钮才会退出Pygame，
       由于显示静态图形，没必要在循环中不断刷新显示。
    """
    image = pygame.image.load(image)
    screen.blit(image,(0,0))
    pygame.display.update()        # 显示刷新
    clock = pygame.time.Clock()
    # 直到按窗口的关闭按钮，才会退出pygame，否则一直滴答滴答
    while not pygame.event.get(QUIT): clock.tick(10)
    pygame.quit()
    
if __name__ == "__main__":

    screen = display_cover("images/gingerbread.png")
    print(screen)
    # if screen : main()
        
