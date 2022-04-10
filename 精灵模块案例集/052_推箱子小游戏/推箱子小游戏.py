"""
   推箱子游戏.py
"""
from sprites import *

def moveobject(obj):
    """移动一个对象,如果对象前面没有墙,则移动它,否则直接返回。"""
    x,y = obj.pos()
    x = x + bug.dx  # obj的前一格的x坐标
    y = y + bug.dy  # obj的前一格的y坐标
    # 所有墙的x,y坐标
    cors = [wall.position() for wall in wall_group]
    if (x,y) in cors:return         # 说明前面有墙，直接返回
    obj.move(bug.dx,bug.dy)
    return True
   
def existbox(x,y):
    """在x,y坐标是否存在箱子"""
    for box in box_group:
        if box.distance(x,y)<1:
            return box
        
def movethebug():    
    x1 = bug.xcor() + bug.dx   # 注意此时bug并没有到达x1坐标及y1坐标
    y1 = bug.ycor() + bug.dy   # x1,y1就是bue前进方向的第一格
    box = existbox(x1,y1)      # 检测在前进方向的第一格是否有箱子
    if box:                    # 如果朝bug前一格有箱子       
        x2 = box.xcor() + bug.dx     # 这个箱子的朝bug前进方向第二格的x坐标
        y2 = box.ycor() + bug.dy     
        other = existbox(x2,y2)      # 检测(x2,y2)这个坐标是否有箱子
        if other == None:    # 如果没有，并没有墙的阻挡则向周边移动箱子
            canmove = moveobject(box)
            if canmove:bug.move(bug.dx,bug.dy)
    else:        
        moveobject(bug)
        
screen = Screen()
bug = Sprite()

box_group = Group(tag='box')
square1 = Sprite('res/blue_square.png',pos=(100,0),tag='box') # 会自动加入到'box'组
square2 = Sprite('res/blue_square.png',pos=(100,100),tag='box')
square3 = Sprite('res/blue_square.png',pos=(-100,0),tag='box')

wall_group = Group(tag='wall')
wall1 = Sprite('res/brown_square.png',pos=(100,150),tag='wall')# 会自动加入到'wall'组
wall2 = Sprite('res/brown_square.png',pos=(-100,100),tag='wall')
wall3 = Sprite('res/brown_square.png',pos=(-150,100),tag='wall')

screen.listen()
keyup = Key('Up')             # 实例化向上方向箭头
keydown = Key('Down')
keyleft = Key('Left')
keyright = Key('Right')

clock = Clock()
while True: 
    bug.dx = 0
    bug.dy = 0
    if keyup.down():          # 按了向上方向箭头
        bug.dx = 0            # 设定水平速度为0   
        bug.dy = 50           # 设定垂直速度为50 
        bug.setheading(90)    # 面向90的方向
    if keydown.down():        # 按了向下方向箭头
        bug.dx = 0
        bug.dy = -50
        bug.setheading(-90)
    if keyleft.down():
        bug.dx = -50
        bug.dy = 0
        bug.setheading(180)
    if keyright.down():
        bug.dx = 50
        bug.dy = 0
        bug.setheading(0)
    while keyup.down() or keydown.down() or keyleft.down() or keyright.down():screen.update()

    movethebug()               # 移动这只虫子 
    clock.tick(60)
    
                
