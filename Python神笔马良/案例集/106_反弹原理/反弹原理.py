"""
   反弹原理.py
"""
from random import randint
from turtle import Turtle,RawTurtle,Screen

def bounce_on_edge(self):
    """给RawTurtle类新增碰到边缘就反弹的方法"""
    sw = self.screen.window_width()       # 窗口宽度
    sh = self.screen.window_height()      # 窗口高度 
    x = self.xcor()                       # 海龟x坐标
    y = self.ycor()                       # 海龟y坐标
    if x > sw/2 or x < -sw/2:             # 到了最右边或最左边
        self.seth(180 - self.heading())   # 改变方向
    elif y  > sh/2 or y < -sh/2:          # 到了最上边或最下边 
        self.seth( -self.heading())

RawTurtle.bounce_on_edge = bounce_on_edge # 新增方法 

screen = Screen()                         # 新建屏幕
screen.delay(0)                           # 绘画延时为0毫秒

t = Turtle(shape='circle')                # 新建圆形海龟对象
t.speed(0)                                # 设置移动速度为最快
t.penup()                                 # 抬笔
t.setheading(randint(1,360))              # 随机选择一个方向
while True:                               # 当成立的时候 
    t.fd(0.2)                             # 前进0.2个单位
    t.bounce_on_edge()                    # 碰到边缘就反弹 
