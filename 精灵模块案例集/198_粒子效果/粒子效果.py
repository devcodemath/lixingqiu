from random import randint
from sprites import *
from particle import Particle

screen = Screen()
screen.colormode(255)
screen.bgcolor('black')
screen.tracer(0,0)
bug = Sprite(visible=False)

ps = []
while True:
    bug.clear()
    if len(ps)<500:
        ps.append(Particle(0,0))
    for p in ps:
        p.move()
        bug.goto(p.x,p.y)
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        bug.dot(2,(r,g,b))
    screen.update()
