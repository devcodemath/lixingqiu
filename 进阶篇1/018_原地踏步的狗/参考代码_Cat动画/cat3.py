"""小猫边走边换造型的类"""

from turtle import Turtle,Screen

class Cat:
    def __init__(self,images,x,y):
        self.images = images
        self.index = 0
        self.x = x
        self.y = y
        self.body = Turtle(shape = images[0])
        self.body.penup()
    def move(self,distance):
        self.body.fd(distance)
        self.next_costume()
    def next_costume(self):
        self.index = 1 - self.index
        self.body.shape(self.images[self.index])

screen = Screen()
images = "cat1.gif","cat2.gif"
[screen.addshape(image) for image in images]
c1 = Cat(images,100,100)

for i in range(100):
    c1.move(1)
