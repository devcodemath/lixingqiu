"""
   红太阳.py
"""
import turtle

turtle.speed(1)        # 设定移动速度为最慢
turtle.delay(20)       # 设定画笔绘画延时
turtle.color('red')    # 设定画笔和填充颜色
turtle.dot(100)        # 打直径为100的圆点

turtle.pensize(2)      # 设定画笔粗细   
for x in range(18):    # 在范围18内更新x变量的值
    turtle.penup()     # 抬笔
    turtle.fd(120)     # 前进120个单位
    turtle.pendown()   # 落笔
    turtle.fd(50)      # 前进50个单位
    turtle.penup()     # 抬笔
    turtle.bk(170)     # 前进170个单位
    turtle.rt(20)      # 右转20度
turtle.done()          # 做完
