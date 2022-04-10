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
    
monkey1 = Sprite(shape='monkey.png',tag='monkey')
monkey1.goto(-100,50)

monkey2 = Sprite(shape='monkey.png',tag='monkey')
monkey2.goto(100,100)

monkey3 = Sprite(shape='monkey.png',tag='monkey')
monkey3.goto(130,00)

# 下面新建组，会自动把相应标签的对象都添加到组中
monkey_group = Group("monkey")# 新建由猴子标签组成的猴组

arrow = Sprite(shape='pointer')
arrow.goto(-220,-150)

speed = 10
mkey = Mouse()                # 实例化鼠标左按键 
clock = Clock()               # 实例化时钟对象 
start_shoot_flag = False      # 开始发射标志,值为False表示没有开始发射
while True:
    arrow.heading(mouse_pos())# 箭头朝向鼠标指针的方向
    
    # 按下鼠标指针那么speed,即速度会一直增加
    if mkey.down():
       speed = speed + 0.1
       start_shoot_flag = True  # 值为True,表示开始发射
       screen.title("速度:"+str(speed))

    # 一旦松开鼠标按键,那么就会发射
    if start_shoot_flag and not mkey.down():
        shoot()
        start_shoot_flag = False
        speed = 10
    if ball.isvisible():
       ball.move(ball.dx,ball.dy)        
       ball.dy = ball.dy - 1       
       for m in list(monkey_group):
          if m.collide(ball):m.remove()
       if ball.collide_edge(): ball.hide() # 隐藏小球
    screen.update()
    clock.tick(60)
