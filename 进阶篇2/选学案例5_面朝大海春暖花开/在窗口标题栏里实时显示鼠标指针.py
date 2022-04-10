"""在窗口标题栏里实时显示鼠标指针.py"""

from turtle import *

def display(x,y):
    screen.title(str(x) + "," + str(y))

screen = Screen()
screen.onmousemove(display)
screen.delay(0)
screen.exitonclick()

 
