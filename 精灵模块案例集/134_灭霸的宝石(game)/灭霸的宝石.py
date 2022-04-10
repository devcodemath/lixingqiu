"""
    灭霸的宝石.py
    本程序运行后通过鼠标指针操作角色,让它去接'宝石'
"""
from sprites import *
from time import sleep
from random import randint

gems = []                                 # 新建列表，装宝石的
screen = Screen()                         # 新建屏幕
screen.setup(843,468)                     # 设定屏幕宽高
screen.bgpic('星空背景.png')              # 设定屏幕背景
screen.title('灭霸的宝石')                # 设定屏幕标题

for x in range(10):                       # 在range(10)范围内迭代x
    x = randint(-400,400)                 # 生成一个x坐标 
    y = randint(240,690)                  # 生成一个y坐标
    g = Sprite(shape='circle',pos=(x,y))  # 新建一个叫g的角色
    g.randomcolor()                       # 随机颜色
    gems.append(g)                        # 添加到宝石列表

mieba = Sprite('灭霸.png')                # 新建灭霸角色
mieba.sety(-200)                          # 设定灭霸的y坐标 

while True:                               # 当成立的时候
    mx,my = mouse_pos()                   # 获取鼠标指针的x,y坐标
    mieba.setx(mx)                        # 设定灭霸的x坐标为mx
    for g in gems:                        # 对于gems中的每一颗宝石
        g.addy(-5)                        # 往下移5个单位
        # 如果宝石的y坐标小于-234或者碰到灭霸,则隐藏换颜色到最上面去
        if g.ycor() < -234 or g.collide(mieba):
            g.hide()                      # 隐藏 
            x = randint(-400,400)         # 设定x坐标 
            y = randint(240,690)          # 设定y坐标
            g.randomcolor()               # 设定随机颜色
            g.goto(x,y)                   # 到x,y坐标
            g.show()                      # 显示出来
    sleep(0.01)                           # 等待0.01秒   
            
