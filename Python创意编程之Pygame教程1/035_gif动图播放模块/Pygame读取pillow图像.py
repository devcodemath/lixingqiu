"""
   Pygame读取pillow图形文件最简代码。
"""
import pygame
from PIL import Image

cover = "林素婉300.gif"
im = Image.open(cover)
im =  im.convert(mode="RGB")  # 转换成这个模式
mode = im.mode
size = im.size

im_string = im.tobytes()      # 转换成字节型数据
cover = pygame.image.fromstring(im_string,size,mode)

screen = pygame.display.set_mode(size)
screen.blit(cover,(0,0))
pygame.display.update()

# 等待按下窗口关闭按钮
clock = pygame.time.Clock()
while not pygame.event.get(pygame.QUIT):clock.tick(30)
pygame.quit()
