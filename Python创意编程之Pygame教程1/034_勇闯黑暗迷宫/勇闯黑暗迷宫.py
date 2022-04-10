"""
   勇闯黑暗迷宫,这是2019/8/11版本的原理程序。
   用鼠标方箭头操作小猫上下左右移动，碰到绿旗就过关了。
   不过每次没有在一定时间内过关的话，会停电，黑乎乎的一片，
   这个时候只能凭记忆过关了。
"""
import time
import pygame
from pygame.locals import *

class Maze(pygame.sprite.Sprite):
    """迷宫类,继承自角色类"""
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self._time = 5               # 黑灯时间
        self.start_time = time.time()# 起始时间
        self.candraw = True          # 是否渲染
        
    def update(self):
        """更新"""
        if not self.candraw:return
        if time.time() - self.start_time > self._time:
            self.candraw = False
            
    def draw(self,screen):
        """如果能画,那么就渲染迷宫图片在screen上"""
        if self.candraw:
           screen.blit(self.image,self.rect)
           
class Sprite(pygame.sprite.Sprite):
    """角色类,继承自pygame的Sprite类"""
    def __init__(self,image,pos):
        """初始化方法,image:图像,pos:坐标"""
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.dead = False
        
    def update(self):
        """更新角色"""
        keys = pygame.key.get_pressed()
        if keys[K_UP] : self.rect.move_ip(0,-2)
        if keys[K_DOWN] : self.rect.move_ip(0,2)
        if keys[K_LEFT] : self.rect.move_ip(-2,0)
        if keys[K_RIGHT] : self.rect.move_ip(2,0)
        
    def draw(self,screen):
        """重画角色"""
        if self.dead == False:       # 没死就重画
           screen.blit(self.image,self.rect)
   
def main():
    """主要调用函数"""
    
    得分 = 0
    icon = "李兴球.ico"
    width,height = size = 480,360
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("勇闯黑暗迷宫原理程序by lixingqiu")
    pygame.display.set_icon(pygame.image.load(icon)) # 窗口图标

    startxy = (50,315)                     # 角色起始坐标
    cat = pygame.image.load("cat.png")
    cat = Sprite(cat,startxy)              # 实例化角色
    images = [f"mazes/迷宫{i}.png" for i in range(6)]
    images = [pygame.image.load(im) for im in images]
    index = 0    
    mazes = [Maze(im) for im in images]    # 所有迷宫
    maze = mazes[0]                        # 第一个迷宫
    amounts = len(mazes)                   # 迷宫数量
    clock = pygame.time.Clock()            # 时钟对象 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:running = False
            
        maze.update()
        cat.update()
        
        # 小猫的坐标更新后,检测它的mask和迷宫的mask是否有重叠
        s = pygame.sprite.collide_mask(maze,cat) # s是碰撞点
        if s :                             # 如果碰到 
            pixel = maze.image.get_at(s)   # 获取像素值S
            if pixel[0] != 255:            # 碰到绿旗,过关          
                 index = index + 1
                 index = index % amounts
                 maze = mazes[index]       # 取下一个迷宫
                 maze.start_time = time.time()
                 cat.rect.center = startxy # 小猫归位
                 得分 = 得分 + 10
            else:
                print("死了!")
                cat.dead = True
        else:
            pixel = None
            
        # 提示信息
        info = "你死了" if cat.dead else "祝你好运"
        info = "得分:" + str(得分) + "," + info
        pygame.display.set_caption(info)

        # 重新渲染画面
        screen.fill((22,20,10))
        maze.draw(screen)
        cat.draw(screen)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":

    main()





    
        
