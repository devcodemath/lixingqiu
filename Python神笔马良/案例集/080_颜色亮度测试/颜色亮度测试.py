"""
   颜色亮度测试.py
   本程序需要coloradd模块支持,
   请在cmd窗口,即命令提示符下输入pip install coloradd进行安装。
   本程序演示brightset命令,它能设置一种颜色的亮度。
   brightset第一个参数为颜色三元组，第二个参数为从0到1的小数。
   第二个参数值越大，颜色的亮度越高。
"""
from turtle import *
from coloradd import *

screen = Screen()
screen.colormode(255)        # 使用coloradd模块需要设置颜色模式为255
screen.bgcolor('black')
screen.title('亮度渐变示例之brightset命令')

c = (255,0,0)                # 表示RGB红色三元组
tom = Turtle(shape='turtle') # 新建造型为turtle的海龟对象
tom.bk(200)                  # 倒退200
tom.pensize(100)             # 画笔尺寸为100  

for x in range(401):
      # 把表示为颜色的c元组的亮度增加，返回三元组为ys，
      # 注意不要返回为c，这样就把c给变了。
    ys = lightset(c,x/400)
    print(ys)
    tom.color(ys)
    tom.fd(1)
    
screen.mainloop()
