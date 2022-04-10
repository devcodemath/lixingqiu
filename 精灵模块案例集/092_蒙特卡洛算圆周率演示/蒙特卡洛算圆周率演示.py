"""
   蒙特卡洛方法动画演示,本例在正方形内打点,圆周率的值为
   扇区内点数除以总共点数的积再乘以4。关于什么是蒙特卡洛，请自行百度。
"""
from sprites import *

screen = Screen()

s = Sprite()
s.draw_grid2(1,1,500,500)
s.sety(280)
ft = ('楷体',22,'normal')
ft2 = ('新宋体',16,'normal')
s.write('蒙特卡洛算圆周率演示',align='center',font=ft)
s.sety(250)
s.write('单击鼠标左键中止',align='center',font=ft2)

s.goto(250,-250)
s.left(90)
s.pendown()
s.circle(500,90)
s.hide()
s.penup()
left,bottom = -250,-250
counter = 0
r = 0
def breakdot(x,y):
    global running
    running = False
screen.onclick(breakdot)            # 单击中断循环
running = True
while running :
    s.gotorandom(-250,250,-250,250) # 到正方形区域
    counter = counter + 1           # 统计总共点数
    if s.distance(left,bottom)<500: # 距离小于500
        r = r + 1                   # 进行统计扇区点数
        s.dot(5,'red')              # 打红点以示区别
    else:
        s.dot(5,'blue')

pai = 4 * r/counter                 # 算出圆周率 
s.goto(0,-290)

s.write('圆周率为'+str(pai),align='center',font=ft)
screen.mainloop()








