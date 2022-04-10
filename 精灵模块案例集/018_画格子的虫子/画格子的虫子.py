"""
   画格子的虫子
"""
from sprites import *

width,height = 800,600
screen = Screen()
screen.setup(width,height)
screen.title("画格子的虫子")   

b = Sprite()
b.pendown()

for x in range(30):      
  b.addx(400)
  b.addx(-400)
  b.addy(10)
b.home()
for x in range(30):      
  b.addx(400)
  b.addx(-400)
  b.addy(-10)
b.home()

for x in range(30):      
  b.addx(-400)
  b.addx(400)
  b.addy(-10)
b.home()

for x in range(30):      
  b.addx(-400)
  b.addx(400)
  b.addy(10)
b.home()

for x in range(40):      
  b.addy(400)
  b.addy(-400)
  b.addx(10)
b.home()

for x in range(40):      
  b.addy(400)
  b.addy(-400)
  b.addx(-10)
b.home()

for x in range(40):      
  b.addy(-400)
  b.addy(400)
  b.addx(10)
b.home()

for x in range(40):      
  b.addy(-400)
  b.addy(400)
  b.addx(-10)
b.home()
b.penup()
b.dot(5,'red')
b.goto(100,100)
b.dot(5,'red')
b.goto(-100,100)
b.dot(5,'red')
b.goto(-100,-100)
b.dot(5,'red')
b.goto(100,-100)

b.dot(5,'blue')
b.goto(200,200)
b.dot(5,'blue')
b.goto(-200,200)
b.dot(5,'blue')
b.goto(-200,-200)
b.dot(5,'blue')
b.goto(200,-200)

def displaymouse():
    screen.title(str(mouse_pos()))
    screen.ontimer(displaymouse,100)

displaymouse()

screen.mainloop()
