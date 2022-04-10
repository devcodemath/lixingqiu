"""
   轮子走了.py
"""
import time
import turtle 

def draw_polygon(number,length):
    """画正多边形
       number,边数
       length:边长
    """
    for _ in range(number):
        turtle.fd(length)
        turtle.left(360/number)

n = 6                              # 边数
d = 50                             # 边长
turtle.ht()
turtle.delay(0)
turtle.speed(0)
turtle.penup()
turtle.width(2)
turtle.bk(200)                      # 倒退200
turtle.pendown()                    # 落笔
for _ in range(30):
    turtle.clear()
    draw_polygon(n,d)               # 画正多边形
    turtle.fd(d)                    # 前进d个单位
    time.sleep(0.01)
    turtle.left(360/n)              # 左转360/n度
    
    # 下面是不断地擦除，右转1度，重画，就有了动画效果
    for _ in range(int(360/n)):
        turtle.clear()              # 清除所画
        turtle.right(1)             # 右转1度
        draw_polygon(n,d)           # 画正多边形
        time.sleep(0.01)            # 等待0.01秒
turtle.done()        

