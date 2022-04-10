"""
   抛物模块_射猴子.py
   按住鼠标左键,速度会一直增加,松开后发射!
"""
import math
from sprites import *

def shoot():
    global speed
    # 新建标签为'ball'的小球
    ball = Sprite(shape='circle',visible=False,tag='ball') 
    ball.goto(arrow.pos())            #  到达箭头坐标
    angle = math.radians(ball.towards(mouse_pos()))
    ball.dx = speed * math.cos(angle)
    ball.dy = speed * math.sin(angle)
    ball_group.rebuild()
    ball.show()
    
width,height = 516,389
screen = Screen()
screen.setup(width,height)
screen.bgpic('森林.png')

monkey1 = Sprite(shape='monkey.png',tag='monkey')
monkey1.goto(-100,50)

monkey2 = Sprite(shape='monkey.png',tag='monkey')
monkey2.goto(100,100)

monkey3 = Sprite(shape='monkey.png',tag='monkey')
monkey3.goto(130,00)

arrow = Sprite(shape='pointer')
arrow.goto(-220,-150)

# 下面新建组，会自动把相应标签的对象都添加到组中
ball_group = Group('ball')    # 新建由ball标签组成的球组
monkey_group = Group("monkey")# 新建由猴子标签组成的猴组

speed = 10
mkey = Mouse()                # 实例化鼠标按键 
clock = Clock()               # 实例化时钟对象 
start_shoot_flag = False      # 开始发射的一个标志
while True:
    arrow.heading(mouse_pos())# 箭头朝向鼠标指针的方向
    
    # 按下鼠标指针那么speed,即速度会一直增加
    if mkey.down() and len(ball_group)==0:
       speed = speed + 0.1
       start_shoot_flag = True
       screen.title("速度:"+str(speed))

    # 一旦松开鼠标指针,那么就会发射
    if start_shoot_flag and not mkey.down():
        shoot()
        start_shoot_flag = False
        speed = 10

    # ball_group是继承自set的组,在下面的for循环中的
    # b.remove() 命令会动态的改变它,所以把它转换成
    # 列表进行遍历。
    for b in list(ball_group):         
        b.move(b.dx,b.dy)        
        b.dy = b.dy - 1
        if b.collide_edge(): b.remove() # 从球组和总表中移除

    for m in list(monkey_group):
        if len(ball_group)==0:continue
        for ball in ball_group:
            if m.collide(ball):m.remove()
    screen.update()
    clock.tick(60)
