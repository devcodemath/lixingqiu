""" 
   这是用屏幕的定时器功能实现的弹球移动,速度比较慢,请改成不用定时器功能实现移动.
   
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
        self.move()
    def move(self):
        x = self.xcor() + self.xspeed
        y = self.ycor() + self.yspeed
        self.goto(x,y)
        if abs(x) > self.screen_width//2 : self.xspeed = -self.xspeed
        if abs(y) > self.screen_height//2: self.yspeed = -self.yspeed
        
        self.screen.ontimer(self.move,10)

if __name__ == "__main__":
    
    screen = Screen()
    screen.delay(0)
    screen.bgcolor("black")
    screen.title("模拟弹球-面向对象编程法")     

    [Ball() for i in range(10)]
        
    screen.exitonclick()
  
