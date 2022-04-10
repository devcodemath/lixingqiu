"""请增加让猫可以一边移动一边换造型的方法"""

from turtle import Turtle,Screen

class Cat:
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
        self.body = Turtle(shape = image)
        self.body.penup()
    def move(self,distance):
        self.body.fd(distance)

screen = Screen()
image1 = "cat1.gif"
screen.addshape(image1)
c1 = Cat(image1,100,100)

for i in range(100):
    c1.move(1)
