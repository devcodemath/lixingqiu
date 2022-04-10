"""
   闪烁的文字效果,本程序会生成360张文字图片,
   每张的颜色都不一样,让它们轮流显示,从而形
   成闪烁的文字效果动画。
   
"""
import pygame
from pygame import *

def coloradd(color,dh):
    """
       颜色增加函数，本函数把颜色的色相进行增加。其它指标不变。
       color：pygame.Color实例化后的颜色
       dh：一个int,色相增加的值
    """
    h,s,v,a = color.hsva   
    h = h + dh             # 色相增加
    h = h % 360            # 不能超过360
    color.hsva = h,s,v,a   # 设定颜色的hsva值 
    return color

BGCOLOR = (32,76,150)
WIDTH,HEIGHT = 480,360

pygame.init()
# 新建屏幕对象，它是最底层的surface
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BGCOLOR)
pygame.display.set_caption("闪烁的文字效果www.lixingqiu.com")

images = []
color = pygame.Color('red')
myfont = pygame.font.Font("msyh.ttf",88)

# 添加360张图片到images中
for i in range(360):
    flash = myfont.render("风火轮编程",True,color)
    images.append(flash)
    color = coloradd(color,1)

w = images[0].get_width()     # 获取图像的宽度
x = WIDTH//2 - w//2           # 设定渲染的左上角x坐标
y = HEIGHT//2 -100            # 设定渲染的左上角y坐标
index = 0
clock = pygame.time.Clock()   # 时钟对象
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:running = False
    flash = images[index]
    screen.blit(flash,(x,y))  # 把flash渲染到screen上  
    pygame.display.update()   # 刷新屏幕显示
    index += 40
    index = index % 360
    clock.tick(30)            # fps约为60

pygame.quit()


