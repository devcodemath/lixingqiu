"""面朝大海春暖花开.py，本程序运行后海龟会自动朝向鼠标指针的方向。
需要有修改后的turtle.py版本才能有这种效果。"""

import glob
from turtle import *

def dynamic_bg():
    global index
    screen.bgpic(bg[index])      # 设定屏幕背景
    index += 1                   # 背景索引加1
    index = index % bgamounts    # 索引对数量取余
    screen.ontimer(dynamic_bg,100)# 100毫秒后再次运行
    
def facemouse(x,y):
    """面朝鼠标指针的函数"""
    a = t.towards(x,y)            # 朝向x,y坐标，返回角度值
    t.setheading(a)
    s = TITLE + ":" + str(x) + "," + str(y) + "," + str(round(a))
    screen.title(s)    
    t.setheading(a)               # 设定海龟的方向

TITLE = "面朝大海春暖花开"        # 设定标题
index = 0                         # 背景索引号    
bg = glob.glob("spring/*.png")    # 所有背景图
bgamounts = len(bg)               # 背景数量

screen = Screen()                 # 新建屏幕对象
screen.delay(0)                   # 设定屏幕延时
screen.setup(500,300)             # 设定屏幕大小
screen.bgcolor("black")           # 设定屏幕背景
screen.title(TITLE)               # 设定屏幕所在窗口的标题

t = Turtle(shape='turtle')        # 新建海龟对象
t.penup()                         # 抬起笔来
t.goto(-100,-100)                 # 定位海龟坐标
t.color("darkgreen")              # 设定颜色为深绿色
t.shapesize(2,2)                  # 放大2倍

try:
  screen.onmousemove(facemouse)   # 绑定到函数
except:
  pass
dynamic_bg()                      # 动态背景
screen.mainloop()                 # 进入主循环
