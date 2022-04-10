"""
   地图破坏者(打方块),
   这个程序演示的是如何把游戏中的地图进行破坏,
   这些方块都是图章,它们碰到子弹会消失。
   如果把箭头换成坦克，操作坦克移动，加上敌人坦克，
   那么就可以变成坦克大战游戏了。
"""
from sprites import *

# 新建50X50像素的图形，用来代表砖块
img = Image.new("RGBA",(50,50),color='brown')
img.save('square.png')

screen = Screen()                 # 新建屏幕
screen.title('地图破坏者')

square = Sprite('square.png')     # 新建棕色方块
square.goto(-300,300)
for _ in range(4):                # 迭代4次
    for x in range(10):           # 在范围10迭代x
        square.stamp()            # 盖图章
        square.fd(60)             # 前进60个单位 
    square.right(90)              # 向右转90度

square.goto(-180,180)
for _ in range(4):                # 迭代4次
    for x in range(6):            # 在范围6迭代x
        square.stamp()            # 盖图章
        square.fd(60)             # 前进60个单位 
    square.right(90)              # 向右转90度
    
bricks = square.stampItems        # 砖块们

square.home()                     # 到原点
square.shape('pointer')           # 变形为指针 

# 此角色作为子弹
circle = Sprite('circle',visible=False)

leftkey = Mouse()                 # 鼠标左键
clock = Clock()                   # 时钟对象
shoot = False                     # 控制发射的逻辑变量
while 1:
    square.heading(mouse_pos())   # 朝向鼠标指针
    if leftkey.down() and shoot==False:
        shoot = True
        circle.heading(mouse_pos())
        circle.show()
    if circle.isvisible():
        circle.fd(15)
    if circle.collide_edge():
        shoot = False
        circle.hide()
        circle.home()
    for brick in bricks[:]:
        if square.stampcollide(brick,circle):
            shoot = False
            square.clearstamp(brick)
            circle.hide()
            circle.home()
        
    screen.update()
    clock.tick(60)
