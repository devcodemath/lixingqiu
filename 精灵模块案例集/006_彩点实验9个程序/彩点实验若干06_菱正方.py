"""
  彩点实验若干06_菱正方.py
"""

from sprites import *

d = Sprite(shape='blank',visible=False)
d.screen.bgcolor('black')

while 1:
    d.randompos()
    c = abs(d.xcor()) + abs(d.ycor())  
    if c < 200:
       d.randomcolor()
       d.dot(10)
