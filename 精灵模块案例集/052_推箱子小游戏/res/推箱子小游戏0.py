"""
   推箱子游戏1.py
"""
from sprites import *

def addx(obj,dx):
    """增加x"""
    x,y = obj.pos()
    x = x + dx
    for wall in wall_group:
        if wall.distance(x,y)<1:
            return
    obj.addx(dx)
    return True

def addy(obj,dy):
    """增加y"""
    x,y = obj.pos()
    y = y + dy
    for wall in wall_group:
        if wall.distance(x,y)<1:
            return
    obj.addy(dy)
    return True
    
    
def existbox(x,y):    
    for box in box_group:
        if box.distance(x,y)<1:
            return box
        
def existotherbox(self,x,y):
    """查找x,y坐标是否有箱子"""
    for other in box_group:
        if self == other:continue
        if other.distance(x,y)<1:
            return other
screen = Screen()

bug = Sprite()

box_group = Group(tag='box')
square1 = Sprite('res/blue_square.png',pos=(100,0),tag='box')
square2 = Sprite('res/blue_square.png',pos=(100,100),tag='box')
square3 = Sprite('res/blue_square.png',pos=(-100,0),tag='box')

wall_group = Group(tag='wall')
wall1 = Sprite('res/brown_square.png',pos=(100,150),tag='wall')
wall2 = Sprite('res/brown_square.png',pos=(-100,100),tag='wall')
wall3 = Sprite('res/brown_square.png',pos=(-150,100),tag='wall')

def moveleft():
    bug.setheading(180)
    x = bug.xcor() - 50
    y = bug.ycor()
    box = existbox(x,y)      # 检测在左边是否有箱子
    if box:
        print(box)
        x1 = box.xcor()-50
        y1 = box.ycor()      # 下面检测此箱子左边是否还有箱子
        other = existotherbox(box,x1,y1)
        if other == None:    # 如果没有，并没有墙的阻挡则向左移动箱子
            moved = addx(box,-50)
            if moved:addx(bug,-50)
    else:
        addx(bug,- 50)
        
def moveright():
    bug.setheading(0)
    x = bug.xcor() + 50
    y = bug.ycor()
    box = existbox(x,y)
    if box:
        print(box)
        x1 = box.xcor()+50
        y1 = box.ycor()    
        other = existotherbox(box,x1,y1)
        if other == None:
            moved = addx(box,50)
            if moved:addx(bug,50)
    else:
        addx(bug,50)
    
def moveup():
    bug.setheading(90)
    x = bug.xcor()
    y = bug.ycor()+50
    box = existbox(x,y)
    if box:
        print(box)
        x1 = box.xcor() 
        y1 = box.ycor() + 50  
        other = existotherbox(box,x1,y1)
        if other == None:
            moved = addy(box,50)
            if moved:addy(bug,50)
    else:
        addy(bug,50)
        
def movedown():
    bug.setheading(-90)
    x = bug.xcor()
    y = bug.ycor()-50
    box = existbox(x,y)
    if box:
        print(box)
        x1 = box.xcor() 
        y1 = box.ycor() - 50  
        other = existotherbox(box,x1,y1)
        if other == None:
            moved = addy(box,-50)
            if moved:addy(bug,-50)
    else:
        addy(bug,-50)        

screen.onkey(moveup,"Up")
screen.onkey(movedown,"Down")
screen.onkey(moveleft,"Left")
screen.onkey(moveright,"Right")
screen.listen()
screen.mainloop()
