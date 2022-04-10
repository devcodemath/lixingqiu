"""彩色方块世界.py"""

from random import choice,randint
from turtle import Turtle, Screen

def spawn_square(colour,screen):
    """生成小方块,colour为颜色,screen为屏幕对象"""
    screen_width = screen.window_width()  # 屏幕宽度
    screen_height = screen.window_height()# 屏幕高度
    t = Turtle(shape = 'square')          # 生成方形海龟对象
    t.color(colour)                       # 上颜色
    t.penup()                             # 抬笔
    x = randint(-screen_width//2,screen_width//2)  # 屏幕x坐标范围
    y = randint(-screen_height//2,screen_height//2)# 屏幕y坐标范围
    t.goto(x,y)                           # 定位
    return lambda c: t.color(c)           # 返回参数为c的函数，它用来设定t的颜色

if __name__ == "__main__":

    amounts = 200
    cs = 'red','orange','magenta','green','cyan'  # 颜色元组
    screen = Screen()                     # 新建屏幕对象
    screen.bgcolor("black")               # 设定屏幕背景为黑色
    screen.delay(0)                       # 延时为0
    screen.colormode(255)                 # 颜色模式为255
    screen.title("彩色方块世界")          # 设定标题
    # f是一个列表，它存储的是一些函数，这些函数有一个参数，用来设定海龟的颜色
    f = [spawn_square(choice(cs),screen) for i in range(amounts)]
    index = 0
    while True:
        r = randint(0,255)                # RGB三元组红色份量
        g = randint(0,255)                # RGB三元组绿色份量
        b = randint(0,255)                # RGB三元组蓝色份量
        f[index]((r,g,b))                 # 调用索引为index的f函数
        index = index + 1                 # 索引加1
        index = index % amounts           # 索引对总数求余

