"""
   老鼠找花,本例中老鼠会自动找到花朵,然后把它背到圆圈里。
"""
from sprites import *

flower = Sprite('res/flower.png',pos=(-100,100))
flower.scale(0.6)
flower.follow = False            # 自定义逻辑属性,表示是否跟随
flower.end = False               # 自定义逻辑属性,表示是否放下

mouse = Sprite('res/rat1.png')   # 新建老鼠
mouse.setheading(random.randint(1,360))

radius = 100
x0,y0 = 250,100
bug = Sprite(pos=(x0,y0))        # 画圆圈的虫子
bug.pendown()
bug.fd(radius)
bug.left(90)
bug.circle(radius)
bug.right(90)
bug.bk(radius)

clock = Clock()
while True:
    mouse.fd(10)
    if random.randint(1,1000) == 1 : mouse.right(10)
    if flower.follow : flower.goto(mouse.pos())

    # 以下满足两个条件，就把把花放下
    if mouse.distance(bug.pos()) < radius/3 and flower.follow:
        flower.follow = False
        flower.end = True
    # 以下满足三个条件，老鼠就会朝向花果，
    if mouse.distance(flower.pos()) < 50 and \
       flower.follow == False and flower.end == False:
        if mouse.distance(flower.pos()) > 10:
           mouse.heading(flower)
        else:
            # 距离小于或等于10了，让花朵跟随着老鼠动，老鼠朝向圆心
            flower.follow =True
            mouse.heading((x0,y0))
            
    mouse.bounce_on_edge()
    clock.tick(30)
