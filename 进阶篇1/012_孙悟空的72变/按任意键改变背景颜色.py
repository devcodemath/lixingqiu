"""按任意键改变背景颜色"""
from turtle import Screen
from random import randint

def set_bgcolor():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    screen.bgcolor(r,g,b)
    

screen = Screen()
screen.colormode(255)
screen.onkeypress(set_bgcolor)
screen.listen()
screen.mainloop()
