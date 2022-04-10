""" 多彩弹球一.py。 本程序会生成一些彩色的小球,它们碰到边缘会反弹。"""
from glob import glob
from turtle import Screen,Turtle
from random import randint,choice
 
width,height = 800,600
gif_images = glob("images/*.gif")

screen = Screen()
screen.delay(0)                     # 屏幕延时为0毫秒
screen.bgcolor("black")
screen.setup(width,height)
screen.title("多彩弹球一")
[screen.addshape(image) for image in gif_images]

ball = Turtle(shape=choice(gif_images))    # 生成一个小球
ball.penup()                               # 抬笔
ball.speed(0)                              # 动作速度最快
ball.xspeed = randint(-5,5)                # 新的属性,随机x速度
ball.yspeed = randint(-5,5)                # 新的属性,随机y速度
for i in range(10):                        # 迭代i变量10次
    t =  ball.clone()                      # 复制一个小球
    t.shape(choice(gif_images))            # 设定gif图
    t.xspeed = randint(-5,5)               # 随机x速度
    t.yspeed = randint(-5,5)               # 随机y速度
    
all_balls = screen.turtles()               # 获取所有海龟对象
screen.onclick(lambda x,y :screen.bye())   # 单击屏幕关窗口
while True:
    for ball in all_balls:
        ball.setx(ball.xcor() + ball.xspeed)
        ball.sety(ball.ycor() + ball.yspeed)
        if abs(ball.xcor()) > width//2 : ball.xspeed = -ball.xspeed
        if abs(ball.ycor()) > height//2: ball.yspeed = -ball.yspeed
        
"""
问题:
1、在对边缘的碰撞检测的时候,小球会陷进去一半,这是由于在检测的时候是用小球中心点进行判断的,请对这种情况进行改进。
2、什么条件下会出现小球静止不动的现象？请解决这个问题。
3、本程序使用了嵌套的循环，能不能不使用嵌套循环实现同样的效果。
4、本程序设置了单击屏幕后会关闭窗口，但会在IDLE出现异常出错信息，
能修改为让程序正常结束而不出现这些信息吗？
"""


