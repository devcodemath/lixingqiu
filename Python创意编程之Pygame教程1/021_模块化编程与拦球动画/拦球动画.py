"""
   拦球动画,本程序导入Ball类和Board类,让球碰到拦板会反弹。
"""

from ball import *
from board import *

def main():
    """
       主要函数
    """
    size = 480,360
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("拦球动画演示代码")

    # 生成拦板,前面是板子的宽高,后面是坐标
    b = Board((230,10),(200,size[1]-50))      # 生成拦板
    
    balls = [Ball(screen,b) for i in range(3)]# 生成3个球
    group = pygame.sprite.Group()
    [ball.add(group) for ball in balls]
    group.add(b)                             # 把板子加到组中

    clock = pygame.time.Clock()              # 新建时钟对象
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running=False
            
        group.update()             # 调用组中所有对象的update方法
        
        screen.fill((110,10,60))
        group.draw(screen)         # 在screen上渲染组中的每个对象的surface    
        
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    
if __name__ == "__main__":

    main()
           
