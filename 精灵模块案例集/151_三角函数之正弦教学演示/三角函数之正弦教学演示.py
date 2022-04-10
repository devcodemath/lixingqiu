"""
   三角函数之正弦教学演示.py
"""
from sprites import *

ft = ('Arail',18,'normal')

s = Sprite(shape='sincab.png',pos=(0,-150))

d = Sprite(visible=False)

w = Sprite(visible=False)
w.draw_grid2(4,4,200,200)

line = Sprite(shape='line')
line.scale(2)
while 1:
    d.clear()
    mx,my = mouse_pos()
    line.heading((mx,my))
    angle = line.heading()
    x = 200 * math.cos(math.radians(angle))
    y = 200 * math.sin(math.radians(angle))
    d.goto(x,y)
    d.pendown()
    d.goto(x,0)
    d.penup()
    d.goto(x,y+5)
    d.write('C',font=ft)
    d.goto(x+5,-20)
    d.write('B',font=ft) 
    d.goto(-20,-20)
    d.write('A',font=ft)
    if mx > 0:
        if my > 0 :
            d.goto(30,0)
            d.setheading(90)
            d.pendown()
            d.circle(30,angle)
            d.penup()
        else:            
            d.goto(30,0)
            d.setheading(-90)
            d.pendown()
            d.circle(-30,360-angle)
            d.penup()            
    else:
        d.goto(-30,0)
        d.setheading(90)
        d.pendown()
        d.circle(-30,180-angle)
        d.penup()
    
    line.wait(0.1)
