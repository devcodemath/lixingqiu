"""
   Python海龟画图3D立方体演示.py
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
    global viewfactor,xshift,yshift,zshift
    if (z+zshift) == 0 : return     
    xcor = viewfactor * (x+xshift)/(z+zshift)
    ycor = viewfactor * (y+yshift)/(z+zshift)
    turtle.goto(xcor,ycor)
    
turtle.color('blue')
turtle.pensize(2)
turtle.speed(0)
turtle.delay(0)
turtle.penup()
turtle.ht()
turtle.title('Python海龟画图3D立方体演示by李兴球')
turtle.tracer(0)
oldx = None
oldy = None
def shift(event):
    global oldx,oldy,xshift,yshift
    if oldx==None:oldx = event.x  # 第一次
    if oldy==None:oldy = event.y  # 第一次
    dx = event.x - oldx
    dy = event.y - oldy
    oldx = event.x
    oldy = event.y
    xshift += dx
    yshift -= dy

def fov(event):
    global viewfactor
    viewfactor +=  event.delta/60
    
canvas = turtle.getcanvas()
canvas.bind("<B1-Motion>",shift)
canvas.bind("<MouseWheel>",fov)

while True:
    turtle.clear()
    gotoxyz(50,50,0)
    turtle.pendown()
    gotoxyz(50,-50,0)
    gotoxyz(-50,-50,0)
    gotoxyz(-50,50,0)
    gotoxyz(50,50,0)
    turtle.penup()
    gotoxyz(50,50,50)
    turtle.pendown()
    gotoxyz(50,-50,50)
    gotoxyz(-50,-50,50)
    gotoxyz(-50,50,50)
    gotoxyz(50,50,50)
    turtle.penup()
    gotoxyz(50,50,50)
    turtle.pendown()
    gotoxyz(50,50,0)
    turtle.penup()
    gotoxyz(50,-50,50)
    turtle.pendown()
    gotoxyz(50,-50,0)    
    turtle.penup()
    gotoxyz(-50,-50,50)    
    turtle.pendown()
    gotoxyz(-50,-50,0)    
    turtle.penup()
    gotoxyz(-50,50,50)
    turtle.pendown()
    gotoxyz(-50,50,0)
    turtle.penup()
    turtle.update()
    time.sleep(0.1)
 
    
