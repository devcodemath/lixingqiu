"""
   画太极图教学辅助程序。
   本程序采用Screen(3)把窗口整体分为两个大区。
   上面的是root.topframe，下面的是root.bottomframe。
   在root.bottomframe框架中，又分为左右两个框架，
   名称分别是lframe和rframe。
   其中lframe又分为frameup和framedown两个框架。
   而rframe又分为rframeleft和rframeright两个框架。
   为更好的理解，请查看'程序的窗口分区示意图.png'图形。
"""
from sprites import *

def draw_filled_circle():
    """画填充颜色的圆形"""
    x = int(xvar.get())
    y = int(yvar.get())
    radius = int(radiusvar.get())
    color = colorvar.get()
    angle = int(anglevar.get())
    pdstatus = turtle.isdown()    # 保存是否落笔状态    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor(color)
    screen.tracer(0,0)
    for x in range(angle*10):
        turtle.fd(radius)
        turtle.bk(radius)
        turtle.rt(0.1)                
    if pdstatus:
        turtle.pendown()
    else:
        turtle.penup()
    screen.tracer(1,0)
    
    
screen = Screen(3)              # 上下框架结构topframe和bottomframe
screen.bgcolor('#a0aea2')
screen.title('画太极图教学辅助程序')

turtle = Sprite(shape='turtle') # 新建一只海龟
turtle.penup()
turtle.pensize(2)
turtle.shapesize(2,2,2)
turtle.setheading(90)
turtle.color('black','yellow')
turtle.say('你好,请单击按钮',10,False)

root = screen._root
root.topframe.pack(expand=1,fill='both')
root.bottomframe.pack(expand=0,fill='both',padx=10)

lframe = TK.Frame(root.bottomframe,bg='yellow')
lframe.pack(side=TK.LEFT)
rframe = TK.Frame(root.bottomframe,bg='pink')
rframe.pack(side=TK.LEFT,expand=1,fill='both')

frameup = TK.Frame(lframe,bg='blue')
frameup.pack(side=TK.TOP,expand=0,fill='both',padx=10)
framedown = TK.Frame(lframe,bg='cyan')
framedown.pack(side=TK.BOTTOM,expand=0,fill='both',padx=10,pady=10)

drawcircle = TK.Button(frameup,text='画圆形',font=('黑体',13,'normal'),command=draw_filled_circle)
drawcircle.pack(side=TK.LEFT)

xvar = TK.StringVar(value='0')
x_lable = TK.Label(frameup,text='x:')
x_lable.pack(side=TK.LEFT)
x_cor = TK.Entry(frameup,width=5,textvariable=xvar)
x_cor.pack(side=TK.LEFT)

yvar = TK.StringVar(value='0')
y_lable = TK.Label(frameup,text='y:')
y_lable.pack(side=TK.LEFT)
y_cor = TK.Entry(frameup,width=5,textvariable=yvar)
y_cor.pack(side=TK.LEFT)

colorvar = TK.StringVar(value='black')
color_lable = TK.Label(frameup,text='颜色:')
color_lable.pack(side=TK.LEFT)
color = TK.Entry(frameup,width=8,textvariable=colorvar)
color.pack(side=TK.LEFT)

radiusvar = TK.StringVar(value='100')
radius_lable = TK.Label(frameup,text='半径:')
radius_lable.pack(side=TK.LEFT)
radius = TK.Entry(frameup,width=8,textvariable=radiusvar)
radius.pack(side=TK.LEFT)

anglevar= TK.StringVar(value='180')
angle_lable = TK.Label(frameup,text='角度:')
angle_lable.pack(side=TK.LEFT)
angle = TK.Entry(frameup,width=8,textvariable=anglevar)
angle.pack(side=TK.LEFT)

def cmd1():
    xvar.set('0')
    yvar.set('0')
    colorvar.set('black')
    radiusvar.set('100')
    anglevar.set('180')
    draw_filled_circle()
    step1['state']= TK.DISABLED
    
def cmd2():
    xvar.set('0')
    yvar.set('0')
    colorvar.set('white')
    radiusvar.set('100')
    anglevar.set('180')
    draw_filled_circle()
    step2['state']= TK.DISABLED
    
def cmd3():
    xvar.set('0')
    yvar.set('50')
    colorvar.set('white')
    radiusvar.set('50')
    anglevar.set('360')
    draw_filled_circle()
    step3['state']= TK.DISABLED
    
def cmd4():
    xvar.set('0')
    yvar.set('-50')
    colorvar.set('black')
    radiusvar.set('50')
    anglevar.set('360')
    draw_filled_circle()
    step4['state']= TK.DISABLED
    
