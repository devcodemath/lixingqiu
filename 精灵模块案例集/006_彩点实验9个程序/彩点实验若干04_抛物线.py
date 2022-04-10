"""
  彩点实验若干04_抛物.py
"""

from sprites import *

d = Sprite(shape='blank',visible=False)
d.screen.bgcolor('black')

while 1:
    d.randompos()
    if d.ycor() > 0.5 * d.xcor() * d.xcor() /100:
       d.randomcolor()
       d.dot(10)
