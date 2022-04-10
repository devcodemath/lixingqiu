"""请增加让猫可以移动的方法"""

from turtle import Turtle,Screen

class Cat:
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
        self.body = Turtle(shape = image)
        self.body.penup()

screen = Screen()
image1 = "cat1.gif"
screen.addshape(image1)
c1 = Cat(image1,100,100)
