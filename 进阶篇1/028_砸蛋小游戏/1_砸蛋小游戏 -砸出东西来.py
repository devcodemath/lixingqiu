"""砸蛋小游戏-砸出东西来.py,本程序单击蛋蛋后会有道具出现"""
import pygame,glob
from turtle import *
from random import choice,randint

class Prop(Turtle):
    """道具类,当砸到蛋蛋时,生成一个它的实例"""
    def __init__(self,image,position):
        Turtle.__init__(self,visible=False)  # 初始化时不可见
        self.penup()                         # 不需画所以抬笔
        self.shape(image)                    # 设定道具造型
        self.goto(position)                  # 设定坐标
        self.setheading(randint(20,160))     # 设定方向
        self.sw = self.screen.window_width() # 屏幕宽度
        self.sh = self.screen.window_height()# 屏幕高度
        self.showturtle()                    # 显示出来
        self.move()                          # 开始移动
    def move(self):
        """在屏幕范围内不断移动直到超出范围"""
        self.fd(20)
        if abs(self.xcor()) > self.sw or \
           abs(self.ycor()) > self.sh:       # 超过宽高
            self.hideturtle()                # 隐藏对象
            return                           # 立即返回
        self.screen.ontimer(self.move,50)    # 再次运行        
        
class Egg(Turtle):
    def __init__(self,images,position,sound,prop_images):
        Turtle.__init__(self,visible=False)
        self.prop_images = prop_images       # 道具图形表        
        self.images = images                 # 造型列表
        self.index = 0                       # 造型索引号
        self.sound = sound                   # 音效
        self.penup()                         # 抬笔
        self.goto(position)                  # 定位置
        self.shape(images[0])                # 初始为第一个造型        
        self.showturtle()                    # 显示
        self.onclick(self.open)              # 切换到开的造型
        self.counter = 0                     # 单击后自动闭合计时器
        self.times = 1                       # 单击后自动闭合总时间
        
    def open(self,x,y):
        """切换到打开蛋蛋的造型"""
        self.onclick(None)                   # 取消onclick的绑定
        if self.index == 0:
            image = choice(self.prop_images) # 随机选择一张gif图
            Prop(image,self.position())      # 生成一个道具
        self.sound.play()                    # 播放音效   
        self.index = 1                       # 指定造型索引(开)
        self.shape(self.images[self.index])  # 设定造型
        self.delay_close()                   # 延时1秒后关闭
        
    def delay_close(self):
        """延时把蛋蛋关闭"""
        if self.counter<self.times:          # 时间范围内继续等待
            self.counter += 1
            self.screen.ontimer(self.delay_close,1000)
        else:
            self.counter = 0
            self.index = 0                # 切换回闭合的索引
            self.shape(self.images[self.index]) # 设定造型(合)
            self.onclick(self.open)       # 时间到了让单击有效           

if __name__ == "__main__":

    width,height = 480,360                   # 定义宽高
    prop_images = glob.glob("gif/*.gif")     # 道具列表    
    egg_images =['images/造型1.gif','images/造型2.gif']
    
    screen = Screen()                        # 新建屏幕
    screen.delay(0)                          # 延时为0
    screen.title("砸蛋小游戏_作者：李兴球")  # 设置标题
    screen.setup(width,height)               # 设置宽高
    screen.bgpic("images/stage.png") 
    [screen.addshape(image) for image in egg_images]  # 增加蛋蛋造型
    [screen.addshape(image) for image in prop_images] # 增加道具造型

    pygame.mixer.init()                               # 初始化混音器
    pygame.mixer.music.load("audio/8-Bit Numa Numa.wav") # 加载背景音乐
    pygame.mixer.music.play(-1,0)                     # 循环播放音乐
    clicked_sound =pygame.mixer.Sound("audio/THUNK.wav") # 生成音效对象

    pos_list=[(0,0),(-150,-50),(150,-50)]             # 每个蛋的坐标列表
    [Egg(egg_images,pos,clicked_sound,prop_images) for pos in pos_list]
    
    screen.mainloop()
    
        
