"""
   月满西楼mv.py
   
"""
__author__ = "李兴球"
__date__ = "2019年12月24日"

import time,os

from sprites import *
from winsound import PlaySound,SND_ASYNC

class Star(Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self,shape='star',visible=False,pos=(x,y))
        self.cs = ['gray','white']
        self.se = [0.15,0.16]
        self.index = 0        
        self.show()
        self.flash()
        
    def flash(self):
        """闪烁"""
        self.index = 1 - self.index
        self.color(self.cs[self.index])
        self.scale(self.se[self.index])
        t = random.randint(800,1200)
        self.screen.ontimer(self.flash,t)        
        
project_name = '月满西楼'
width,height = 600,600
screen = Screen()
screen.bgcolor('dodger blue')
screen.setup(width,height) 
screen.title(project_name)
screen.bgpic('荷塘月夜-唯美浪漫.png')

cors = [(0,250),(100,230),(-100,230),(-10,20),(30,50),(150,150),
        (-200,10),(-150,150),(-100,90),(250,130),(220,220),(100,90)]
for x,y in cors:Star(x,y)

# 显示标题,在一定时间后会自动清除
w = Sprite(visible=False,shape='title0.png')
w.addy(250)
w.stamp(60)
w.shape('title1.png')
w.addy(-220)
w.stamp(60)

piter= Sprite(visible=False )
piter.color("white")

"""在舞台上印歌词代码段"""
song_file="邓丽君-月满西楼.wav"    # 歌曲文件
lrc_file="月满西楼歌词.txt"        # 歌词文件
words_list=[]                      # 歌词列表
words_index=0

f = open(lrc_file)
words_=f.readlines()                         
f.close()

words_list=[ line.strip() for line in words_ if len(line)>1]  
words_lines=len(words_list)

PlaySound(song_file, SND_ASYNC) # 异步播放音效

def get_time_axis(index):
    """获取时间轴"""
    songtime=words_list[index]
    songtime=songtime.split("]")[0]
    songtime=songtime.split(":")
    songtimef=songtime[0][1:3]
    songtimef=int(songtimef)*60    
    songtimem=float(songtime[1])
    return int((songtimef+songtimem)*1000)
 
words_index=0
begin_time=time.time()
def display_subtitle():
    """随着音乐显示歌词函数"""
    global words_index            # 歌词索引号
    global words_lines            # 歌词line数

    ziti = ("",24,"normal")    
    current_time=time.time()
    running_time=(current_time-begin_time)*1000
    screen.title(project_name + "," + str(running_time))
    if running_time > get_time_axis(words_index):
        piter.clear()
        display_words_=words_list[words_index].split("]")[1]
        piter.goto(0,0)
        piter.color("black")
        
        piter.write(display_words_,align='center',font=ziti)
        piter.goto(-1,-1)
        piter.color("white")
        piter.write(display_words_,align='center',font=ziti)    
        words_index=words_index+1
        
    if words_index<words_lines:        
        screen.ontimer(display_subtitle,100)
        
display_subtitle()
screen.mainloop()






