"""
   旋转模式.py
   精灵的旋转模式有三种,0代表360度旋转,1代表左右翻转,2代表不旋转。
"""
from sprites import *

screen = Screen()              # 新建屏幕对象
screen.setup(480,360)          # 设定屏幕宽高

s0 = Sprite(2,pos=(0,100))     # 新建小猫角色
s0.rotatemode(0)               # 设定旋转模式360度旋转
s0.setheading(45)
s0.say('我要任意360度旋转',100000,False)

s1 = Sprite(2,pos=(0,0))       # 新建小猫角色
s1.rotatemode(1)               # 设定旋转模式左右翻转
s1.setheading(46)
s1.say('左右翻转就OK了',100000,False)

s2 = Sprite(2,pos=(0,-100))     # 新建小猫角色
s2.rotatemode(2)                # 设定旋转模式不旋转
s2.setheading(85)
s2.say('我就不旋转',100000,False) 

while 1:
    s0.fd(10)
    s0.bounce_on_edge()
    
    s1.fd(10)
    s1.bounce_on_edge()
    
    s2.fd(10)
    s2.bounce_on_edge()
    time.sleep(0.1)
    
    
