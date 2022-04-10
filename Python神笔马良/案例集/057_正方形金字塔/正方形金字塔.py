"""
   正方形金字塔.py
"""
import turtle

def draw_square(length):
    for _ in range(4):
        turtle.fd(length)
        turtle.rt(90)
        
levels = 10                       # 层数 
length = 20                       # 正方形的边长

turtle.speed(0)                   # 移动速度为最快
turtle.delay(0)                   # 绘画延时为0毫秒
turtle.width(2)                   # 画笔宽度为2
for c in range(levels,0,-1):
    for _ in range(c):
        draw_square(length)
        turtle.fd(length)
    if c == 1:break
    turtle.bk(length*c)           # 回到这行的起点
    turtle.fd(length/2)           # 前进边长的一半 
    turtle.left(90)               # 左转90度(变成向上了)
    turtle.fd(length)             # 前进length
    turtle.right(90)

turtle.ht()                       # 隐藏海龟
turtle.done()                     # 事件循环
    
    
