"""最简音乐播放器.py"""
import pygame
from turtle import *

def playmusic(x,y):
    """播放音乐"""
    pygame.mixer.music.stop()         # 停止播放音乐
    if bluebutton.index == 0 :        # 如果没有播放则播放 
       pygame.mixer.music.play(-1,0)
    bluebutton.index = 1 - bluebutton.index # 切换造型索引
    bluebutton.shape(blue_images[bluebutton.index])#换造型
    
def playsound(x,y):
    """播放声音效果,造型会自动切换回去"""
    sound.play()                           # 播放音效
    redbutton.index = 1 - redbutton.index  # 切换造型索引
    redbutton.shape(red_images[redbutton.index])  #换造型
    def delay_alt():
        """延时把造型切换回去"""
        if redbutton.counter < redbutton.times:# 小于则等待
            redbutton.counter += 1             # 统计次数
            screen.ontimer(delay_alt,50)       # 再次调用函数
        else:
            redbutton.counter = 0
            redbutton.index = 1 - redbutton.index       # 下一造型
            redbutton.shape(red_images[redbutton.index])# 切换回去
    delay_alt()
        
pygame.mixer.init()                               # 混音器初始化
pygame.mixer.music.load("audio/Tragedy Flame.wav")# 加载背景音乐
sound = pygame.mixer.Sound("audio/super jump.wav")# 实例化音效对象

screen = Screen()                                 # 新建屏幕对象
screen.setup(480,360)                             # 设定屏幕大小
screen.title("最简音乐播放器_作者：李兴球")       # 设定屏幕标题
blue_images = ["images/pbl.gif","images/sbb.gif"] # 蓝色按钮图表
screen.addshape(blue_images[0])                   # 添加按钮到屏幕
screen.addshape(blue_images[1])                   # 添加按钮到屏幕
red_images = ["images/pbr.gif","images/pbp.gif"]  # 红色按钮图像表
screen.addshape(red_images[0])                    # 添加按钮到屏幕
screen.addshape(red_images[1])                    # 添加按钮到屏幕

bluebutton = Turtle(shape = blue_images[0])       # 新建蓝色按扭
bluebutton.penup()                                # 蓝色按扭抬笔
bluebutton.setx(-120)                             # 设定横向坐标
bluebutton.index = 0                              # 自定索引属性
bluebutton.onclick(playmusic)                     # 绑定单击事件

redbutton = Turtle(shape = red_images[0])         # 新建红色按扭
redbutton.penup()                                 # 红色按扭抬笔
redbutton.setx(120)                               # 设定横向坐标
redbutton.index = 0                               # 自定索引属性
redbutton.counter = 0                             # 设计数器属性
redbutton.times  = 10                             # 设定次数属性
redbutton.onclick(playsound)                      # 绑定单击事件

screen.mainloop()                                 # 进入主循环
