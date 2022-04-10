"""
   沙漠横版动画.py
   这是横版过关游戏的动画基础,原理都一样,
   无论是用pygame或者turtle实现.
"""
import time
from sprites import Sprite,Screen

screen = Screen()
screen.screensize(1,1)
screen.setup(600,295)
screen.bgpic('沙漠.png')

sp = Sprite('沙漠.png',pos=(600,0))
speed=5

while True:
    screen.move(-speed,0)                #  背景往后移
    if screen.xcor()<=-600:screen.setx(600)
    sp.bk(speed)                         # 角色往后移
    if sp.xcor()<=-600:sp.setx(600)
    screen.update()
