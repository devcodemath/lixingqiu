"""
   多线程绘画.py
"""
from random import random,randint
from turtle import Turtle,Screen
from threading import Thread

def randomcolor():
    """随机生成颜色"""
    r = random()
    g = random()
    b = random()
    return r,g,b
    
def run():
    """生成海龟让它移动100次"""
    t = Turtle(shape='turtle')
    t.speed(1)
    t.color(randomcolor())
    for _ in range(100):           # 重复100次
        fx = randint(-50,50)       # 生成-50到50之间的整数
        t.setheading(fx)           # 把fx设置为海龟的方向
        t.fd(randint(1,50))        # 随机移动一定的距离

screen = Screen()
screen.bgcolor('black')

# 创建十个线程并启动它们
[Thread(target=run).start() for _ in range(10)]

screen.mainloop()       # 这行代码一定要，是主线程
