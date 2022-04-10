"""
   旋转迷宫.py
"""
import time
import turtle

def draw_square(pos,length):
    """以pos为中心点画边长为length的正方形"""
    turtle.penup()
    turtle.bk(length/2)          # 倒回
    turtle.rt(90)                # 右转90
    turtle.bk(length/2)          # 再倒回
    turtle.left(90)              # 左转90
    turtle.pendown()             # 落笔  
    for _ in range(4):           # 到了正方形左上角
        turtle.fd(length)
        turtle.rt(90)
    turtle.penup()
    turtle.rt(90)
    turtle.fd(length/2)
    turtle.lt(90)
    turtle.fd(length/2)
    
turtle.speed(0)
turtle.tracer(0,0)              # 关闭显示刷新，设置绘画延时为0毫秒
turtle.pensize(2)
turtle.hideturtle()             # 隐藏海龟

while True:
    turtle.clear()              # 清空所画
    turtle.rt(1)
    for d in range(300,30,-30): 
        draw_square((0,0),d)    # 在当前方向画正方形
    turtle.update()             # 刷新显示  
    time.sleep(0.01)            # 等待0.01秒
