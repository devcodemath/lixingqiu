"""
   诗韵竹林_自动演示版.py
"""
from sprites import *

PlaySound("竹苑情歌.wav",SND_ASYNC|SND_LOOP) # 重复播放背景音乐 

pngs = []                                    # 存储每个诗角色的造型列表
txtfiles = ['大风歌.txt','登鹳雀楼.txt',
            '登幽州台歌.txt','击壤歌.txt',            
            '梅花.txt','编程乐.txt',
            '江南.txt','静夜思.txt','凉州词.txt']

# 这个for循环把文本文件转换成png图片并添加到pngs列表中
for f in txtfiles:                           # 每一个文本文件
    filename = 'res/' + f + ".png"           # 输出的png图像文件名
    txt4image(f,filename)                    # 文本文件转换成图像文件
    pngs.append(filename)                    # 添加到pngs列表

poems = []                                   # 存储每个诗角色的列表   
screen = Screen()                            # 新建屏幕
screen.setup(800,600)                        # 设定屏幕宽高
screen.bgpic('bg4.png')                      # 贴上屏幕背景图片
screen.title('诗韵竹林_自动演示版')          # 设定窗口标题

xy = (-1000,0)
for p in pngs:                               # 对于每一张png图片  
    shi = Sprite(p,pos=xy,visible=False)     # 新建不可见角色
    shi.scale(2)                             # 扩大为2倍
    poems.append(shi)                        # 添加到诗列表

index = 0                                    # 新建一个变量
while True:                                  # 当成立的时候
    p = poems[index]                         # 取索引为index的诗
    p.show()                                 # 显示出来
    p.slide((0,0),1000)                      # 滑行到中间
    p.wait(5)                                # 等待5秒       
    p.slide((1000,0),1000)                   # 滑行到(1000,0)
    p.hide()                                 # 隐藏
    p.goto(-1000,0)                          # 回到(-1000,0)
    index = index + 1                        # 索引加1 
    index = index % len(poems)               # 索引对诗的数量求余
