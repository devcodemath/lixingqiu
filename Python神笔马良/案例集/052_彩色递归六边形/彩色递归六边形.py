"""
   彩色递归六边形.py
"""
import turtle

def draw_circle(radius,level):
    if level>0:
        turtle.color(cs[level%10])
        turtle.begin_fill()
        turtle.circle(radius,360,6)
        turtle.end_fill()
        draw_circle(radius/1.3,level-1)
       
cs = ['red','orange','yellow','green','brown',
      'cyan','blue','purple','pink','magenta']

draw_circle(100,10)

turtle.ht()             # 隐藏海龟
turtle.done()           # 事件循环
