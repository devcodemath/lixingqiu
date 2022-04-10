"""
  彩点实验若干02_圆形.py
"""

from sprites import *

d = Sprite(shape='blank',visible=False)
d.screen.bgcolor('black')

radius = 200
while 1:
    d.randomcolor()
    d.randomheading()
    d.fd(random.randint(1,radius))
    d.dot(10)
    d.home()
    
