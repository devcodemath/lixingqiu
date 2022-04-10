"""超级小猫.py"""

from turtle import *             # 从海龟画图导入所有命令
from winsound import PlaySound,SND_ASYNC # 导入播放wav命令和异步常量

喵 = "喵.wav"
width,height= 480,360

screen = Screen()                # 新建屏幕
screen.setup(width,height)       # 设定屏幕宽和高
screen.bgpic("blue-sky.png")     # 设定屏幕背景
screen.title("小猫行走动画")     # 设定屏幕标题
screen.delay(0)

cats = []                        #小猫造型列表,也可用glob('*.gif')实现
for i in range(1,17):
    "补0操作形成gif文件名"
    s = "0" * (4 - len(str(i)))  + str(i) + ".gif" 
    cats.append("images/" + s)
    screen.addshape("images/" + s) # 添加到屏幕的形状列表
amounts = len(cats)              # 求出猫的造型数量

t = Turtle(visible=False)        # 新建不可见海龟对象,名为t
t.penup()                        # 由于不需要画画,所以让它抬笔
t.goto(-300,-110)                # 定位到坐标
t.showturtle()                   # 显示
PlaySound(喵,SND_ASYNC)          # 发声
index = 0                        # 索引为0
def move():
    global index                 # 由于要改变index的值,所以要申明为global
    t.shape(cats[index])         # 设定新的造型
    t.fd(5)                      # 前进5个单位
    index = index + 1            # 索引加1
    index = index % amounts      # 索引对数量求余
    screen.ontimer(move,200)     # 200毫秒后再次运行机制move函数
move()
screen.exitonclick()             # 单击屏幕关闭窗口

               
