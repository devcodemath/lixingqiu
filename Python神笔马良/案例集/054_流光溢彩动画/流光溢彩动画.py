"""
   本程序实现流光溢彩的动画效果
"""
from turtle import *
from coloradd import *

c = (255,0,0)
t = Turtle()
t.width(40)
t.screen.colormode(255)
t.screen.tracer(0,0)    # 关闭自动刷新和绘画延时

while 1 : 
    t.clear()           # 清除以前所画
    for _ in range(100):
        t.color(c)
        c = coloradd(c,0.01)
        t.fd(2)
    
    t.screen.update()   # 手动刷新屏幕 
    t.bk(200)
