"""
   下雨效果.py
   本程序定义了一个叫Line的类。它有三个属性。
   一个是pos，代表它的起始点坐标。
   一个是length，代表它的长度。
   一个是angle，表示它的前进方向。
   还有一个是rect，是一个二元组，表示所在区域范围。
"""
import math
from turtle import Turtle,Screen
from random import randint

class Line:
    def __init__(self,pos,length,angle,rect):
        """
           pos:起始坐标
           length:长度
           angle:方向
           rect:所在区域
        """
        self.pos = pos                      # 端点坐标
        self.length = length                # 线长度 
        self.angle = angle                  # 线的方向
        d = math.radians(angle)             # 转换为弧度
        self.dx = 3 * math.cos(d)           # 水平方向移动的距离
        self.dy = 3 * math.sin(d)           # 垂直方向移动的距离
        self.sw = rect[0]                   # 所在区域的宽度
        self.sh = rect[1]                   # 所在区域的高度
        
    def move(self):
        """移动线条，到了边缘就从另一端出现"""
        self.pos[0] = self.pos[0] + self.dx # 水平坐标增加
        self.pos[1] = self.pos[1] + self.dy # 垂直坐标增加
        if abs(self.pos[0]) > self.sw/2:    # 如果到了左右边缘
            self.pos[0] = -self.pos[0]
        if abs(self.pos[1]) > self.sh/2:    # 如果到了上下边缘
            self.pos[1] = -self.pos[1]
        
        
width,height = 480,360

screen = Screen()                           # 新建屏幕
screen.setup(width,height)                  # 设定屏幕宽高
screen.bgcolor('black')                     # 设定背景颜色
screen.tracer(0,0)                          # 关闭动画自动显示

render = Turtle(visible=False)              # 新建render用来画线 
render.penup()                              # 抬笔
render.speed(0)                             # 移动速度为最快
render.color('gray')                        # 颜色为灰 

lines = []                                  # 所有线条都放这个列表中
for _ in range(100):                        # 重复100次   
    x = randint(-width//2,width//2)         # 生成x坐标
    y = randint(-height//2,height//2)       # 生成y坐标
    d = randint(10,30)                      # 这个表示线的长度
    xian = Line([x,y],d,-90,(width,height)) # 生成一条线
    lines.append(xian)                      # 把xian添加到lines列表
    
while True:
    render.clear()                          # 擦掉以前画的
    # 下面是画每一条线
    for line in lines:
        render.goto(line.pos)               # 到线的端点
        render.seth(line.angle)             # 设置方向
        render.pendown()                    # 落笔
        render.fd(line.length)              # 前进
        render.penup()                      # 抬笔
    # 画完后一起刷新显示 
    screen.update()
    [line.move() for line in lines]         # 每条线进行移动
        








        
