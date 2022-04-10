"""
   飞行棋演示
"""
from sprites import *

cors = [(-200,-150),(-200,-100),(-200,-50),(-200,0),(-200,50),(-200,100),
        (-200,150),(-150,150),(-100,150),(-100,100),(-100,50),(-100,0),
        (-100,-50),(-100,-100),(-50,-100),(0,-100),(50,-100),(100,-100),
        (100,-50),(100,0),(100,50),(100,100),(100,150),(150,150),(200,150),
        (200,100),(200,50),(200,0),(200,-50),(200,-100),(200,-150)]

colors = makecolors()      # 产生颜色表

width,height = 480,360     # 定义宽高
screen = Screen()          # 新建屏幕
screen.bgcolor('black')    # 背景为黑
screen.setup(width,height) # 设定宽高

square = Sprite(shape='square',visible=False)
square.scale(2.4)
for c in cors:
    square.color('gray',random.choice(colors))
    square.goto(c)
    square.stamp()

# 在飞行棋上移动的小猫
cat = Sprite('res/cat1.png',visible=False)
cat.scale(0.5)
cat.goto(cors[0])
cat.index = 0
cat.show()

# 投射的色子
seimages = [f'sezi/{i}1.png' for i in range(1,7)]
sezi = Sprite(shape=seimages,visible=False)
sezi.scale(0.5)

clock = Clock()
running = True
while running:
    sezi.goto(-250,-190)
    sezi.dx = 8                       # 水平速度
    sezi.dy = 16                      # 垂直速度
    sezi.show()
    sezi.play('sezi/yisell_sound_1.wav')
    while sezi.xcor()<0:              # 投射色子
        sezi.move(sezi.dx,sezi.dy)
        sezi.dy -= 0.5               
        r = random.randint(1,6)
        sezi.shapeindex(r-1)
        screen.title(f'Python精灵模块飞行棋演示,本次会移动{r}次')
        clock.tick(30)
    sezi.wait(1)
    # 小猫开始移位
    for _ in range(r):
        cat.index += 1        
        cat.goto(cors[cat.index])
        # 到了最后一个坐标,则是到终点
        if cat.index == len(cors) - 1:
           running = False
           break
        cat.wait(0.2)
    cat.wait(1)
sezi.saycolor('yellow')
sezi.say('到终点了')
screen.mainloop()

        



    
