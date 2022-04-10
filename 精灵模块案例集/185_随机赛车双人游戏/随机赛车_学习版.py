from sprites import *
from random import *

width,height = 960,720
screen = Screen()
screen.setup(width,height)
screen.bgcolor('gray')

r = Sprite('cyan.png')
cs = [r]
for _ in range(20):
    r.gotorandom()
    x = (10 + random())/30 
    y = r.clone()
    r.shapesize(x,x)
    cs.append(y)

cyan = (0,255,255)


car1 = Sprite('res/redcar.png')

leftkey = Key("Left")
rightkey = Key("Right")
upkey = Key("Up")
downkey = Key("Down")
screen.listen()
while True:
    if leftkey.down():car1.left(2)
    if rightkey.down():car1.right(2)
    if upkey.down():car1.fd(2)
    if downkey.down():car1.bk(2)    
    if car1.collidecolor(cyan,cs):print('碰到')
    screen.update()
