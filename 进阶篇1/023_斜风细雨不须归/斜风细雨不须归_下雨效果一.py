from turtle import Turtle,Screen         # 导入海龟命令
from random import randint               # 导入 randint
 
width,height = 800,600                   # 定义全局变量
screen = Screen()                        # 新建屏幕对象
screen.bgcolor("black")                  # 设定屏幕背景
screen.bgpic("bg.png")                   # 设屏幕背景图
screen.setup(width,height)               # 设屏幕宽和高
screen.delay(0)                          # 设定屏幕延时
screen.title("斜风细雨不须归_下雨效果一")# 设定屏幕标题
screen.addshape('line',((0,0),(0,100)))  # 增加line形状

rain = Turtle(visible=False,shape='line')# 建line形对象
rain.penup()                             # 抬笔以便不画
rain.setheading(-100)                    # 定方向为-100
rain.color("gray")                       # 设颜色为青色 
rains = [rain.clone() for i in range(50)]# 克隆50个rain
rains.append(rain)                       # 添加到列表中

for rain in rains:                       # 依次迭代列表
    x = randint(-width//2,width//2)      # 设定 x值范围
    y = randint(height//2 ,600 + height//2 )  # y值范围
    rain.goto(x,y)                       # 定位初始坐标
    rain.showturtle()                    # 显示rain对象

while True:                              # 当成立的时候
    for rain in rains:                   # 依次迭代列表
        rain.fd(20)                      # rain 前进 20
        if rain.ycor() < -height//2:     # 到了最低坐标
            rain.ht()                    # 隐藏rain对象
            x = randint(-width//2,width//2)   # 设x坐标
            y = randint(height//2 ,600 + height//2 )
            rain.goto(x,y)               # 定位到 (x,y)
            rain.st()                    # 重新显示rain
                    
 
    

