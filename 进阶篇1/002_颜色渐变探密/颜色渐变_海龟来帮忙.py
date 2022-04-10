"""颜色渐变_海龟来帮忙.py"""

from coloradd import coloradd

color_list = []
color = (255,0,0)                 # 从红色开始
for i in range(0,200):            # 重复200次
    color = coloradd(color,0.01)  # 颜色增加0.01
    color_list.append(color)      # 添加到列表

from turtle import Turtle,Screen  # 导入Turtle类及Screen命令

screen = Screen()                 # 新建屏幕对象
screen.bgcolor("black")           # 设定屏幕颜色为黑色
screen.colormode(255)             # 颜色模式设为255

t = Turtle()                      # 新建海龟对象
t.bk(200)                         # 倒退200
t.width(20)                       # 笔宽为2

for colour in color_list:         # 迭代颜色表
    t.color(colour)               # 设海龟画笔和填充颜色
    t.fd(2)                       # 前进2个单位

screen.exitonclick()              # 单击屏幕关窗
