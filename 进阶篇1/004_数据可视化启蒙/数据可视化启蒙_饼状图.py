"""数据可视化启蒙_饼状图.py
本程序根据输入的百分比数,生成饼状图,新的知识点有numinput方法."""
import sys
from turtle import *

width,height = 480,360
screen = Screen()
screen.bgcolor("white")
screen.setup(width,height)
title,prompt = "百分比","请输入0到100之间的整数"
percent = screen.numinput(title,prompt,maxval=100,minval=0,default=30)
 
if percent == None:
    screen.bye()
    sys.exit()
angle = 360 * percent//100 # 算出要旋转的角度
radius = 100               # 设定半径
t = Turtle(shape='turtle') # 新建海龟对象
t.color('green')           # 把海龟变绿

t.fd(radius)            # 前进半径个单位
t.left(90)              # 左转90度准备画圆

t.begin_fill()          # 开始填充
t.circle(radius)        # 画圆
t.end_fill()            # 结束填充

t.right(90)             # 右转90度,准备回去
t.bk(radius)            # 倒退半径个单位

t.color('red')          # 红色代表所占的百分比颜色
t.begin_fill()          # 开始填充
t.fd(radius)            # 前进半径个单位
t.left(90)              # 左转90度准备画弧
t.circle(radius,angle)  # 画弧
t.goto(0,0)             # 回到原点
t.end_fill()            # 结束填充
t.penup()               # 抬笔

t.goto(0,120)           # 到上面准备写字
t.color('black')
info = str(percent) + "%"
t.write(info,align='center',font=('黑体',24,'normal'))
screen.title(info)
t.ht()
screen.exitonclick()







    
