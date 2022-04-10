"""龟兔赛跑多媒体动画.py,本程序演示乌龟和兔子赛跑。
它们的形状是从外面导入进来的，宽度都是100个像素。"""

from turtle import *                # 从海龟模块导入所有命令
from time import sleep              # 从时间模块导入sleep命令
from random import randint          # 从随机模块导入randint命令
from winsound import PlaySound,SND_ASYNC,SND_LOOP

"定义要用到的变量名称"
game_title = "龟兔赛跑"
turtle_image = "乌龟.gif"
rabbit_image = "兔子.gif"
ziti = ('黑体',32,'normal')

"新建屏幕,进行相应的设置"
screen = Screen()                    # 新建屏幕对象
screen.bgcolor("gray")               # 设置背景为灰色
screen.title(game_title)             # 写上窗口标题
screen.setup(680,580)                # 设定屏幕的宽高
screen.addshape(turtle_image)        # 给屏幕添加乌龟的图形
screen.addshape(rabbit_image)        # 给屏幕添加兔子的图形

"下面的海龟是位'作者',它的任务是在屏幕上显示汉字"
writer = Turtle(visible=False)       # 新建写标题的海龟对象
writer.color("cyan")                 # 设tt的颜色为青色
writer.penup()                       # 抬笔
writer.goto(0,200)                   # 定位
writer.write(game_title,align='center' ,font=ziti)
writer.goto(0,-200)

"设置起始线条"
start_line = Turtle(shape='square')  # 起始线条
start_line.shapesize(10,0.1)         # 横向扩大10倍,纵向为0.1倍
start_line.color("white")            # 颜色为白色
start_line.penup()                   # 抬笔
start_line.goto(-230,0)              # 定位

"设置终点线条与终点x坐标,谁的x坐标先超过则为赢"
endx = 230                           # 设置终点x坐标
end_line = Turtle(shape='square')    # 终点线条
end_line.shapesize(10,0.1)           # 横向扩大10倍,纵向为0.1倍
end_line.color("red")                # 颜色为红色
end_line.penup()                     # 抬笔
end_line.goto(endx,0)                # 定位

"选手一号,兔子"
r = Turtle(shape=rabbit_image)       # 新建兔子对象
r.penup()
r.goto(-280,50)

"选手二号,乌龟"
t = Turtle(shape=turtle_image)       # 新建乌龟对象
t.penup()
t.goto(-280,-50)

"准备开始播放音乐,开始赛跑"
PlaySound("Hawaii Five-O.wav",SND_ASYNC|SND_LOOP)
sleep(1)
while True:
    t.fd(randint(2,6))               # 乌龟移动随机个单位
    sleep(0.1)
    if t.xcor() + 50 >= endx:        # 由于它的宽度为100,所以这里加50
        result = "乌龟赢了"
        break
    
    r.fd(randint(2,6))               # 兔子移动随机个单位
    sleep(0.1)
    if r.xcor() + 50 >= endx:        # 由于它的宽度为100,所以这里加50
        result = "兔子赢了"
        break
    
writer.color("yellow")   
writer.write(result,align='center' ,font=ziti)
screen.exitonclick()
