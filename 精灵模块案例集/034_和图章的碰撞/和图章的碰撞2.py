"""
   和图章的碰撞.py
   本程序测试和图章的碰撞,会在小猫的头上显示结果.
"""

from sprites import  * 

def printw(info,obj):
    """info:要显示的信息
       obj:对象
    """
    t.clear()
    x,y = mouse_pos()
    t.goto(x,y+50)
    t.write(info + str(obj))
    
screen = Screen()                     # 新建屏幕

t = Sprite(visible=False)

sp = Sprite()                         # 新建精灵
sp.stamp()                            # 盖图章  
sp.fd(100)                            # 前进100
sp.stamp()
sp.fd(100)

sp2 = Sprite(2)                       # 小猫精灵

tom = Turtle(shape='turtle')          # 新建海龟 
tom.shapesize(3,3)
tom.penup()
tom.goto(-100,100)

while 1:
    sp2.goto(mouse_pos())
    if sp2.collide(sp):printw('碰到精灵',sp)
    if sp2.collide(tom):printw('碰到海龟',tom)
    
    for p in sp.stampItems:  #  获取sp盖的图章们的编号
        if sp2.collide(p):printw('碰到图章:',p)
