"""白桦林的故事.py，本程序新建Snow类生成粒子效果做为雪花飘落。
名为sing的函数生成一只海龟，用来在屏幕上显示歌词并播放音乐。"""

__author__ = "李兴球"
__date__   = "2019/2/20"

from turtle import Turtle,Screen
from random import randint,choice
from musicwithlrc import *
from winsound import PlaySound,SND_ASYNC
from tkinter import messagebox

def sing(filename,srcfilename):
    """播放音乐并显示歌词"""
    ziti = ("楷体",22,"normal")                 # 字体样式 
    time_and_lrc = make_septime_lrc(srcfilename)# 时间和歌词
    lrc_amounts = len(time_and_lrc)             # 歌词数量 
    writer = Turtle(visible=False)              # 此作者是海龟
    writer.penup()                              # 抬笔
    writer.sety(30)                             # 设定y坐标
    writer.color("blue")                        # 字的颜色
    PlaySound(filename,SND_ASYNC)               # 播放音乐 
    lrc_index = 0                               # 歌词索引从0开始
     
    def display_lrc():                          # 定义显示歌词函数
        """从列表获取歌词显示出来"""
        nonlocal lrc_index                      # 非本地变量
        if lrc_index < lrc_amounts:             # 索引小于数量则显示歌词
            septime,lrc = time_and_lrc[lrc_index]
            writer.clear()                      # 写新歌词前先擦掉
            writer.write(lrc,align='center',font=ziti) # 显示歌词
            writer.screen.ontimer(display_lrc,septime) # 时间到显示下一句
            lrc_index = lrc_index + 1            # 索引加1 
    display_lrc()        
        
class Snow(Turtle): 
    def __init__(self):        
        Turtle.__init__(self,shape='dot',visible=False)
        self.penup()
        self.color("white")                       # 雪花颜色
        self.sh = self.screen.window_height()     # 屏幕高度
        self.sw = self.screen.window_width()      # 屏幕宽度
        self.init()
        
    def init(self):
        self.ht()                                 # 隐藏自己
        x = randint(-self.sw//2,self.sw//2)       # 设置x坐标
        y = randint(self.sh,self.sh*2)            # 设置y坐标
        self.goto(x,y)                            # 坐标定位
        self.xspeed = randint(-1,1)               # 横向速度
        self.yspeed = randint(-2,-1)              # 垂直速度
        self.st()                                 # 显示自己
        
    def move(self):
        """根据x和y速度移动"""
        x = self.xcor() + self.xspeed   # 水平坐标增加横向速度
        y = self.ycor() + self.yspeed   # 垂直坐标增加垂直速度   
        self.goto(x,y)         
        if y < -self.sh//2 :            # 到屏幕最低就重新init
            self.init()
            
def close_window():
    """单击屏幕把running设为False，这样while循环就结束了"""
    global running    
    if messagebox.askokcancel("白桦林", "你真的要离开吗？"):
        running = False
    
if __name__ == "__main__":
    
    counter = 0                         # 计数器变量
    amounts = 150                       # 设定粒子总数
    width,height = 480,360              # 定义屏幕宽高
    running = True                      # 运行标志
    
    screen = Screen()                   #  新建屏幕
    screen.addshape("dot",((0,0),(0,0)))# 设定dot形状
    screen.setup(width,height)          # 设定屏幕宽高
    screen.bgcolor("black")             # 设定屏幕背景
    screen.bgpic("bg.png")              # 设定背景图片
    screen.title("白桦林的故事_程序制作:李兴球")# 设定标题   
    screen.delay(0)                     # 设定屏幕延时
    
    screen.onclick(lambda x,y:close_window()) # 单击屏幕关窗
    root = screen._root                 # _root继承自Tk类
    # 下一句表示当按窗口关闭按钮时调用close_window函数
    root.ondestroy(close_window)     
    
    sing("白桦林.wav","白桦林.lrc")     # 显示歌词放音乐    
    ps = []                             # 定义粒子列表
    while running:                      # 进入循环
        if counter < amounts:           # 未达指定数量
           p = Snow()                   # 生成雪花粒子
           ps.append(p)                 # 添加到列表
           counter += 1                 # 计数器加一                             
        [p.move() for p in ps]          # 移动每个粒子
        screen.update()                 # 屏幕刷新重画
    root.destroy()                      # 销毁窗口
    

    
