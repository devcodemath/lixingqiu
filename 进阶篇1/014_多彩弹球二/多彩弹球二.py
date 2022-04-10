""" 多彩弹球二.py。 本程序对上节程序进行了完善。"""
from glob import glob
from turtle import Screen,Turtle
from random import randint,choice
 
width,height = 800,600
gif_images = glob("images/*.gif")
speeds = [x for x in range(-5,5) if x!=0] # 如果x不是0则加到列表中

screen = Screen()
screen.delay(0)                           #屏幕延时为0毫秒
screen.bgcolor("white")
screen.setup(width,height)
screen.title("多彩弹球二")
[screen.addshape(image) for image in gif_images]

ball = Turtle(shape=choice(gif_images))    # 生成一个小球
ball.penup()                               # 抬笔
ball.speed(0)                              # 动作速度最快
ball.xspeed = choice(speeds)               # 随机x速度
ball.yspeed = choice(speeds)               # 随机y速度
for i in range(10):                        # 迭代i变量10次
    t =  ball.clone()                      # 复制一个小球
    t.shape(choice(gif_images))            # 设定gif图
    t.xspeed = choice(speeds)              # 随机x速度
    t.yspeed = choice(speeds)              # 随机y速度
    
all_balls = screen.turtles()               # 获取所有海龟对象
amounts = len(all_balls)                   # 小球数量
running = True
def setclose(x,y):
    global running                         # 申明为全局变量
    running = False
screen.onclick(setclose)                   # 单击屏幕关窗口
index = 0

while running:
    ball = all_balls[index]
    x = ball.xcor() + ball.xspeed          # 水平坐标增加ball.xspeed 
    y = ball.ycor() + ball.yspeed          # 垂直坐标增加ball.yspeed
    ball.goto(x,y)                         # 移到新坐标
    left = x - 45                          # 小球最左边的x坐标
    right = x + 45                         # 小球最右边的x坐标
    top = y + 45                           # 小球最上边的y坐标
    bottom = y - 45                        # 小球最下边的y坐标
    if left <= -width//2 or right >= width//2:  # 左或右超过边缘
        ball.xspeed = -ball.xspeed              # x速度取反
    if bottom <= -height//2 or top >= height//2:# 上或下超过边缘
        ball.yspeed = -ball.yspeed              # y速度取反
    index = index + 1                           # 索引号加1
    index = index % amounts                     # 索引对总数量求余
                                
screen.bye()                                    # 关闭窗口
 

