"""
   滚动的汉字.py
"""
import time
from turtle import *
from write_patch import *

width,height = 480,360
screen = Screen()
screen.tracer(0,0)
screen.setup(width,height)

tom = Turtle(visible=False)
tom.penup()
tom.speed(1)

a = 0
da = 1                              # 每次转动的角度
radius = 50                         # 圆形的半径
perimeter = 2*3.14159*radius        # 周长
dx = perimeter * da/360             # 海龟每次移动的水平距离
zt = ('黑体',32,'normal')
tom.setx(-width/2-radius)           # 移到屏幕最左边

while tom.xcor() -radius < width/2:
    tom.clear()
    tom.dot(radius * 2,'cyan')
    tom.color('red')
    tom.pendown()                   # 落笔
    tom.fd(radius)                  # 画线条
    tom.penup()                     # 抬笔
    tom.bk(radius)
    tom.write('风',align='center',font=zt,angle=a)
    tom.right(da)                   # 海龟向右转
    tom.setx(tom.xcor() + dx)
    time.sleep(0.01)
    a = a - da                      # 字的角度越来越小，也是向右转
    a = a % 360
screen.mainloop()                   # 进入主循环            
