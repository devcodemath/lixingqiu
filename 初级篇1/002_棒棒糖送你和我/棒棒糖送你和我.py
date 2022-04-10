"""棒棒糖送你和我.py 本程序画一个棒棒糖样的图形,引入了coloradd模块里的coloradd命令。
   coloradd命令可以把RGB形式的颜色向着“红橙黄绿青蓝紫”的方向增加。
"""
from turtle import *
from coloradd import * 

screen = Screen()     # 新建屏幕
screen.colormode(255) # 设定屏幕颜色模式
screen.delay(0)       # 设定屏幕延时
screen.setup(640,480) # 设定屏幕宽高
screen.title("棒棒糖交互动画")

t = Turtle(undobuffersize = 2000)   # 新建海龟,可撤销次数为2000
t.hideturtle()
t.shape('blank')

color = (255,0,0)     # RGB红色
for i in range(300):  # 重复300次
    t.width(i/10)     # 画笔笔迹宽度
    t.fd(i/10)        # 海龟前进
    t.rt(10)          # 海龟右转
    color = coloradd(color,0.01) #颜色增加
    t.pencolor(color) # 画笔颜色
    
t.penup()             # 抬笔
t.home()              # 回家到原点
t.setheading(-90)     # 方向向下
t.color("brown")      # 画笔颜色棕色
t.pendown()           # 落笔
t.fd(440)             # 前进

def rev(x,y):
    while t.undobufferentries(): # 获取可撤销次数
       t.undo()
    t.write("再见!",align='center',font=(None,24,'normal'))
       
screen.onclick(rev)    # 单击运行rev函数
screen.mainloop()
