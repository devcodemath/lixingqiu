"""漂亮正方形.py,本程序会用嵌套的for循环画一个漂亮的正方形般的图案."""

from turtle import *
from coloradd import *

def draw_square(turtle,length):
    """用海龟turtle画边长为length的正方形"""
    for _ in range(4):     # 可以用下划线做为变量名称
       turtle.fd(length)   # 让海龟turtle前进length 
       turtle.rt(90)       # 右转90度

screen = Screen()          # 新建屏幕对象
screen.colormode(255)      # 颜色模式设为255
screen.delay(0)            # 屏幕延时为0

colour = (255,0,0)         # 红色的RGB值
t = Turtle()               # 新建海龟对象

t.speed(0)                  # 速度为最快
t.color(colour)             # 初始颜色为colour

for _ in range(4):
    for i in range(100):        
        draw_square(t,i)
        colour = coloradd(colour,0.01)
        t.color(colour)
    t.rt(90)
