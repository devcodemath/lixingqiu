"""
   月满西楼mv.py
   本程序是一幅多媒体动画，主要演示如何继承Sprite类，
   还演示了角色的play方法如何使用。   
"""
__author__ = "李兴球"
__date__ = "2019年12月26日"

import time,os
from sprites import *

class Star(Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self,shape='star',visible=False,pos=(x,y))
        self.cs = ['gray','white']               # 两种颜色，暗和亮
        self.se = [0.15,0.16]                    # 两个大小,
        self.index = 0                           # index属性
        self.show()                              # 显示星星
        self.flash()                             # 闪烁 
        
    def flash(self):
        """闪烁"""
        self.index = 1 - self.index
        self.color(self.cs[self.index])
        self.scale(self.se[self.index])
        t = random.randint(800,1200)
        self.screen.ontimer(self.flash,t)       # 在t毫秒后再次调用flash方法      
        
project_name = '月满西楼'
width,height = 600,600                          # 定义宽度和高度变量

screen = Screen()                               # 新建屏幕
screen.bgcolor('dodger blue')                   # 设定屏幕背景色
screen.setup(width,height)                      # 设定屏幕宽高
screen.title(project_name)                      # 设定窗口标题
screen.bgpic('荷塘月夜-唯美浪漫.png')           # 设定背景图片 

cors = [(0,250),(100,230),(-100,230),(-10,20),(30,50),(150,150),
        (-200,10),(-150,150),(-100,90),(250,130),(220,220),(100,90)]

for x,y in cors:Star(x,y)                       # 在cors中坐标位置生成星星

# 显示标题,在一定时间后会自动清除
w = Sprite(visible=False,shape='title0.png')
w.addy(250)
w.stamp(60)
w.shape('title1.png')
w.addy(-220)
w.stamp(60)

tom = Turtle(visible=False)
tom.color("blue","white")
song_file="邓丽君-月满西楼.wav"                 # 歌曲文件
lrc_file="月满西楼歌词.txt"                     # 歌词文件
fontstyle = ("",24,"normal")  
tom.play(song_file,lrc_file,fontstyle)          # 播放歌曲并显示歌词文件

screen.mainloop()






