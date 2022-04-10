"""
   画绑定盒.py
   绑定盒是一个矩形,围绕角色的最小的矩形,主要用来进行碰撞检测。
   描述绑定盒是用左上角坐标和右下角坐标。
   通过Sprite的bbox方法可以获取角色的绑定盒子。
   bbox命令有scale参数,代表矩形的缩放值。
   本程序是把这个矩形不断地画出来。
"""

from sprites import Turtle,Sprite,Screen

def draw_box(turtle,sprite):
    """turtle：海龟对象,sprite：精灵对象"""
    left,top,right,bottom = sprite.bbox(scale=0.9)    
    turtle.goto(left,top)
    turtle.pendown()
    turtle.goto(right,top)
    turtle.goto(right,bottom)
    turtle.goto(left,bottom)
    turtle.goto(left,top)

screen = Screen()
screen.tracer(0,0)         # 关闭显示刷新,设定绘画延时0毫秒
screen.title('画绑定盒')

d = Turtle(visible=False) # 新建海龟对象用来画绑定盒

bug = Sprite()            # 新建精灵
bug.left(90)
bug.shapesize(5,3)

while 1:
    d.clear()
    draw_box(d,bug)
    screen.update()
    
