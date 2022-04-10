"""伦敦之眼动态贺卡.py 。"""

from time import sleep
from turtle import Screen,Turtle

info = "风火轮少儿编程"
info2 = "祝你元旦快乐"
ziti = ("黑体",32,"normal")
ziti2 = ("楷体制",24,"bold")
colors = ['red','yellow','green','cyan','magenta','blue','white']
amounts = len(colors)
index = 0

screen = Screen()
screen.bgcolor("black")
screen.delay(0)
screen.setup(800,553)
screen.bgpic("伦敦之眼.png")
screen.title(info)

t = Turtle(visible=False)
t.speed(0)
t.penup()
t.goto(-350,177)
t.color("cyan")

for  i in range(200):
    t.clear()                 # 清除
    t.write(info,font=ziti)   # 在新的位置上重写
    screen.update()           # 刷新
    sleep(0.01)               # 延时0.01秒
    t.fd(1)                   # 移动

def repeat():    
    global index              # 申明index为全局变量
    t.color(colors[index])    # 设定颜色
    t.clear()                 # 清除所写
    t.write(info,font=ziti)   # 写字
    index = index + 1         # 索引+1
    index = index % amounts   # 索引对数量求余
    screen.ontimer(repeat,1000) # 1秒后再次执行repeat
repeat()
sleep(1)

t2 = Turtle(visible=False)
t2.speed(0)
t2.penup()
t2.color("yellow")
t2.goto(-90, 50)
for c in info2:                # 遍历字符串
    t2.write(c,move=True,align='center',font=ziti2)
    t2.fd(18)
    sleep(1)
    
screen.exitonclick()          # 单击屏幕关闭窗口
