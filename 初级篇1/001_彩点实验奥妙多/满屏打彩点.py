"""满屏打彩点.py 本程序会在屏幕上打满彩色小圆点。"""

from turtle import *     # 从海龟模块导入所有命令，有Turtle,Screen等
from random import *     # 从随机模块导入所有命令，有choice,randint等

width ,height = 600,600  # 定义屏幕宽高
color_list = ['red','orange','yellow','green','cyan','blue','purple'] # 颜色表

screen = Screen()               # 新建屏幕
screen.setup(width,height)      # 设置屏幕宽高
screen.bgcolor("black")         # 背景黑色
screen.delay(0)                 # 绘画延时为0
screen.title("满屏打彩点")    # 显示屏幕所在的窗口标题

t = Turtle()                    # 新建海龟对象
t.pencolor("white")             # 画笔颜色为白色
t.hideturtle()                  # 隐藏海龟
t.penup()                       # 抬笔

while True:                          # 当为真的时候
    x = randint(-width/2,width/2)    # x的值是最左边x和最右边x之间
    y = randint(-height/2,height/2)  # y的值是最下边y和最上边y之间 
    colour = choice(color_list)  # 从颜色表随机选择一种颜色
    t.pencolor(colour)           # 作为画笔颜色
    t.goto(x,y)                  # 定位到x,y
    t.dot(10)                    # 打点

