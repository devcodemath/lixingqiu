"""
   甩曲彩点动图.py
"""
import time
import turtle

cs = ['red','orange','yellow','green',
      'cyan','gold','white','blue','purple',
      'pink','magenta','brown','gray','lime']

turtle.ht()
turtle.speed(0)
turtle.tracer(0,0)                 # 关闭实时显示
turtle.bgcolor('black')            # 设定背景颜色

def draw_pattern():
    for c in cs:
        turtle.color(c)
        turtle.circle(50,130)     # 画圆，半径50，度数130
        turtle.dot(10)            # 打直径为10的彩色点 
        turtle.circle(50,-130)        
        turtle.rt(360/len(cs))

while True:
    turtle.clear()                 # 清除所画图形
    turtle.rt(2)                   # 海龟右转2度
    draw_pattern()                 # 画图案      
    turtle.update()                # 刷新显示
    time.sleep(0.1)                # 等待0.1秒 
