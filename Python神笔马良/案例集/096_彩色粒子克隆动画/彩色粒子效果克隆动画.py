"""
   彩色粒子效果克隆动画.py
   本程序产生了炫丽的彩色粒子效果,亮点:如何彻底删除一个海龟对象。
   要不然程序会越来越卡！
   Delete thoroughly python turtle object,designer: lixingqiu。
"""

import colorsys
from random import random,choice
from turtle import Turtle,Screen

class Particle(Turtle):
    """继承自海龟的粒子类"""
    def __init__(self):
        """初始化方法"""
        Turtle.__init__(self,visible=False,shape='circle')
        self.penup()
        self._scale = 0.1
        self.shapesize(0.1,0.1)
        # 产生不包括0的-25到25之间的随机整数
        r = [ i for i in range(-25,26) if i != 0] 
        self.goto(choice(r),choice(r))
        # 让海龟的方向朝向原点
        self.setheading(self.towards(0,0))
        self.right(180)
        # 从颜色表中随机选择一种颜色给海龟
        self.color(choice(cs))
        # 注意下面重定义了speed属性(本来是一个speed方法)
        self.speed = self.distance(0,0)/10
        self.st()

    def move(self):
        """向前移动"""
        self.speed = self.distance(0,0)/10         
        self.fd(self.speed)
        self._scale += 0.025
        self.shapesize(self._scale,self._scale)
                    
    def kill(self):
        """自毁，完全删除自己"""
        canvas = self.screen.cv
        canvas.delete(self.drawingLineItem)     # 删除绘画线条项目
        canvas.delete(self.turtle._item)        # 删除海龟本身项目
        [canvas.delete(item) for item in self.items ]# 删除所有产生的项目
        self.screen.turtles().remove(self)      # 从海龟列表中删除自己


#  以下是产生颜色表
cs = []
for y in range(100):
    x = random()                                # 随机产生一个小数
    r,g,b = colorsys.hsv_to_rgb(x,1,1)          # 随机产生一种鲜艳的颜色
    r,g,b = int(r*255),int(g*255),int(b*255)    # 转换成RGB255模式
    cs.append((r,g,b))                          # 添加到列表

width,height = 800,600
screen = Screen()
screen.setup(width,height)                     # 设置屏幕宽高
screen.tracer(0,0)                             # 关闭自动显示
screen.colormode(255)                          # 设定颜色模式
screen.bgcolor('black')                        # 设定背景颜色

while 1:
    
    [Particle() for x in range(10)]            # 产生10个粒子
    for d in screen.turtles()[:]:              # 遍历每个粒子
        d.move()                               # 移动一个粒子  
        x = d.xcor()
        y = d.ycor()
        if abs(x)> width//2 or abs(y) > height//2: # 如果到了边缘
            d.kill()    
    screen.update()                            # 刷新显示
    am = str(len(screen.turtles()))
    screen.title('彩色粒子效果克隆动画,当前有' + am + "克隆体_by 李兴球")


