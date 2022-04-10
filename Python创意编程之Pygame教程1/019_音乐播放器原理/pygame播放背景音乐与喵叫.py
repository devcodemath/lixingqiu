"""
   Pygame播放背景音乐与喵叫示例程序_mixer
"""
import pygame
from pygame.locals import *

rosemusic = "凤飞飞 - 玫瑰玫瑰我爱你.mp3"
screen = pygame.display.set_mode((480,360)) 
pygame.mixer.init() 
pygame.mixer.music.load(rosemusic)
pygame.mixer.music.play(-1,0)     # -1代表循环播放,0代表从头开始

catsound = pygame.mixer.Sound('喵.wav') # 实例化声音对象
clock = pygame.time.Clock()             # 建立时钟对象
pygame.time.set_timer(USEREVENT,3000)   # 每3秒发生USEREVENT事件
pygame.event.set_allowed((USEREVENT,QUIT))  # 设置充许的事件

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:running = False
        if event.type == USEREVENT:
            catsound.play()
            print('播放喵叫了')
    clock.tick(10)

pygame.quit()

    
