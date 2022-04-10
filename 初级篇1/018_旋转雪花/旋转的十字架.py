"""画个十字架旋转起来"""

from turtle import *
screen = Screen()

t = Turtle()

t.begin_poly()
for i in range(4):
    t.fd(100)
    t.bk(100)
    t.rt(90)
t.end_poly()
p = t.get_poly()
print(p)
screen.addshape("cross",p)

t.shape("cross")
t.clear() 

while True: t.right(10)
