""" 海龟入篮"""

from turtle import *
from random import randint

篮子 =[]
for i in range(10):
    海龟 = Turtle(shape="turtle")
    海龟.pencolor("blue")
    海龟.fillcolor("blue")
    篮子.append(海龟)

print(篮子)

fx = 0
for t in 篮子:
    t.setheading(fx)
    t.fd(100)
    fx = fx + 36

length = len(篮子)
for i in range(length):
    篮子.pop()

print(篮子)
    

 
