"""可移动的字.py ,主要讲述基本的动画原理.
本程序让一串汉字从左到右移动,修改一下,让它从下到上移动。"""

from time import sleep
from turtle import Screen,Turtle

info = "风火轮少儿编程"
ziti = ("黑体",32,"normal")

screen = Screen()
screen.bgcolor("black")
screen.delay(0)

t = Turtle(visible=False)
t.penup()
t.bk(150)
t.color("cyan")

for  i in range(200):
    t.clear()                 # 清除
    t.write(info,font=ziti)   # 在新的位置上重写
    screen.update()           # 刷新
    sleep(0.01)               # 延时0.01秒,目的是显示0.01秒左右
    t.fd(1)                   # 移动,准备在新的位置上重写

screen.exitonclick()          # 单击屏幕关闭窗口
