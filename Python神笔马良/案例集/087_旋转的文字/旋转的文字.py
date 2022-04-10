"""
   旋转的文字.py
"""
import time
from turtle import *
from write_patch import *

screen = Screen()
screen.tracer(0,0)

tom = Turtle(visible=False)
tom.speed(1)
zt = ('黑体',32,'underline','italic','bold')
a = 0
while True:
    tom.clear()
    tom.write('风火轮编程',align='center',font=zt,angle=a)
    time.sleep(0.01)
    a = a + 1
    a = a % 360
