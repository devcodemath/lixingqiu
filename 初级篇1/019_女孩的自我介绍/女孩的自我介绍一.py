"""女孩的自我介绍一.py,请把海龟write命令处的代码用循环控制结构实现.
"""
from turtle import *

width,height = 600,600
girl_image = "anna-1.gif"
ziti = ("楷体",18,"normal")
title = '宁彩橙的自我介绍'

screen = Screen()
screen.setup(width,height)
screen.bgcolor("black")
screen.title(title)
screen.addshape(girl_image)

t = Turtle(shape=girl_image)
t.penup()
t.goto(168,-100)

w = Turtle(shape = 'blank')
w.color("cyan")
w.penup()
w.goto(0,200)
w.write(title,align='center',font=("黑体",20,'normal'))

w.color("white")
w.goto(-220,100)

"""
   请把以下重复的代码用for循环或while循环重新实现。
   自我介绍的内容要从文件中加载进来。
   示例文件：“自我介绍.txt”

"""
w.write("你好,我叫宁彩橙。",align='left',font=ziti)
w.sety(w.ycor() - 35)
w.write("我今年12岁了。",align='left',font=ziti)
w.sety(w.ycor() - 35)
w.write("我在北星小学读六年级。",align='left',font=ziti)
w.sety(w.ycor() - 35)
w.write("过完暑假就要上初一了。",align='left',font=ziti)
w.sety(w.ycor() - 35)
w.write("我好希望上初中。",align='left',font=ziti)
w.sety(w.ycor() - 35)
w.write("到时候又能交到许多好朋友。",align='left',font=ziti)
w.sety(w.ycor() - 35)
w.write("还能学到许多新的知识。",align='left',font=ziti)
w.sety(w.ycor() - 35)
w.write("我喜欢跳舞，下象棋，编程。",align='left',font=ziti)
w.sety(w.ycor() - 35)
w.write("还喜欢游泳，看电影，爬山。",align='left',font=ziti)
w.sety(w.ycor() - 35)
w.write("今天天气真好，我要去和大自然亲密接触了。",align='left',font=ziti)
w.sety(w.ycor() - 35)

screen.exitonclick()







