"""
   抛物模块_射猴子.py
   按住鼠标左键,速度会一直增加,松开后发射!
"""
import math
from sprites import *

def shoot():
    global speed
    ball.goto(arrow.pos())            #  到达箭头坐标
    angle = math.radians(ball.towards(mouse_pos()))
    ball.dx = speed * math.cos(angle)
    ball.dy = speed * math.sin(angle)
    ball.show()
    
width,height = 516,389
screen = Screen()
screen.setup(width,height)
screen.bgpic('森林.png')

# 新建造型为'circle'的小球
ball = Sprite(shape='circle',visible=False)

# 新建36只猴子
counter = 0
bossid = random.randint(1,36)           # 随机数
x ,y = -200,150
for i in range(4):                      # 4行
    for j in range(9):                  # 9列
        m = Sprite(shape='monkey.png',tag='monkey')
        m.rotatemode(1)                 # 设定旋转模式为左右翻转
        counter +=1
        if counter == bossid: # 如果生成这只猴子的时候，counter刚好等于bossid
            m.血量 = 1000
        else:
            m.血量 = 1
        m.goto(x,y)
        x = x + 50
    y = y -50
    x = -200
# 新建石头
stone = Sprite('circle',visible=False)
stone.color('cyan')
# 下面新建组，会自动把相应标签的对象都添加到组中
monkey_group = Group("monkey")# 新建由猴子标签组成的猴组

base = Sprite(shape='square',pos=(0,-180)) # 基坐
base.shapesize(1,2)

ak = Key('a')                  # 新建键盘a键
dk = Key('d')                  # 新建键盘d键 
screen.listen()

arrow = Sprite(shape='pointer')
arrow.goto(-220,-150)

speed = 10
mkey = Mouse()                # 实例化鼠标左按键 
clock = Clock()               # 实例化时钟对象 
start_shoot_flag = False      # 开始发射标志,值为False表示没有开始发射
counter = 0                   # 计数器
running = True
while running:
    if stone.isvisible():
        stone.fd(5)
        if stone.collide_edge():stone.hide()
    if random.randint(1,100)==1 and stone.ishide():
        stone.goto(random.choice([m.pos() for m in monkey_group if m.isvisible()]))
        stone.heading(base)
        stone.show()
                   
    if ak.down():base.addx(-2)      # 如果按a键,往左移
    if dk.down():base.addx(2)       # 如果按d键,往右称
    arrow.goto(base.pos())          # 箭头到达base的坐标 
    arrow.heading(mouse_pos())# 箭头朝向鼠标指针的方向
    
    # 按下鼠标指针那么speed,即速度会一直增加
    if mkey.down():
       speed = speed + 0.1
       start_shoot_flag = True  # 值为True,表示已按下鼠标左键,
       screen.title("速度:"+str(speed))

    # 刚才按下子,现在又松开了鼠标按键,那么就会发射
    if start_shoot_flag and not mkey.down():
        shoot()
        start_shoot_flag = False
        speed = 10
    if ball.isvisible():
       ball.move(ball.dx,ball.dy)        
       ball.dy = ball.dy - 1       
       for m in list(monkey_group):
          if m.collide(ball) and m.isvisible():
              m.血量 -= 1
              if m.血量 < 1:m.ht() 
       if ball.collide_edge(): ball.hide() # 隐藏小球
    all_monkeys = [m for m in monkey_group if m.isvisible()] # 所有看得见的猴子
    if len(all_monkeys)==1:                  # 如果只有一只了
        all_monkeys[0].fd(4)                 # 则前进
        all_monkeys[0].bounce_on_edge()      # 碰到边缘就返弹
    screen.update()
    clock.tick(60)
