"""
   winsound循环播放背景音乐
"""

from winsound import *

music = '凤飞飞 - 玫瑰玫瑰我爱你.wav'

PlaySound(music,SND_ASYNC|SND_LOOP)

print("音乐还在循环播放")
