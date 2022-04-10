"""
   reborn重生命令演示.py
   reborn会隐藏对象，然后让对象在新的坐标显示出来。
   调用reborn时还能设定它的dx和dy，即水平速度和垂直速度。
"""
from sprites import *

width ,height = 480,360
screen = Screen()
screen.bgcolor('blue')
screen.setup(width,height)

bug = Sprite()
bug.dx = 1
bug.dy = 0

clock = Clock()
while 1:
    bug.move(bug.dx,bug.dy)
    screen.title(str(bug.position()))
    if bug.xcor() > width//2:
        bug.reborn(-width//2,0,bug.dx,bug.dy)
    clock.tick(60)
