"""
  彩点实验若干07_三角函数圆环.py
"""
import math
from sprites import *

d = Sprite(shape='blank',visible=False)
d.screen.bgcolor('black')

while 1:
    d.randomcolor()
    d.randomheading()
    radius = random.randint(150,200)
    angle = math.radians(d.heading())
    x  = radius * math.sin(angle)
    y  = radius * math.cos(angle)
    d.goto(x,y)
    d.dot(10)
    d.home()
    
