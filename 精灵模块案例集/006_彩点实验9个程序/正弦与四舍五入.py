"""
   正弦与四舍五入彩点实验.py
"""
import math
from sprites import *

screen = Screen()
screen.bgcolor('black')
screen.tracer(0,0)

bug = Sprite(visible=False)

while True:
    bug.gotorandom()
    x = bug.xcor()
    y = bug.ycor()
    b1 = round(math.sin(math.radians(x)))
    b2 = round(math.sin(math.radians(y)))
    if b1 == b2:
        bug.randomcolor()
        bug.dot(10)
        bug.update()
        
                            
                                               
    
