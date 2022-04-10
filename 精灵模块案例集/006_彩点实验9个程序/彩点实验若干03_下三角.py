"""
  彩点实验若干03_下三角.py
"""

from sprites import *

d = Sprite(shape='blank',visible=False)
d.screen.bgcolor('black')

while 1:
    d.randompos()
    if d.xcor() > d.ycor():
       d.randomcolor()
       d.dot(10)
