"""
  纯画笔弹球动画.py
  读者可以在此基础上把它修改成一个拦球游戏。
  步骤为，建立一个Rect类，即矩形类。
  然后采用按键检测，当按了键时重画矩形。
  当然碰撞检测采用矩形碰撞即可。
"""
import time
import turtle
from random import *
from ball import Ball

def randcolor():
    """产生随机颜色"""
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b   
        
def renderball(obj):
    """渲染球"""
    turtle.goto(obj.pos())
    turtle.dot(2 * obj.radius,obj.color)
    
sw = turtle.window_width()                # 获取窗口宽度
sh = turtle.window_height()               # 获取窗口高度
turtle.bgcolor('black')                   # 窗口背景颜色
turtle.colormode(255)                     # 颜色模式为255
turtle.tracer(0,0)                        # 关闭动画显示
turtle.speed(0)                           # 动作速度为最快
turtle.penup()                            # 抬起画笔来
turtle.ht()                               # 隐藏海龟

# 实例化100个球
balls = [Ball(0,0,4,randcolor(),sw,sh) for _ in range(100)]

while True:
    turtle.clear()
    # 更新每个球的坐标
    for ball in balls:
        ball.move()
        ball.bounce_on_edge()
        
    # 重画所有的球
    [renderball(ball) for ball in balls]

    # 渲染所有的对象
    turtle.update()
    time.sleep(0.001)
