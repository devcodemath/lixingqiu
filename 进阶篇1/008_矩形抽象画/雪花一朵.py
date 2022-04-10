from turtle import *
s = Screen()
s.delay(0)

t = Turtle(visible=False)
t.pensize(3)

def draw_square(g,bc):
    """g代表海龟，bc代表边长"""
    for i in range(8):       
       g.fd(bc)
       if bc > 10:draw_square(g,bc/4)
       g.bk(bc)
       g.right(45)
draw_square(t,100)
    
