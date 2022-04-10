"""
   8字图章动画.py
   这是一个简单的运用图章制作的动画。
   所盖的每个图章都会在0.5秒后自动被清除，所以有了这种效果。
"""
from sprites import *

width,height = 600,600
screen = Screen()
screen.bgcolor('white')

ball = Sprite(shape='circle',visible=False)

ball.randomcolor()      # 随机颜色
ball.goto(0,300)        # 坐标定位   
ball.show()             # 显示出来
    
clock = Clock()         # 新建时钟对象
while True:
    for x in range(12):
        ball.fd(20)
        ball.stamp(0.5) # 0.5秒后会自动清除的图章
        ball.right(15)
        clock.tick(30)
    for x in range(24):
        ball.fd(20)
        ball.stamp(0.5)
        ball.left(15)
        clock.tick(30)
    for x in range(12):
        ball.fd(20)
        ball.stamp(0.5)
        ball.right(15)
        clock.tick(30)



