"""
   喊至尊宝后显示字幕.py
   本程序依次显示一些连续图形后显示提示信息
   《大话西游》至尊宝角色，由周星驰饰演。
"""
import pygame
from pygame.locals import *

fd = "喊至尊宝"
images = [pygame.image.load(f"{fd}/{i:04d}.png") for i in range(1,23)]
width,height = images[0].get_size()
print(width,height)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("喊至尊宝后显示字幕")

# 下面轮换显示图片从而播放动画
clock = pygame.time.Clock()
for image in images:
    pygame.event.poll()
    screen.blit(image,(0,0))
    pygame.display.update()
    clock.tick(10)

# 下面开始显示字幕
pygame.font.init()
info = "动画播放完毕, 按任意键关闭窗口..."
font_obj = pygame.font.Font("msyh.ttf",22)
tip = font_obj.render(info,True,(155,0,255,128))
w,h = tip.get_size()
cx = width // 2
cy = height// 2
rect = tip.get_rect(center=(cx,cy))
screen.blit(tip,rect)
pygame.display.update()
while not pygame.event.get(KEYDOWN):clock.tick(30)
pygame.quit()
