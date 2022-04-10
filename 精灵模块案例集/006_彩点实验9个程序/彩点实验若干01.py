"""
  彩点实验若干01.py
"""

from sprites import *

d = Sprite(shape='blank',visible=False)
d.screen.bgcolor('black')

while 1:
    d.randompos()
    d.randomcolor()
    d.dot(random.randint(10,100))
