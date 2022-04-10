"""请修改本程序,让在单击的时候打不同颜色,大小的圆点"""

from turtle import *

def draw(x,y):
    
    t.goto(x,y)
    t.dot(20)

screen = Screen()
screen.delay(0)

t = Turtle(shape='blank',visible=False)
t.penup()
screen.onclick(draw)    
screen.mainloop()


 
