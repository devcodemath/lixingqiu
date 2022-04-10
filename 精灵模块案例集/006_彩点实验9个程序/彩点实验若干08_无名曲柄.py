"""
  彩点实验若干06_菱正方.py
"""

from sprites import *

d = Sprite(shape='blank',visible=False)
d.screen.bgcolor('black')

while 1:
    d.randompos()
    x,y = d.position() 
    if  x * x + y *x < 10000: 
       d.randomcolor()
       d.dot(10)
