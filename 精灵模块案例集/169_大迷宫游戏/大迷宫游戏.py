"""
   大迷宫游戏.py
   小老鼠在一个偌大的迷宫中迷失了方向,请按上下左右方向箭头操作它移动。
   找到出口，走出迷宫。
   本程序需要python精灵模块1.35版本以上支持。
   安装最新版本请用cmd打开命令提示符管理员窗口输入以下命令：
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sprites  --upgrade
   本程序主要演示的像素级碰撞检测命令pixelcollide。它返回碰撞点坐标，
   主碰方(在这里是老鼠)碰撞点的像素值，被碰方(这时是迷宫)，重叠区域矩形。就像下面这样：
   ((14.0, 3.0), (45, 45, 45), (104, 104, 104), (-17.0, 9.0, 18.0, -9.0, 630.0))
   最后重叠区域是一个五元组，这个五元组最后一个值是重叠区域的面积。
   问题是，小老鼠最后找到了绿色的出口，可怎么也无法进门！
   当你理解了pixelcollide的返回值后，相信你能对此程序进行修改，从而解决小老鼠的问题。
   
"""
from sprites import *           # 从精灵模块导入所有命令  
from pygame import mixer        # 从pygame模块导入混音器

screen = Screen()
screen.setup(480,360)
screen.title('大迷宫游戏')

mixer.init()
mixer.music.load('胡伟立 - 周旋过场.mp3')
mixer.music.play(-1,0)          # 从头开始循环播放
maze = Sprite('1.png')          # 新建迷宫
maze.scale(2)                   # 迷宫长宽扩大为原来2倍
maze.ondrag(None)               # 让迷宫不可拖动，(maze.draggable()能让它重新可拖动)

# 新建有两个造型的老鼠角色
rat = Sprite(['res/rat1.png','res/rat2.png']) 
rat.shapesize(0.5,0.6)

leftkey = Key("Left")           # 向左方向箭头
rightkey = Key("Right")         # 向右方向箭头 
upkey = Key("Up")               # 向上方向箭头
downkey = Key("Down")           # 向下方向箭头
screen.listen()                 # 监听屏幕按键
r = None
while True:
    if leftkey.down():          # 按左方向箭头往左移
        rat.nextcostume()
        rat.setheading(180)
        maze.addx(5)        
        r = rat.pixelcollide(maze)
        if r:maze.addx(-5)
    if  rightkey.down():        # 按右方向箭头往左移
        rat.nextcostume()
        rat.setheading(0)
        maze.addx(-5)        
        r = rat.pixelcollide(maze)
        if r:maze.addx(5)
    if  upkey.down():           # 按上方向箭头往左移
        rat.nextcostume()
        rat.setheading(90)
        maze.addy(-5)        
        r = rat.pixelcollide(maze)  
        if r:maze.addy(5)
    if downkey.down():          # 按下方向箭头往左移
        rat.nextcostume()
        rat.setheading(-90)
        maze.addy(5)        
        r = rat.pixelcollide(maze)    # 对rat和maze进行像素极碰撞检测
        if r:maze.addy(-5)
    if r: print(r)
    screen.update()
