"""
   神奇彩条动画.py
   一个用海龟画图的图章功能配合颜色渐变和动画原理做成的动画。
"""
from random import randint
from coloradd import coloradd
from turtle import Turtle,Screen
from winsound import PlaySound,SND_LOOP,SND_ASYNC

screen = Screen()
screen.setup(360,600)
screen.bgcolor('black')
screen.tracer(0,0)
screen.colormode(255)                 # 设定颜色模式为255
screen.screensize(100,100)            # 设定画布尺寸为100X100
screen.title('神奇彩条动画')

PlaySound('领略大自然的美丽神奇.wav',SND_LOOP|SND_ASYNC)

c = (255,255,0)
tom = Turtle(shape='square')
tom.penup()
tom.speed(0)

tom.color(c)
tom.shearfactor(0.5)                   # 变形因子  

toms = [tom]

for i in range(1,10):
    angle = i * 36
    t = tom.clone()                    # 克隆海龟   
    t.setheading(angle)                # 每只海龟初始方向不一样 
    toms.append(t)

# 修改这里的重复次数可以调整彩条长短
for i in range(80):
    [t.stamp() for t in toms]

while True: 
    
    [t.fd(2) for t in toms]            # 每只海龟前进2个单位
    [t.right(1) for t in toms]         # 每只海龟右转1个单位 
    [t.stamp() for t in toms]          # 每只海龟盖图章
    screen.update()
    c = coloradd(c,0.01)               # c颜色增加一点点
    [t.color(c) for t in toms]         # 设定每只海龟颜色为c
    [t.clearstamps(1) for t in toms]   # 清除每只海龟最先盖的章
    
    
    
