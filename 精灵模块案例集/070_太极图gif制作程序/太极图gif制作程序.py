"""
   太极图gif制作演示程序,本程序负责生成一系列png图
"""
from sprites import *

def draw_circle(tom,x,y,radius,degrees):
    """
       tom：精灵对象
       x,y：圆的中心点
       radius：半径
       degrees: 度数
    """
    global counter,frames
    tom.goto(x,y)
    tom.pendown()
    for _ in range(degrees*100):
        tom.fd(radius)
        tom.bk(radius)
        tom.rt(0.01)
        counter += 1
        if counter % 100 == 0 :
            screen.update()
            screen.save(f'res/{frames}.png')
            frames += 1            
    tom.penup()
    

frames = 0
counter = 0
screen = Screen()
screen.setup(300,300)
screen.bgcolor('gray')
screen.tracer(0,0)
s = Sprite(visible=False)
s.pensize(1)

s.setheading(90)
draw_circle(s,0,0,100,180)
s.color('white')
draw_circle(s,0,0,100,180)
draw_circle(s,0,50,50,180)

s.color('black')
draw_circle(s,0,-50,50,180)
s.color('white')
draw_circle(s,0,-50,20,360)

s.color('black')
draw_circle(s,0,50,20,360)


