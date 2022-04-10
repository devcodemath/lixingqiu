"""
   随机赛车双人游戏
   本程序操作红色和青色两架小车去接金币,
   障碍为红色的圈形。碰到障碍物后，小车会自动回到起始坐标。
   接到一个金币后会进行统计。
   这是一个多线程示例程序，两架小车在独自的线程中运行。
   本程序还演示了颜色碰撞和对tkinter的items进行碰撞。
   本程序需要Python精灵模块支持，如果没有安装，请在以下网址下载批处理进行安装。
   http://www.lixingqiu.com/pms.bat

   相关命令说明：

   1、颜色碰撞检测命令collidecolor
   本命令只对造型为图片的角色起作用，它会检测所碰到的角色上面的颜色，
   如果是相应的颜色，则返回真，否则返回假。
   它可以有两个参数，第一个参数是颜色，需要为RGB三元组格式，如(255,0,0)表示的是红色。
   第二个参数应该是一个序列，表示要检测的角色，如果第二个参数为空，则检测所有角色。
   本使中的car1.collidecolor(red,cs)命令，检测的是cs列表中的角色，而red的值是(255,0,0)。
   它的意思car1有没有碰到cs列表中角色上面的红色。

   2、overlap_with，与...重叠命令。
   本命令查找有无和角色最小矩形重叠的项目（包括线条，圆点，多边形，圆弧，图章，填充区域，其它角色)。
   它的参数可以是列表/元组/集合、整数与角色或字符串，返回重叠的所有项目编号。
   本方法返回所有与角色矩形重叠的项目集合。

   典型应用为用一个角色盖一些图章，把这些图章的编号收集起来，然后可以用overlap_with去检测有没有碰到这些图章。
   本例中的金币有一个是角色，其它的都是图章。
   它们的项目编号都放在coins列表中。和海龟画图一样，求一个角色的项目编号用turtle属性的_item值。
   本例coin的项目编号为coin.turtle._item。而所有的图章的项目编号，在盖图章的时候都会直接返回。
   

   
"""
__author__ = '李兴球'
__date__ = '2020/5/27'
__blog__ = 'www.lixingqiu.com'

from sprites import *                # 从精灵模块导入所有命令
from random import random            # 从随机模块导入random命令
from threading import Thread         # 从线程模块导入Thread类 

width,height = 960,720               # 定义宽高
screen = Screen()                    # 生成屏幕
screen.setup(width,height)           # 设置屏幕宽高 
screen.bgcolor('gray')               # 设定背景色
screen.title('随机赛车双人游戏')     # 设定标题  

red = (255,0,0)                      # 代表红色
r = Sprite('res/red.png')            # 障碍物的本体
cs = []                              # cs列表存储所有障碍物
for _ in range(30):
    r.gotorandom(-200,200,-200,200,180)
    x = (10 + random())/50 
    y = r.clone()
    y.shapesize(x,x)
    cs.append(y)
screen.listen()
r.hide()

# 生成一些金币
coin = Sprite(shape='circle')
coin.color('yellow')
coins = [coin.turtle._item]         # coins列表存储的都是些项目编号(整数)
for _ in range(50):
    coin.gotorandom()               # 在到达屏幕范围任一点  
    item = coin.stamp()             # 盖图章
    coins.append(item)              # 添加到coins列表 


def redcarfunc():
    """
       本函数是线程1的目标函数，
       它主要是生成一辆小车，然后可以用上下左右键进行控制，
       并且碰到红色的障碍物，它会回到起始点，
       碰到黄色的圆形，它会得1分，并且黄色圆形会消失。
    """
    score_bug = Sprite(visible=False,pos=(-200,250))
    score_bug.color('red')
    car1 = Sprite('res/redcar.png',pos=(-50,0))
    car1.left(90)
    car1.score = 0                              # 自定义属性
    leftkey = Key("Left")
    rightkey = Key("Right")
    upkey = Key("Up")
    downkey = Key("Down")
    while True:
        if leftkey.down():car1.left(5)
        if rightkey.down():car1.right(5)
        if upkey.down():car1.fd(5)
        if downkey.down():car1.bk(5)    
        if car1.collidecolor(red,cs):car1.slide((-50,0))
        items = car1.overlap_with(coins)
        car1.score += len(items)
        if items:
            [coin.clearstamp(i) for i in items]
            score_bug.clear()
            score_bug.write(car1.score,font=("",32,"normal"))        
        screen.update()
        
thread1 = Thread(target=redcarfunc)            # 创建线程1
thread1.start()                                # 启动线程1

def cyancarfunc():
    """
       本函数是线程2的目标函数，
       它主要是生成一辆小车，然后可以用awsd键进行控制，
       并且碰到红色的障碍物，它会回到起始点，
       碰到黄色的圆形，它会得1分，并且黄色圆形会消失。
    """
    score_bug = Sprite(visible=False,pos=(200,250))
    score_bug.color('cyan')
    car1 = Sprite('res/cyancar.png',pos=(50,0))
    car1.left(90)
    car1.score = 0                              # 自定义属性
    leftkey = Key("a")
    rightkey = Key("d")
    upkey = Key("w")
    downkey = Key("s")
    while True:
        if leftkey.down():car1.left(5)
        if rightkey.down():car1.right(5)
        if upkey.down():car1.fd(5)
        if downkey.down():car1.bk(5)    
        if car1.collidecolor(red,cs):car1.slide((50,0))
        items = car1.overlap_with(coins)
        car1.score += len(items)        
        if items:
            [coin.clearstamp(i) for i in items]
            score_bug.clear()
            score_bug.write(car1.score,font=("",32,"normal"))       
        screen.update()
        
thread2 = Thread(target=cyancarfunc)           # 创建线程2
thread2.start()                                # 启动线程2

PlaySound('Dance Energetic.wav',SND_LOOP|SND_ASYNC)
screen.mainloop()
