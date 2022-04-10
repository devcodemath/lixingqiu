"""
   给Sprite类加方法(迷宫碰撞)
   本程序给Sprite类增加了一个叫spiral的方法,
   这样,所有生成的角色都有了这样一个方法,
   当然,用同样的道理,可以重定义现有的Sprite类的方法。
   本程序还演示了如何使用find_overlapping方法。
   注意在下面的程序中是如何使用items列表的。
"""
from sprites import *

def spiral(self,n):
    """画螺旋图形"""
    for x in range(n):
        self.fd(x*30)
        self.rt(90)
        
Sprite.spiral = spiral      # 类的spiral方法指向spiral

screen = Screen()           # 新建屏幕
bug = Sprite()              # 新建虫子角色
bug.color('blue')           # 虫子的画笔颜色
bug.pensize(2)              # 画笔粗细
bug.pendown()               # 落笔
bug.spiral(20)              # 画"迷宫"图形
bug.penup()                 # 抬笔   
maze = bug.items[-1]        # 取图形的项目编号
print(maze)
bug.goto(0,30)              # 到坐标(0,30)

leftkey = Key("Left")       # 新建左方向箭头实例
rightkey = Key("Right")     # 新建右方向箭头实例
upkey = Key("Up")           # 新建上方向箭头实例
downkey = Key("Down")       # 新建下方向箭头实例
screen.listen()             # 监听屏幕按键

clock = Clock()             # 新建时钟对象 
while True:
    if leftkey.down():      # 如果按了左方向箭头
        bug.setheading(180) # 面向左的方向 
        bug.addx(-5)        # x坐标减小
        if bug.find_overlapping(maze):bug.addx(5)
    if rightkey.down():
        bug.setheading(0)
        bug.addx(5)
        if bug.find_overlapping(maze):bug.addx(-5)
    if upkey.down():
        bug.setheading(90)
        bug.addy(5)
        if bug.find_overlapping(maze):bug.addy(-5)
    if downkey.down():
        bug.setheading(-90)
        bug.addy(-5)
        if bug.find_overlapping(maze):bug.addy(5)
    screen.update()
    clock.tick(30)           # 设定fps为30
    
