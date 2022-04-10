""" 
   让球碰到边缘后,让它反弹
"""

from turtle import *
#color_list = ['red','orange','yellow','green','cyan','blue','purple','pink','brown','magenta','gray','white']
#amounts = len(color_list)

class Ball(Turtle):
    def __init__(self,x,y,angle):
        Turtle.__init__(self,shape='circle')
        self.penup()
        self.color("cyan")
        self.setheading(angle) 


        
screen = Screen()
screen.delay(0)
screen.bgcolor("black")
 
balls = []
for i in range(10):
    balls.append(Ball(0,0,i*36))

while True:
    for ball in balls:
        ball.fd(2)

  
