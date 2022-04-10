"""
   自动贪吃蛇.py
"""
from time import sleep
from random import *
from turtle import Turtle,Screen

def _bounce_on_edge(self):
    """到边缘就反弹"""
    sw = self.screen.window_width()
    sh = self.screen.window_height()
    if self.xcor() > sw//2 or self.xcor()<-sw//2:
        self.right(180)
    if self.ycor()>sh//2 or self.ycor()<-sh//2:
        self.right(180)
# 给Turtle类增加碰到边缘就反弹的方法
Turtle.bounce_on_edge = _bounce_on_edge

screen = Screen()                     # 新建屏幕
screen.setup(480,360)                 # 设置屏幕窗口
screen.title('自动贪吃蛇by李兴球')    # 设置窗口标题

tom = Turtle(shape='square')          # 新建叫tom的海龟
tom.shapesize(0.5)                    # 设定形状缩放率
tom.speed(0)                          # 速度最快
tom.penup()                           # 抬笔

# 下面是盖十个图章
for _ in range(10):                
    tom.stamp()

while True:
    tom.clearstamps(1)                # 清除最早盖的章 
    tom.stamp()                       # 盖一个章
    tom.fd(12)                        # 前进12个单位
    tom.bounce_on_edge()              # 碰到边缘就反弹
    if randint(1,30)==1:              # 设定一定的机率转向
        tom.right(choice([1,-1])*90)
    sleep(0.01)                       # 等待0.01秒
