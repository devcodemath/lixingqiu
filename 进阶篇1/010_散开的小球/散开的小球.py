"""散开的小球.py
   1、请把for循环改成列表推导式
   2、下列代码中的while循环嵌套了一个for循环，把for循环去掉，实现同样的效果
   3、让每个球的颜色不一样。   
"""

from turtle import *

screen = Screen()
screen.delay(0)
screen.bgcolor("white")

t = Turtle(shape='circle')
t.penup()
t.color("magenta")

balls = [t]
for i in range(35):
    balls.append(t.clone())

for i in range(36):
    ball = balls[i]    
    ball.setheading(i*10)
 
while True:
    for ball in balls:
        ball.fd(2)
