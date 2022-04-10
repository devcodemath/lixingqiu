"""用pygame播放音乐.py ,本程序用pygame的混音器功能播放音乐"""

import pygame                    # 导入pygame模块
import time                      # 导入时间模块

filename = "audio/Tragedy Flame.wav"
pygame.mixer.init()              # 混音器初始化
pygame.mixer.music.load(filename)# 加载音乐文件
pygame.mixer.music.play(-1,0)    # 循环播放音乐
sound = pygame.mixer.Sound("audio/super jump.wav")
time.sleep(5)
sound.play()                     # 播放音效
print("正在播放音乐")
