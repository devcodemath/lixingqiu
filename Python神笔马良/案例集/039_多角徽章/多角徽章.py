"""
   多角徽章.py
   本程序需要coloradd模块支持,安装方法为在cmd管理员窗口下输入:
   pip install coloradd
   进行安装，安装好后在IDLE就可以导入coloradd系列命令了。
   
"""
import turtle
from coloradd import coloradd

c = (0,0,255)
turtle.colormode(255)           # 设定颜色模式为255
turtle.bgcolor('black')         # 设定背景色为黑
turtle.delay(0)                 # 设定绘画延时为0毫秒          
turtle.penup()                  # 抬笔
for _ in range(20):
    turtle.pendown()
    for i in range(100):        # 在范围100内更新i的值
        turtle.pensize(100-i)   # 设定画笔粗细
        c = coloradd(c,0.01)    # 把c“增加”
        turtle.color(c)         # 把c设为海龟画笔颜色
        turtle.fd(1)            # 前进1个单位
    turtle.penup()              # 抬笔 
    turtle.bk(100)              # 倒退100个单位 
    turtle.right(18)            # 右转18度

turtle.done()
