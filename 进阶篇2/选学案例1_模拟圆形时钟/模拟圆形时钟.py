""" 模拟圆形时钟.py
这是一个用海龟模块制作的模拟时钟程序,海龟的方向模式有两种，一种是standard，这是默认的。
另一种是logo，这是和最老的logo计算机语言的方向模式相匹配，此模式以向上为0度，向右转为方向增加，
向左转为方向减小，所以它的90度是向右，它的-90度是向左，而180度和-180度都是向下。
这种模式刚好和挂在墙上的时钟相匹配，所以本程序中采用这种模式，用screen.mode("logo")命令设置即可。
作者:李兴球,日期:2018/12/10于杭州"""

from turtle import *
from time import *

def init_screen():
    """新建屏幕对象，注册箭头指针形状"""
    screen = Screen()
    screen.title("模拟时钟")
    screen.delay(0)
    screen.setup(700,700)
    screen.mode("logo")            # 此模式刚好和时钟转动相适配
    pointer = ((0,0),(5,0),(5,50),(10,50),(0,60),(-10,50),(-5,50),(-5,0)) # 顶点表
    screen.addshape("pointer",pointer)    # 添加大箭头各顶点到形状列表    
    return screen
    
def draw_digital():    
    """画时钟的一圈数字"""
    ziti = (None,28,"bold")
    radius = 300
    draw_turtle = Turtle(visible=False,shape='circle')
    draw_turtle.penup()
    draw_turtle.setheading(30)
    for i in range(1,13):
        draw_turtle.fd(radius)
        draw_turtle.write(str(i),align="center",font=ziti)
        draw_turtle.bk(radius)
        draw_turtle.right(30)
    draw_turtle.showturtle()

def run_hour():
    """时钟指针"""
    hour = localtime(time()).tm_hour            # 求出当前的小时数
    hour = hour % 12
    minute = localtime(time()).tm_min           # 求出当前的分钟数
    hour = hour + minute/60                     # 1小时有60分钟     
    angle =  hour * 360/12                      # 时针每刻度是30度
    angle = angle % 360     
    hour_pointer.setheading(angle)               # 设置方向     
    hour_pointer.screen.ontimer(run_hour,60000)  # 每分钟更新一次
       
def run_minute():
    """分钟指针"""
    minute = localtime(time()).tm_min           # 求出当前的分钟数  
    angle =   minute * 360/60                   # 分针每刻度是6度
    angle = angle % 360         
    minute_pointer.setheading(angle)            # 设置方向
    minute_pointer.screen.ontimer(run_minute,1000)

def run_second():
    """秒钟指针"""
    second = localtime(time()).tm_sec 
    angle =  second * 360/60 
    angle = angle % 360         
    second_pointer.setheading(angle)
    second_pointer.screen.ontimer( run_second,1000)    

if __name__ == "__main__":

    screen = init_screen()
    draw_digital()                          # 画数字

    hour_pointer = Turtle(shape='pointer')  # 生成时钟指针
    hour_pointer.shapesize(1.3,3.5)         # 缩放指针长宽
    hour_pointer.color("red")
    run_hour( )
    
    minute_pointer = Turtle(shape='pointer')# 生成分钟指针
    minute_pointer.shapesize(0.8,4.2)
    minute_pointer.color("orange")
    run_minute( )

    second_pointer = Turtle(shape='pointer')# 生成秒钟指针
    second_pointer.shapesize(0.5,4.3)
    second_pointer.color("blue")
    run_second( ) 

    screen.mainloop()


    
    
