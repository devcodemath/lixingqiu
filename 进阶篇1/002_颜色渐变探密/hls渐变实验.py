"""hls渐变实验.py"""

import colorsys

color_list = []
for i in range(0,100):
    "色相从0到99/100,颜色应该从红色过渡到接近红色"
    r,g,b = colorsys.hls_to_rgb(i/100,0.5,1)   #HLS转RGB   
    color_list.append((r,g,b))
 

from turtle import Turtle,Screen     # 导入Turtle类及Screen命令

screen = Screen()                    # 新建屏幕对象
screen.bgcolor("white")              # 设定屏幕颜色为白色
print("颜色模式",screen.colormode()) # 显示当前颜色模式

t = Turtle()                         # 新建海龟对象
t.bk(200)                            # 倒退200
t.width(20)                          # 笔宽为2

for colour in color_list:            # 迭代颜色表
    t.color(colour)                  # 设海龟画笔和填充颜色
    t.fd(2)                          # 前进2个单位

screen.exitonclick()                 # 单击屏幕关窗