def cmd5():
    pdstatus = turtle.isdown()    # 保存是否落笔状态
    turtle.penup()
    turtle.goto(0,-50)
    turtle.dot(20,'white')    
    if pdstatus:
        turtle.pendown()
    else:
        turtle.penup()
    step5['state']= TK.DISABLED
    
def cmd6():
    pdstatus = turtle.isdown()    # 保存是否落笔状态
    turtle.penup()
    turtle.goto(0,50)
    turtle.dot(20,'black')    
    if pdstatus:
        turtle.pendown()
    else:
        turtle.penup()
    step6['state']= TK.DISABLED
     
step1 = TK.Button(framedown,text='第一步:在(0,0)坐标向右画一个半径为100的黑色半圆',font=('黑体',13,'normal'),command=cmd1)
step1.pack(side=TK.TOP)

step2 = TK.Button(framedown,text='第二步:在(0,0)坐标向右画一个半径为100的白色半圆',font=('黑体',13,'normal'),command=cmd2)
step2.pack(side=TK.TOP)

step3 = TK.Button(framedown,text='第三步:在(0,50)坐标向右画一个半径为50的白色半圆',font=('黑体',13,'normal'),command=cmd3)
step3.pack(side=TK.TOP)

step4 = TK.Button(framedown,text='第四步:在(0,-50)坐标向右画一个半径为50的黑色半圆',font=('黑体',13,'normal'),command=cmd4)
step4.pack(side=TK.TOP)

step5 = TK.Button(framedown,text='第五步:在(0,-50)坐标打一个白色的小圆点',font=('黑体',13,'normal'),command=cmd5)
step5.pack(side=TK.TOP)

step6 = TK.Button(framedown,text='第六步:在(0,50)坐标打一个黑色的小圆点',font=('黑体',13,'normal'),command=cmd6)
step6.pack(side=TK.TOP)


# 在bottomframe的右边放几个常用操作按钮
rframeleft = TK.Frame(rframe,bg='dodger blue')
rframeleft.pack(side=TK.LEFT,expand=1,fill='both')
rframeright = TK.Frame(rframe,bg='green')
rframeright.pack(side=TK.LEFT,expand=1,fill='both')

def reset():
    turtle.reset()
    turtle.penup()
    turtle.pensize(2)
    turtle.shapesize(2,2,2)
    turtle.setheading(90)
    turtle.color('black','yellow')
    turtle.say('你好,请单击按钮',10,False)
    step1['state']= TK.NORMAL
    step2['state']= TK.NORMAL
    step3['state']= TK.NORMAL
    step4['state']= TK.NORMAL
    step5['state']= TK.NORMAL
    step6['state']= TK.NORMAL
    
clearb = TK.Button(rframeleft,text='重置',font=('黑体',13,'normal'),command=reset)
clearb.pack(side=TK.TOP)

fd10b = TK.Button(rframeleft,text='前进10',font=('黑体',13,'normal'),command=lambda:turtle.fd(10))
fd10b.pack(side=TK.TOP)

bk10b = TK.Button(rframeleft,text='倒退10',font=('黑体',13,'normal'),command=lambda:turtle.bk(10))
bk10b.pack(side=TK.TOP)

right10b = TK.Button(rframeleft,text='右转10度',font=('黑体',13,'normal'),command=lambda:turtle.right(10))
right10b.pack(side=TK.TOP)

left10b = TK.Button(rframeleft,text='左转10度',font=('黑体',13,'normal'),command=lambda:turtle.left(10))
left10b.pack(side=TK.TOP)

pendownb = TK.Button(rframeleft,text='落笔',font=('黑体',13,'normal'),command=lambda:turtle.pendown())
pendownb.pack(side=TK.TOP)

penupb = TK.Button(rframeleft,text='抬笔',font=('黑体',13,'normal'),command=lambda:turtle.penup())
penupb.pack(side=TK.TOP)

def gohome():
    turtle.home()
    turtle.setheading(90)
    
homeb = TK.Button(rframeright,text='回家',font=('黑体',13,'normal'),command=gohome)
homeb.pack(side=TK.TOP)
randomb = TK.Button(rframeright,text='随机位置',font=('黑体',13,'normal'),command=lambda:turtle.randompos())
randomb.pack(side=TK.TOP)

def callaskcolor():
    c = askcolor()
    turtle.color(c[1])    
colorb = TK.Button(rframeright,text='颜色',font=('黑体',13,'normal'),command=callaskcolor)
colorb.pack(side=TK.TOP)

def runcommand():
    c = screen.textinput('运行','海龟名称为turtle,屏幕名称为screen,请自行输入命令:')
    if c=='' or c == None:return
    try:
        exec(c)
    except Exception as e :
        showinfo('错误',str(e))
    
runb = TK.Button(rframeright,text='运行',font=('黑体',13,'normal'),command=runcommand)
runb.pack(side=TK.TOP)

screen.mainloop()
