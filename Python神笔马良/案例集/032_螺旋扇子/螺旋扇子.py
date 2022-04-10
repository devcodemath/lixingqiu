"""
   螺旋扇子.py
"""
import turtle
from coloradd import *      # 从coloradd命令导入所有命令

turtle.bgcolor('black')
turtle.colormode(255)       # 把颜色模式设置为255
c = (0,255,255)

for i in range(1,181):
    ys = lightset(c,i/181)  # 设置c的亮度，返回到ys
    turtle.color(ys)        # 把ys设置为画笔颜色
    turtle.fd(i)            # 海龟前进i
    turtle.bk(i)            # 海龟倒退i
    turtle.right(2)         # 海龟右转2度
    
turtle.done()               # 事件循环
