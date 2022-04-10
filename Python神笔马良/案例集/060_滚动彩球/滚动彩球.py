"""
  滚动彩珠.py
 
"""
import turtle
import random
import time

cs = ['red','orange','yellow','green','cyan']

turtle.tracer(0,0)               # 关闭显示刷新与设定绘画延时为0毫秒
turtle.bgcolor('black')
turtle.hideturtle()
turtle.penup()

def draw_pattern():
    global index
    for i in range(40):
        turtle.color(cs[index])  # 把索引为index的颜色设为海龟的颜色
        turtle.fd(100)           # 前进100个单位
        turtle.dot(10)           # 打彩色圆点
        turtle.bk(100)           # 倒退100个单位
        turtle.lt(9)             # 左转9度 
        index += 1               # index增加1
        index = index % 5        # index对5求余 

index = 0
while True:
    turtle.clear()               # 清除所有画的图形
    draw_pattern()               # 重新画图案
    turtle.update()              # 更新显示
    time.sleep(0.1)
    # 下面是轮换颜色必需的
    index = index + 1
    index = index % 5
    
