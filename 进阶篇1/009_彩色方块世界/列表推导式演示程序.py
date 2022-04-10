"""
列表解析式是将一个列表（实际上适用于任何可迭代对象）转换成另一个列表的语法糖(语法技巧)。


"""
import time
from turtle import *

width,height = 480,360
"把下面这句改成列表推导式"
images = ["0.gif","1.gif","2.gif","3.gif","4.gif","5.gif","6.gif","7.gif","8.gif","9.gif","10.gif","11.gif","12.gif","13.gif","14.gif"]

screen = Screen()
screen.setup(width,height)
"把下面的for循环改成列表解析式"
for i in range(len(images)):
    screen.addshape("images/" + images[i])

t = Turtle(shape ='blank')

index = 0
while True:
    t.shape("images/" + images[index])
    time.sleep(1)
    index = index + 1
    index = index % len(images)

