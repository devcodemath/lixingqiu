"""砸蛋小游戏.py 这是简单版本,本程序新建了一个Egg类,用鼠标单击它会换造型."""
import pygame
from turtle import *

class Egg(Turtle):
    def __init__(self,images,position,sound):
        Turtle.__init__(self,visible=False)
        self.images = images                 # 造型列表
        self.index = 0                       # 造型索引号
        self.sound = sound                   # 音效
        self.penup()                         # 抬笔
        self.goto(position)                  # 定位置
        self.shape(images[0])                # 初始为第一个造型
        self.showturtle()                    # 显示
        self.onclick(self.next_costume)      # 单击绑定：下一个造型
        
    def next_costume(self,x,y):
        """切换到下一个造型"""
        self.sound.play()                    # 播放音效       
        self.index = 1 - self.index          # 指向下一个造型
        self.shape(self.images[self.index])  # 设定造型

if __name__ == "__main__":

    width,height = 480,360                   # 定义宽高
    egg_images =['images/造型1.gif','images/造型2.gif']
    
    screen = Screen()                        # 新建屏幕
    screen.delay(0)                          # 延时为0
    screen.title("砸蛋小游戏_作者：李兴球")  # 设定标题
    screen.setup(width,height)               # 设置宽高
    screen.bgpic("images/stage.png")         # 设置背景
    [screen.addshape(image) for image in egg_images] # 注册造型

    pygame.mixer.init()                      # pygame初始化
    pygame.mixer.music.load("audio/8-Bit Numa Numa.wav") # 加载音乐
    pygame.mixer.music.play(-1,0)                  # 循环播放
    clicked_sound =pygame.mixer.Sound("audio/THUNK.wav") # 加载音效

    egg1 = Egg(egg_images,(0,0),clicked_sound)     # 生成蛋蛋
    egg2 = Egg(egg_images,(-150,-50),clicked_sound)# 生成蛋蛋
    egg3 = Egg(egg_images,(150,-50),clicked_sound) # 生成蛋蛋
    
    screen.mainloop()
    
        
