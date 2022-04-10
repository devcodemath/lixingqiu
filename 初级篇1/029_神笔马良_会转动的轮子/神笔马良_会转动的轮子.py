"""神笔马良_会转动的轮子.py
   着重理解轮子每旋转angle度,那么它应该移动多少距离。
 
"""
import math
from turtle import *
from time import sleep

width,height = 600,300            # 宽,高定义
radius = 100                      # 圆的半径
周长 = 2 * radius * math.pi       # 周长公式
angle = 5                         # 每次旋转的度数
step = angle * 周长/360           # angle * 每度移动的距离

screen = Screen()                 # 新建屏幕
screen.setup(width,height)        # 设屏幕宽高
screen.delay(0)                   # 屏幕延时为0
screen.bgcolor("gray")            # 背景色为灰色
screen.title("会转动的轮子")      # 屏幕标题

t = Turtle()                      # 新建海龟对象
t.color("cyan")                   # 设定颜色为青色

t.begin_poly()                    # 开始记录顶点
for i in range(20):               # 重复20次
    t.fd(radius)                  # 前进100个单位
    t.begin_fill()                # 开始填充
    t.circle(8)                   # 画圆
    t.end_fill()                  # 结束填充
    t.bk(radius)                  # 倒退100个单位
    t.rt(18)                      # 右转18度
t.end_poly()                      # 结束记录顶点
t.penup()                         # 抬笔
p = t.get_poly()                  # 获取所有顶点坐标
screen.addshape('wheel',p)        # 添加形状为wheel
t.clear()                         # 清空自己所画图形
t.shape('wheel')                  # 把自己的形状设为wheel
t.speed(0)                        # 设速度为最快

while True:
    t.right(angle)                # 右转angle度
    t.setx(t.xcor() + step)       # 相应地要前进step个单位
    if abs(t.xcor())+radius+16  > width//2: # 到边缘反弹
        step = -step
        angle= -angle
    sleep(0.04)
    
