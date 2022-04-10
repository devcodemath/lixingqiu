"""
   彩色十字架跳高台(颜色碰撞).py
"""
from sprites import *

ft = ('黑体',24,'normal')
screen = Screen()                 # 新建屏幕
screen.setup(960,720)             # 设定宽高

platform = Sprite('platform.png') # 平台
cross= Sprite('cross.png')        # 十字架
cross.write("本程序演示颜色碰撞",align='center',font=ft)
crossgreen = (0,128,0)            # 十字架的绿色 
crossred = (255,0,0)              # 十字架的红色
crossorange = (255,165,0)         # 十字架的橙色
crossblue = (0,0,255)             # 十字架的蓝色

leftkey = Key("Left")             # 左方向箭头
rightkey = Key("Right")           # 右方向箭头
upkey = Key("Up")                 # 上方向箭头
screen.listen() 
dy = 0                            # 垂直速度

while True:
    # 十字架的蓝色和迷宫的蓝色的碰撞检测
    point = cross.coloroverlap(crossblue,(2,64,255))    
    if point:                    # 碰到了就往上移1个单位  
        cross.addy(1)
        dy = 0         
    else:
        cross.addy(dy)           # 没碰到就自由落体运动
        dy = dy -2
        p3 = cross.coloroverlap(crossorange,(2,64,255))
        if p3:dy = -dy
        
    if leftkey.down():           # 按左键就往左移
        cross.addx(-5)
        p1 = cross.coloroverlap(crossgreen,(2,64,255))
        if p1:cross.addx(5)
        
    if rightkey.down():          # 按右键就往右移
        cross.addx(5)
        p2 = cross.coloroverlap(crossred,(2,64,255))
        if p2:cross.addx(-5)
        
    if upkey.down() and point:             # 按上方向箭头跳跃 
        dy = 14
        cross.addy(dy)

    screen.update()
    


