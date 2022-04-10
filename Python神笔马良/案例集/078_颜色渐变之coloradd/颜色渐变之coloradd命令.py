"""
   颜色渐变之coloradd.py
   本程序需要coloradd模块支持,
   请在cmd窗口,即命令提示符下输入pip install coloradd进行安装。
   本程序演示coloradd命令,它能让RGB颜色三元组表示的'颜色增加'。
"""
from turtle import *
from coloradd import *

screen = Screen()
screen.colormode(255)        # 使用coloradd模块需要设置颜色模式为255
screen.bgcolor('black')
screen.title('颜色渐变示例之coloradd命令')

c = (255,0,0)                # 在这里代表红色，请自行学习RGB三元色知识
tom = Turtle(shape='turtle') # 新建造型为turtle的海龟对象
tom.bk(200)                  # 倒退200
tom.pensize(100)             # 画笔尺寸为100  

for _ in range(400):
    tom.color(c)
    c = coloradd(c,0.01)     # 颜色增加0.01
    tom.fd(1)
    
screen.mainloop()
