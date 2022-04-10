"""
   颜色渐变之colorset.py
   本程序需要coloradd模块支持,
   请在cmd窗口,即命令提示符下输入pip install coloradd进行安装。
   本程序演示colorset命令,它能把一个整数转换成一个RGB颜色三元组。
   如把0转换成(255,0,0)，这样能代表红色。
"""
from turtle import *
from coloradd import *

screen = Screen()
screen.colormode(255)        # 使用coloradd模块需要设置颜色模式为255
screen.bgcolor('black')
screen.title('颜色渐变示例之colorset命令')

tom = Turtle(shape='turtle') # 新建造型为turtle的海龟对象
tom.bk(200)                  # 倒退200
tom.pensize(100)             # 画笔尺寸为100  

for x in range(400):   
    c = colorset(x)          # 把x转换成RGB颜色三元组
    print(c)
    tom.color(c)
    tom.fd(1)
    
screen.mainloop()
