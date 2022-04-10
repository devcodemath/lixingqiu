"""海龟赛跑小动画，程序看起来比较乱，
变量命名也不规范，有冗余的代码，
请把此代码进行优化
"""

from turtle import *         
import time
from random import randint

screen = Screen()
screen.bgcolor("black")   
screen.title("海龟赛跑")
screen.setup(800,600)
screen.delay(10)

t = Turtle()
t.penup()
t.goto(-250, 250)  

"用t来画跑道"
for i in range(26):
    t.pencolor("white")  # 线条颜色
    t.write(i)
    t.right(90)
    t.forward(10)
    t.pendown()
    t.forward(150)
    t.penup()
    t.backward(160)
    t.left(90)
    t.forward(20)

t.ht() 
x = t.xcor()        #x是终点坐标，首先超这个坐标的海龟会取得胜利


"生成5只海龟，放在起跑线上"
color = ["red", "white", "blue", "yellow", "cyan"]  # 颜色列表
turtles = []                                        # 放海龟的列表
y = 230                                             # 参加比较的第一只海龟的y坐标
for i in range(5):
    turtles.append(Turtle())                        # 添加到turtles列表
    turtles[i].color(color[i])                      # 设定颜色
    turtles[i].shape("turtle")                      # 设定形状
    turtles[i].penup()                              # 抬笔
    turtles[i].goto(-270, y)                        # 定位
    y = y - 30                                      # y减去30，每只海龟的y坐标依次递减
  
 
"发号令的海龟，在屏幕上打印些字，表示要开始。"
w = Turtle()  
w.shape("turtle")
w.color("yellow","brown")
w.penup()
w.goto(0, 10)
w.pendown()
w.write("准备好了吗？", move=False, align="center", font=("Arial", 50, "normal"))
time.sleep(1)
w.clear()
w.write("OK？", move=False, align="center", font=("Arial", 50, "normal"))
time.sleep(1)
w.clear()
w.write("Go", move=False, align="center", font=("Arial", 50, "normal"))
time.sleep(1)
w.clear()
penup()

"下面是以随机‘速度’移动海龟们"
for i in range(180):
    turtles[0].forward(randint(1, 5))# 随机向前移动1到5个单位的距离 
    a, b = turtles[0].position()     # 索引为0的海龟的坐标，为什么要命名为a,b?
    if a >= x:                       # 如果这只海龟的x坐标大于x，则它赢了。        
        t.ht()                       #隐藏                 
        t.penup()                    #抬笔
        t.goto(0, -170)              #定位
        t.pendown()                  #落笔
        t.pencolor("red")            #设颜色
        t.write("红色海龟赢得比赛。", move=False, align="center", font=("Times Roman New", 25, "normal"))
        break
    turtles[1].forward(randint(1, 5)) #索引为1的海龟前进1到5像素
    a, b = turtles[1].position()
    if a >= x:       
        t.ht()
        t.penup()
        t.goto(0, -170)
        t.pendown()
        t.pencolor("white")
        t.write("白色海龟赢得比赛。", move=False, align="center", font=("Times Roman New", 25, "normal"))
        break
    turtles[2].forward(randint(1, 5)) #索引为2的海龟前进1到5像素
    a, b = turtles[2].position()
    if a >= x:        
        t.ht()
        t.penup()
        t.goto(0, -170)
        t.pendown()
        t.pencolor("blue")
        t.write("蓝色海龟赢得比赛。", move=False, align="center", font=("Times Roman New", 25, "normal"))
        break
    turtles[3].forward(randint(1, 5)) #索引为3的海龟前进1到5像素
    a, b = turtles[3].position()
    if a >= x:
        t.ht()        
        t.penup()
        t.goto(0, -170)
        t.pendown()
        t.pencolor("Yellow")
        t.write("黄色海龟赢得比赛。", move=False, align="center", font=("Times Roman New", 25, "normal"))
        break
    turtles[4].forward(randint(1, 5)) #索引为4的海龟前进1到5像素
    a, b = turtles[4].position()
    if a >= x:        
        t.ht()
        t.penup()
        t.goto(0, -170)
        t.pendown()
        t.pencolor("Cyan")
        t.write("青色海龟赢得比赛。", move=False, align="center", font=("Times Roman New", 25, "normal"))
        break
screen.exitonclick()
 

