"""土耳其进行曲配音动画.py,本程序要有coloradd模块,否则无法运行."""

from turtle import *
from coloradd import addcolor
from random import randint,choice
from winsound import PlaySound,SND_ASYNC,SND_LOOP

def repeat(s,n):
    for i in range(n):
        exec(s)

code_list = []               # 定义代码字符串列表
colour = (1,0,0)           # 定义起始颜色三元组

screen = Screen()            # 新建屏幕
screen.bgcolor("gray")       # 设屏幕背景为灰色
#screen.colormode(255)        # 屏幕模式为RGB255
screen.delay(0)              # 延时为0
screen.title("土耳其进行曲配音动画")

t = Turtle()                 # 新建海龟对象

"下面的for循环形成code,并添加到code_list列表"
for i in range(1,50):
    angle = randint(1,360)
    code = "t.fd(" + str(i) + ");t.rt(" + str(angle) + ");t.dot(5)"
    code_list.append(code)

for code in code_list:
    print(code)

"下面的代码重复500次,执行代码表中的代码一定的次数."
PlaySound("土耳其进行曲.wav",SND_ASYNC|SND_LOOP)
for i in range(500):
    repeat(choice(code_list),randint(2,10))  # 随机选择一句代码,重复2到10次  
    colour = addcolor(colour,0.01)           # 颜色增加0.01
    t.pencolor(colour)                       # 重设画笔颜色
    if t.distance(0,0)>200:                  # 到原点的距离大于200就回到原点
        t.penup()
        t.home()
        t.pendown()
screen.exitonclick()

