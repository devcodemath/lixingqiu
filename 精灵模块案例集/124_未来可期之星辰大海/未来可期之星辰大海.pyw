"""
   未来可期之星辰大海.py
   本程序演示两个动画,从文件中读取字符串,从左到右显示出来
"""
from sprites import *                           # 从精灵模块导入所有命令

PlaySound('流浪者(剪).wav',SND_LOOP|SND_ASYNC)  # 循环播放背景音乐

screen = Screen()                               # 新建屏幕 
screen.setup(800,600)                           # 设定宽高 
screen.bgpic('星空背景.png')                    # 贴上背景
screen.title('未来可期之星辰大海by李兴球www.lixingqiu.com')              # 写上标题

brain = Sprite(shape='brains',pos=(0,170))      # 大脑动画角色
man = Sprite(shape='ironmans',pos=(0,-160))     # 钢铁侠动画角色

f = open('文字说明.txt')                        # 打开文字说明 
c = f.read()                                    # 读取文件
f.close()                                       # 关闭文件

txt2image(c,'res/zi.png',color=(255,250,0))     # 文字转换成图像
subtitle = Sprite('res/zi.png',pos=(1598,0))    # 新建字幕角色 

while True:                                     # 当成立的时候 
    subtitle.bk(5)                              # 字幕往左移5个单位
    if subtitle.xcor()<-1598:                   # 如果x坐标小于-1598 
        subtitle.setx(1598)                     # 则设定x坐标为1598
    brain.nextcostume()                         # 大脑角色切换造型
    man.nextshape()                             # 钢铁侠角色切换造型
    time.sleep(0.1)                             # 等待0.1秒
    
