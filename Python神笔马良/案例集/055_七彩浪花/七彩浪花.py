"""
   七彩浪花.py
"""
import turtle

cs = ['red','orange','yellow','green',
      'cyan','blue','magenta']

def draw_wave():
    """画一朵浪花"""
    angle = turtle.heading()   # 记住老的方向值
    pos = turtle.position()    # 记住老的坐标值
    turtle.pd()
    for s in range(25):
        turtle.width(s)        # 画笔越来越粗
        turtle.fd(2)           # 前进2个单位
        turtle.right(4)        # 右转4度
    turtle.pu()
    turtle.goto(pos)           # 回到原先坐标 
    turtle.setheading(angle)   # 回到原先方向

turtle.left(90)
turtle.penup()
for i in range(7):
    c = cs[i]
    turtle.color(c)
    draw_wave()
    turtle.fd(100)
    turtle.rt(360/7)

turtle.ht()                   # 隐藏海龟
turtle.done()                 # 事件循环 
