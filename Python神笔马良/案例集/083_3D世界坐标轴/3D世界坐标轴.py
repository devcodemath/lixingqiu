"""
   3D世界坐标轴.py
   3D世界的每一个点，最终都是在屏幕显示出来，而屏幕是2D的。
   所以这个3D点就需要转换成2D坐标点。
"""
__author__ = '李兴球'
__blog__ = 'www.lixingqiu.com'

import turtle
import time

viewfactor = 150
xshift = 0
yshift = 0
zshift = 50
def gotoxyz(x,y,z):
    """转换三维坐标到二维坐标"""
    global viewfactor,xshift,yshift,zshift
    if (z+zshift) == 0 : return     
    xcor = viewfactor * (x+xshift)/(z+zshift)
    ycor = viewfactor * (y+yshift)/(z+zshift)
    turtle.goto(xcor,ycor)
    
turtle.pensize(4)
turtle.speed(0)
turtle.delay(0)
turtle.penup()
turtle.ht()
turtle.title('3D世界坐标轴by李兴球')
turtle.tracer(0)
oldx = None
oldy = None
def shift(event):
    global oldx,oldy,xshift,yshift
    if oldx==None:oldx = event.x  # 第一次
    if oldy==None:oldy = event.y  # 第一次
    dx = event.x - oldx           # 鼠标指针水平偏移量
    dy = event.y - oldy           # 鼠标指针垂直偏移量
    oldx = event.x
    oldy = event.y
    xshift += dx
    yshift -= dy

def fov(event):
    global viewfactor
    viewfactor +=  event.delta/60
    
canvas = turtle.getcanvas()
canvas.bind("<B1-Motion>",shift) # 绑定左键单击移动事件到shift
canvas.bind("<MouseWheel>",fov)  # 绑定滚轮事件到fov函数

turtle.bgcolor('black')
while True:
    turtle.clear()
    gotoxyz(0,0,0)              # 到圆点
    turtle.pendown()
    turtle.color('red')
    gotoxyz(300,0,0)            # x轴
    turtle.penup()

    gotoxyz(0,0,0)              # 到圆点
    turtle.pendown()
    turtle.color('blue')
    gotoxyz(0,300,0)            # y轴
    turtle.penup()
    
    gotoxyz(0,0,0)              # 到圆点
    turtle.pendown()
    turtle.color('yellow')
    gotoxyz(0,0,300)            # z轴
    turtle.penup()    
    
    turtle.update()
    time.sleep(0.1)
 
    
