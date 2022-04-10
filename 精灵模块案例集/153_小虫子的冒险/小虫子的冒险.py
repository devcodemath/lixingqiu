"""
   小虫子的冒险.py
   这是一个迷宫类型的小游戏。
   用上下左右键操作方向箭头指挥虫子进入小方块即成功。
   虫子是不能越穿“墙壁”的，当然也不能碰到左右或上下移动蓝色圆点。
"""
from sprites import *              # 从精灵模块导入所有命令

screen = Screen()                  # 新建屏幕对象
screen.setup(480,360)              # 设置屏幕宽高
screen.title('小虫子的冒险')       # 设定标题

square = Sprite(shape='square')    # 新建方块
square.color('blue','')
square.goto(175,45)
square.scale(2)

# 下面的代码是画迷宫地图
bug = Sprite(visible=True)         # 新建虫子角色
bug.scale(0.5)
bug.pensize(4)
bug.goto(-220,120)
bug.pendown()
bug.fd(100)
bug.right(90)
bug.fd(150)
bug.left(90)
bug.fd(50)
bug.left(90)
bug.fd(200)
bug.right(90)
bug.fd(220)
bug.right(90)
bug.fd(100)
bug.left(90)
bug.fd(50)
bug.right(90)
bug.fd(50)
bug.right(90)
bug.fd(50)
bug.left(90)
bug.fd(150)
bug.right(90)
bug.fd(370)
bug.right(90)
bug.fd(250)
line = bug.items[0]        # 在没抬笔之前获取所画线条的编号
bug.penup()
bug.goto(-170,10)                  # 定位到初始坐标 

dot1 = Sprite(shape='circle')      # 新建角色叫圆点1
dot1.scale(0.5)
dot1.color('blue')

dot2 = Sprite(shape='circle',pos=(0,-50))
dot2.scale(0.5)
dot2.color('blue')
dot2.setheading(90)

dot3 = Sprite(shape='circle',pos=(0,-100))
dot3.scale(0.5)
dot3.color('blue')

dot4 = Sprite(shape='circle',pos=(100,-100))
dot4.scale(0.5)
dot4.color('blue')
dot4.setheading(90)

dots = [dot1,dot2,dot3,dot4]
# 每个点的项目编号存在dotsitems列表中
dotsitems = [dot1.turtle._item,dot2.turtle._item,
             dot3.turtle._item,dot4.turtle._item]

leftkey = Key('Left')                     # 新建左方向箭头
rightkey = Key('Right')                   # 新建右方向箭头
upkey = Key('Up')                         # 新建上方向箭头
downkey = Key('Down')                     # 新建下方向箭头
screen.listen()                           # 侦听屏幕按键
while not square.contain(bug):            # 当方块没有碰到虫子的时候
    for dot in dots:                      # 每一个点
        dot.fd(5)
        if dot.overlap_with(line):        # 碰到线条则反向
           dot.right(180)
    if leftkey.down():                    # 如果按下左键
        bug.setheading(180)               # 面向左的方向 
        bug.addx(-5)                      # x坐标左移
        if bug.overlap_with(line):        # 如果和线条重叠了(碰到了) 
            bug.addx(5)                   # x坐标还原(下面的原理相同)
    if rightkey.down():
        bug.setheading(0)
        bug.addx(5)        
        if bug.overlap_with(line):
            bug.addx(-5)
    if upkey.down():
        bug.setheading(90)
        bug.addy(5)        
        if bug.overlap_with(line):
            bug.addy(-5)
    if downkey.down():
        bug.setheading(-90)
        bug.addy(-5)
        if bug.overlap_with(line):
            bug.addy(5)        
    if bug.overlap_with(dotsitems):      # 如果虫子和每个点有碰撞
        bug.goto(-170,10)                # 回到初始坐标   
        bug.play('hurt.wav')             # 虫子发出声音
    time.sleep(0.04)                     # 等待0.04秒

bug.stamp()                              # 虫子盖图章
square.stamp()                           # 方块盖图章 
square.hide()                            # 方块隐藏
square.home()                            # 方块回家
square.write2('成 功')                   # 显示成功二字
screen.mainloop()                        # 进入屏幕主循环
