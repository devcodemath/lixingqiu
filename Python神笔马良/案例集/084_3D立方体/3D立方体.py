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

turtle.speed(0)
turtle.delay(0)
turtle.penup()
turtle.ht()
turtle.tracer(0)
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
 
    
