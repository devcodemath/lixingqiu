""" 
   请把弹球改成多种颜色的.
   
"""

from turtle import Turtle,Screen
from random import randint
 
class Ball(Turtle):
    def __init__(self):
        Turtle.__init__(self,shape='circle')
        self.penup()
        self.color("cyan")
        self.xspeed = randint(-5,5)
        self.yspeed = randint(-5,5)
        self.screen_width = self.screen.window_width()
        self.screen_height = self.screen.window_height()

    def move(self):
        x = self.xcor() + self.xspeed
        y = self.ycor() + self.yspeed
        self.goto(x,y)
        if abs(x) > self.screen_width//2 : self.xspeed = -self.xspeed
        if abs(y) > self.screen_height//2: self.yspeed = -self.yspeed
        


if __name__ == "__main__":
    
    screen = Screen()
    screen.delay(0)
    screen.bgcolor("black")
    screen.title("模拟弹球-面向对象编程法")
     
    all_balls = [Ball() for i in range(10)]

    while True:
        for ball in all_balls:
            ball.move()
 
  
