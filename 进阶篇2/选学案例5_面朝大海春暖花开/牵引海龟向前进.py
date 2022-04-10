"""牵引海龟向前进.py"""

from turtle import *

def followmouse(x,y):
    screen.title(str(x) + "," + str(y))
    a = t.towards(x,y)            # 朝向x,y坐标，返回角度值
    t.setheading(a)               # 设置a为海龟的方向
    if t.distance(x,y)>40:t.fd(5) # 到x,y的距离大于40就前进5

screen = Screen()
screen.delay(0)

t = Turtle(shape='turtle')        # 新建海龟对象
t.penup()                         # 抬笔
t.color("red")                    # 设定颜色为红色
t.shapesize(5,5)                  # 放大5倍
                                 
screen.onmousemove(followmouse)   # 绑定到函数
screen.mainloop()                 # 进入主循环
