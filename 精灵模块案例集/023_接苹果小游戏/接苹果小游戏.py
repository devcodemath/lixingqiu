"""
   接苹果小游戏，本程序实现操作一个篮子去接苹果,
   Sprite类是继承自Turtle的一个类，所以基于海龟画图。
"""
from sprites import *

screen = Screen()                        # 新建屏幕
screen.tracer(0,0)                       # 追踪命令                  
screen.setup(800,500)
screen.bgpic('greenforest.png')

basket = Sprite('basket.png')            # 新建篮子

counter = 0
clock = Clock()                          # 新建时钟对象
while 1:
    if random.randint(1,10)==1:          # 产生一个苹果
        x = random.randint(-380,380)     # x坐标
        y = 400                          # y坐标
        a = Sprite('apple.png',pos=(x,y),tag='apple')        
        a.scale(max(0.5,random.random()))# 缩放大小
    
    for apple in screen.turtles():
        if apple.get_tag()!= 'apple':continue      
        apple.move(0,-5)                   # 在水平和垂直方向移动
        if apple.collide(basket):
            apple.remove()                 # 移除苹果
            counter += 1                   # 接到苹果了进行统计
            continue
        if apple.ycor() < -250:apple.remove()
    mx,my = mousepos()                    # 获取鼠标指针的x,y坐标
    basket.goto(mx,-180)    
    screen.update()
    screen.title('接苹果小游戏，已接到：' + str(counter) + '个苹果')
    
    clock.tick(60)
    
    
    
