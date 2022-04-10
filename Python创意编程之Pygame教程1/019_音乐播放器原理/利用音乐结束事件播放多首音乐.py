"""
   利用音乐结束事件循环播放多首音乐.py ,
   本程序在播放完一首音乐后,会自动触发音乐结束事件。
   在下面的代码中会不断地判断是否这一事件发生。
   如果发生了，那么就让列表索引增加1，播放下一首音乐。
   
"""

import pygame
from pygame.locals import *

pygame.init()
 
screen = pygame.display.set_mode((100,100))
pygame.display.set_caption("利用音乐结束事件循环播放多首音乐")
 
music_list = ['纯音乐.mp3','凤飞飞 - 玫瑰玫瑰我爱你.mp3','喵.wav']
music_amounts = len(music_list)
music_index = 0
# 播放音乐，设置音乐结束事件
pygame.mixer.music.load(music_list[music_index])
pygame.mixer.music.set_endevent(USEREVENT) # 音乐结束事件
pygame.mixer.music.play()

clock = pygame.time.Clock()

running = True
while running:
     
    for event in pygame.event.get():   # 迭代每个事件
        if event.type == pygame.QUIT:  # 如果单击了关闭按钮
            running = False 
        elif event.type == USEREVENT: 
            # 当音乐播放完毕后会触发此事件，播放下一首音乐
            music_index +=1
            music_index = music_index % music_amounts
            pygame.mixer.music.load(music_list[music_index])
            pygame.mixer.music.play()      
 
    # 由于不需要显示什么,所以显示代码略  
    clock.tick(10)                    # 设置fps为10
 
pygame.quit()
