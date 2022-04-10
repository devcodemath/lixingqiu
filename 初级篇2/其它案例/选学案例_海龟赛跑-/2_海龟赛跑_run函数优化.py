"""海龟赛跑小动画，请把此代码进行优化"""
 

import time
from random import randint
from turtle import Turtle,Screen        


def init_screen():
    """新建屏幕对象"""
    screen = Screen()
    screen.bgcolor("black")   
    screen.title("海龟赛跑")
    screen.setup(800,600)
    screen.delay(10)
    return screen

def draw_racetrack():    
    """画跑道，返回终点x坐标"""
    t = Turtle()
    t.penup()
    t.goto(-250, 250)   

    for i in range(26):
        t.pencolor("white")  # 线条颜色
        t.write(i)           # 写i
        t.right(90)
        t.forward(10)
        t.pendown()
        t.forward(150)
        t.penup()
        t.backward(160)
        t.left(90)
        t.forward(20)

    t.ht() 
    return  t               #返回海龟对象


 
def command_turtle():
    """印发号施令的裁判海龟"""
    ziti = ("Arial", 50, "normal")
    w = Turtle()  # 发号令的海龟
    w.shape("turtle")
    w.color("yellow","brown")
    w.penup()
    w.goto(0, 10)
    w.pendown()
    w.write("准备好了吗？", align="center", font=ziti)
    time.sleep(1)
    w.clear()
    w.write("OK？", align="center", font=ziti)
    time.sleep(1)
    w.clear()
    w.write("Go", align="center", font=ziti)
    time.sleep(1)
    w.clear()
    penup()

def generate_player():
    """生成5只海龟，做为参赛选手"""
    color = ["red", "white", "blue", "yellow", "cyan"]  # 颜色列表
    turtles = []                                        # 放海龟的列表
    y = 230
    for i in range(5):
        turtles.append(Turtle())                        # 添加到turtles列表
        turtles[i].color(color[i])                      # 设定颜色
        turtles[i].shape("turtle")                      # 设定形状
        turtles[i].penup()                              # 抬笔
        turtles[i].goto(-270, y)                        # 定位
        y = y - 30                                      # y减去30
    return turtles
def print_result(t,color):
    """打印结果"""
    t.ht()                                              #隐藏                 
    t.penup()                                           #抬笔
    t.goto(0, -170)                                     #定位
    t.pendown()                                         #落笔
    t.pencolor(color)                                   #设颜色
    t.write(color + "海龟赢得比赛。", move=False, align="center", font=("Times Roman New", 25, "normal"))

def run(turtles,t):
    """让选手们跑，就是以随机速度移动海龟们,
    参数说明：
    endx ： 终点x坐标
    返回值：None
    """
    running = True
    while running:
       for turtle in turtles:
          turtle.forward(randint(1, 5))       # 随机向前移动1到5个单位的距离 
          x = turtle.xcor()                   # 获取海龟的x坐标
          if x >= t.xcor():                   # 如果这只海龟的x坐标大于endx，则它赢了。
             color = turtle.pencolor()        # 返回画笔颜色
             print_result(t,color)            # 打印结果
             running = False                  # 相当于比赛结束标志
             break

if __name__ == "__main__":

    screen = init_screen()                 #初始化屏幕
    t = draw_racetrack()                   #画跑道，返回画跑道的海龟对象
    turtles = generate_player()            #产生选手
    run(turtles,t)                         #海龟们开始比赛，跑
    
    screen.exitonclick()
 

