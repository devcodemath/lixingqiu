"""海龟赛跑小动画，请把此代码进行优化"""
 

from turtle import *         
import time
from random import randint

def init_screen():
    screen = Screen()
    screen.bgcolor("black")   
    screen.title("海龟赛跑")
    screen.setup(800,600)
    screen.delay(0)
    return screen

def draw_racetrack():    
    """画跑道，返回终点x坐标"""
    t = Turtle()
    t.penup()
    t.goto(-250, 250)  

    # 画跑道

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
    return  t,t.xcor()        #首先超这个坐标的海龟会取得胜利


 
def command_turtle():
    """印发号施令的裁判海龟"""
    ziti = ("Arial", 50, "normal")
    w = Turtle()  # 发号令的海龟
    w.shape("turtle")
    w.color("yellow","brown")
    w.penup()
    w.goto(0, 10)
    w.pendown()
    w.write("准备好了吗？",align="center", font=ziti)
    time.sleep(1)
    w.clear()
    w.write("OK？",align="center", font=ziti)
    time.sleep(1)
    w.clear()
    w.write("Go",align="center", font=ziti)
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
def print_result(color):
    """打印结果"""
    t.ht()                       #隐藏                 
    t.penup()                    #抬笔
    t.goto(0, -170)               #定位
    t.pendown()                  #落笔
    t.pencolor(color)            #设颜色
    t.write(color + "海龟赢得比赛。", move=False, align="center", font=("Times Roman New", 25, "normal"))

def run(endx):
    """让选手们跑，就是以随机速度移动海龟们,
    参数说明：
    endx ： 终点x坐标
    返回值：None
    """

    for i in range(180):
        turtles[0].forward(randint(1, 5))# 随机向前移动1到5个单位的距离 
        a, b = turtles[0].position()
        if a >= endx:                       # 如果这只海龟的x坐标大于endx，则它赢了。        
            print_result("red")
            break
        turtles[1].forward(randint(1, 5))
        a, b = turtles[1].position()
        if a >= endx:       
            print_result("white")
            break     
        turtles[2].forward(randint(1, 5))
        a, b = turtles[2].position()
        if a >= endx:        
            print_result("blue")
            break
        turtles[3].forward(randint(1, 5))
        a, b = turtles[3].position()
        if a >= endx:
            print_result("yellow")
            break
        turtles[4].forward(randint(1, 5))
        a, b = turtles[4].position()
        if a >= endx:        
            print_result("cyan") 
            t.write("青色海龟赢得比赛。", move=False, align="center", font=("Times Roman New", 25, "normal"))
            break

if __name__ == "__main__":

    screen = init_screen()
    t,endx = draw_racetrack()
    turtles = generate_player()
    run(endx)
    
    screen.exitonclick()
 

