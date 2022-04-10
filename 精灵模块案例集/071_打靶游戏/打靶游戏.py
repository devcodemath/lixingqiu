"""
   打靶游戏,本程序还会自动截屏,这样就能制作一个gif文件了.
"""
from sprites import *

width,height = 480,360           # 定义宽高
screen = Screen()                # 新建屏幕
screen.setup(width,height)       # 设置宽高
screen.bgpic('stage.png')        # 设定背景

准心 = Sprite(shape='准心.png')  # 新建准心
弹孔 = Sprite(shape='弹孔.png')  # 新建弹孔

leftkey = Mouse(1)               # 鼠标左键
rightkey = Mouse(3)              # 鼠标右键
score = 0
counter = 0                      # 计数器
while True:                      # 无限循环
    screen.save(f'res/game{counter}.png') # 截屏幕
    counter += 1                          # 计数器增1
    准心.goto(mouse_pos())       # 准心跟随鼠标指针
    if rightkey.down():          # 如单击右键重来
        score = 0
        弹孔.clear()
    if leftkey.down():           # 如单击左键

        # 直到松开才留下弹痕,并且计算得分
        while leftkey.down():screen.update()
        弹孔.goto(mouse_position())
        弹孔.stamp()
        if 弹孔.distance(0,0)<30:
            score += 5
        elif 弹孔.distance(0,0)>30 and 弹孔.distance(0,0)<63:
            score += 3
        elif 弹孔.distance(0,0)>63 and 弹孔.distance(0,0)<93:
            score += 2
        elif 弹孔.distance(0,0)>93 and 弹孔.distance(0,0)<123:
            score += 1
        screen.title('当前得分' + str(score))
            
            
        
