"""
  彩点实验若干05_椭圆.py
"""

from sprites import *

d = Sprite(shape='blank',visible=False)
d.screen.bgcolor('black')
dot1 = (-100,0)
dot2 = (100,0)
while 1:
    d.randompos()
    d1 = d.distance(dot1)
    d2 = d.distance(dot2)    
    if d1 + d2 < 300:
       d.randomcolor()
       d.dot(10)
