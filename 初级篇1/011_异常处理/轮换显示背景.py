"""本程序的if语句也可以不要,请修改程序去掉if实现同样的功能,
并在适合的位置加上try...except的容错处理"""

from turtle import *
from time import sleep
screen = Screen()
screen.setup(480,360)
screen.title("轮换显示背景")
images=['desert.gif', 'flowers.gif', 'red.gif', 'woods.gif']
index = 0
while True:
    screen.bgpic(images[index])
    screen.update()
    index = index + 1
    if index == len(images): index = 0    
    sleep(0.5)
print("这句代码永远不会运行。")
