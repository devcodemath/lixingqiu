"""
   颜色碰撞示例程序.py
   本程序演示颜collidecolor命令,它可以检测角色有没有碰到其它角色上面的颜色。
   注意，这个命令对背景颜色/图片/图章/角色所画的图形颜色无效。
"""
from sprites import *

screen = Screen()
screen.title('collidecolor颜色碰撞演示程序')

w = Sprite(visible=False)           # 用于写字的角色
w.addy(100)

blue = Sprite('blue.png')           # 中间的蓝色方块
r1 = Sprite('p1.png',pos=(100,100)) # 右上角的十字架
r2 = Sprite('p2.png')               # 随鼠标移动的十字架

c1 = (0,255,255)                    # 代表青色
c2 = (0,0,255)                      # 代表蓝色
clock = Clock()                     # 时钟对象

while 1:   
    r2.goto(mouse_pos())                # r2跟随鼠标移动  
    flag = r2.collidecolor(c2)          # r2是否碰到蓝色
    if flag:                            # 如果碰到,在标题栏显示
       screen.title('碰到蓝色')
       w.write("碰到蓝色",align='center')
    else:
       screen.title('')                 # 否则在屏幕标题栏显示空字符串
       w.clear()
    clock.tick(60)

