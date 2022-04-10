"""旋转雪花.py"""
from time import sleep
from turtle import Screen,Turtle  # 从海龟画图导入Screen函数和Turtle类

screen = Screen()                 # 新建屏幕
screen.setup(800,600)             # 设置屏幕宽和高
screen.delay(15)                  # 绘画延时为15
screen.bgcolor("black")           # 背景为黑色

def draw_branch(length):
    """画分支函数"""
    lg = length//2
    t.fd(lg)
    t.lt(45)
    t.fd(lg*0.8)
    t.bk(lg*0.8)
    t.rt(90)
    t.fd(lg*0.8)
    t.bk(lg*0.8)
    t.lt(45)
    t.fd(lg)
    t.bk(length)
def draw_snow(length):            # 画雪花函数    
    for i in range(8):            # 重复8次  
        draw_branch(length)
        t.rt(45)                  # 右转45度

t = Turtle()                      # 新建海龟对象
t.color("white")                  # 颜色为白色

t.begin_poly()                    # 开始记录顶点 
draw_snow(200)                    # 画雪花
t.end_poly()                      # 结束记录顶点
p = t.get_poly()                  # 得到顶点坐标元组
t.clear()                         # 清除所画图形
screen.addshape("snow",p)         # 给形状列表添加snow形状,形状列表可以由screen.getshapes()得到
t.shape("snow")                   # 设定t的形状为snow 
for  i in range(10,1,-1):         # for循环的目的是让它较慢的缩小 
    t.shapesize(i/10,i/10)
    sleep(0.1)
while True:
    t.rt(1)
    sleep(0.01)
