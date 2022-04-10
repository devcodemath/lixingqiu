"""
     碰彩球游戏，本程序是主程序，它会导入球类和显示封面函数。
  主要运行流程为，显示封面，进入游戏，根据游戏结果显示相应画面。
"""
from ball import *
from cover import *

def start_game(screen):
    """
       screen是屏幕对象
       本函数生成游戏中的各个对象,进入游戏循环,
       返回游戏成功或失败的逻辑值。
    """
    ball_size = 20,20                 # 球的宽度和高度
    scale = pygame.transform.scale    # 定义别名
    images = [f'images/{i}.png' for i in range(5)]
    images = [pygame.image.load(image) for image in images]
    images = [scale(image,ball_size)   for image in images]
  
    balls = pygame.sprite.Group()     # 新建球组  
    
    clock = pygame.time.Clock()
    running = True
    while running:
        if randint(1,10) ==1 :        # 不定时生成彩球
            Ball(choice(images),balls,screen)
        for event in pygame.event.get():
            if event.type == QUIT:running=False
            
        balls.update()
        if Ball.endflag != -1   :      # 游戏结束            
            running = False
            
        screen.fill((23,234,31))       # 填充背景
        balls.draw(screen)             # 画所有小球
        
        pygame.display.update()        # 显示刷新
        clock.tick(20)                 # 设定fps

    return Ball.endflag

def main():

    cover_image = "images/gingerbread.png"
    screen = display_cover(cover_image)  # 显示封面

    if screen == None: return
    
    success = start_game(screen)        # 进入游戏
    print('success',success)
    
    # 以下根据success的值显示相应的画面
    if success == 1:
        image = "images/success.png"
        display(screen,image)           # 显示成功画面
    elif success == 0:
        image = "images/fail.png"
        display(screen,image)           # 显示失败画面
    elif success == -1 :                
        pygame.quit()                   # 直接退出
        
if __name__ == "__main__":

    main()
        
