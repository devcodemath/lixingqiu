"""
   和图章的碰撞.py
"""

from sprites import  * 

screen = Screen()                     # 新建屏幕

bug = Sprite()                         # 新建精灵,默认是bug
bug.stamp()                            # 盖图章  
bug.fd(100)                            # 前进100
bug.stamp()
bug.fd(100)

cat = Sprite(2)                       # 小猫角色

turtle = Turtle(shape='turtle')       # 新建海龟 
turtle.shapesize(3,3)
turtle.penup()
turtle.goto(-100,100)

while 1:
    cat.goto(mouse_pos())
    if cat.collide(bug):print('碰到精灵',bug)
    if cat.collide(turtle):print('碰到海龟',turtle)
    
    for tz in bug.stampItems:       #  获取bug盖的图章们的编号
        if cat.collide(tz):print('碰到图章:',tz)
