"""
   write命令教学档案
   首先,角色所在的区为displayframe,它是一个tkinter框架或者就是tk窗口(不分区时)。
   在sprites版本v1.19中，在新建屏幕的时候可以加布局参数。
   参数的名称叫layout，如果用Screen新建屏幕不写参数或值为1，那么一切还是海龟画图那样的布局。
   如果加了参数值为2，那么会形成左右布局，这个时候会有窗口会一分为二。
   左边的框架叫leftframe，右边的框架叫rightframe。它们的父(master)组件都是root。
   而角色所在的displayframe就在leftframe框架的上面。有一个叫bottomframe的框架
   在leftframe框架的下面。读者可在rightframe和bottomframe这两个框架中放置组件。
   这里需要tkinter知识，在turtle模块中它的缩写为TK。
"""
from sprites import *

screen = Screen(2)         # 新建左右分区的屏幕对象
screen.setup(800,600)
screen.title('write命令教学档案')

turtle = Sprite(shape='turtle')
turtle.color('blue')
turtle.speed(1)
root= screen._root

root.rightframe.pack(expand=0)
root.rightframe.config(padx=10,pady=10)     # 配置右框架背景色与间隙

upframe = TK.Frame(root.rightframe)
upframe.pack(side=TK.TOP,expand=1)
downframe = TK.Frame(root.rightframe)
downframe.pack(side=TK.TOP)

fontstyle = ('黑体',12,'normal')

b0 = TK.Button(upframe,text="import turtle",font=fontstyle)
b0.pack(anchor='w')
def reset():
    turtle.reset()
    turtle.color('blue')
b1 = TK.Button(upframe,text="turtle.reset()",font=fontstyle,command=reset)
b1.pack(anchor='w')

b3 = TK.Button(upframe,text="turtle.sety(250)",font=fontstyle,command=lambda:turtle.sety(250))
b3.pack(anchor='w')
b4 = TK.Button(upframe,text="turtle.write('风火轮编程')",font=fontstyle,command=lambda:turtle.write('风火轮编程'))
b4.pack(anchor='w')

b5 = TK.Button(upframe,text="turtle.sety(200)",font=fontstyle,command=lambda:turtle.sety(200))
b5.pack(anchor='w')
b6 = TK.Button(upframe,text="turtle.write('风火轮编程',align='center')",font=fontstyle,command=lambda:turtle.write('风火轮编程',align='center'))
b6.pack(anchor='w')

b7 = TK.Button(upframe,text="turtle.sety(150)",font=fontstyle,command=lambda:turtle.sety(150))
b7.pack(anchor='w')
b8 = TK.Button(upframe,text="turtle.write('风火轮编程',align='right')",font=fontstyle,command=lambda:turtle.write('风火轮编程',align='right'))
b8.pack(anchor='w')

b9 = TK.Button(upframe,text="turtle.sety(100)",font=fontstyle,command=lambda:turtle.sety(100))
b9.pack(anchor='w')
b10 = TK.Button(upframe,text="turtle.write('风火轮编程',font=('黑体',18,'normal'))",font=fontstyle,command=lambda:turtle.write('风火轮编程',font=('黑体',18,'normal')))
b10.pack(anchor='w')

b11 = TK.Button(upframe,text="turtle.sety(50)",font=fontstyle,command=lambda:turtle.sety(50))
b11.pack(anchor='w')
b12 = TK.Button(upframe,text="turtle.write('风火轮编程',font=('黑体',18,'bold'))",font=fontstyle,command=lambda:turtle.write('风火轮编程',font=('黑体',18,'bold')))
b12.pack(anchor='w')

b13 = TK.Button(upframe,text="turtle.sety(0)",font=fontstyle,command=lambda:turtle.sety(0))
b13.pack(anchor='w')
b14 = TK.Button(upframe,text="turtle.write('风火轮编程',font=('黑体',18,'italic'))",font=fontstyle,command=lambda:turtle.write('风火轮编程',font=('黑体',18,'italic')))
b14.pack(anchor='w')

b15 = TK.Button(upframe,text="turtle.sety(-50)",font=fontstyle,command=lambda:turtle.sety(-50))
b15.pack(anchor='w')
b16 = TK.Button(upframe,text="turtle.write('风火轮编程',move=True)",font=fontstyle,command=lambda:turtle.write('风火轮编程',move=True))
b16.pack(anchor='w')


lb = TK.Label(downframe,text='自行输入代码')
lb.pack(side=TK.TOP)
v = TK.StringVar(root, value="turtle.write('Python',align='center')")
code = TK.Entry(downframe,width=50,font=('宋体',12,'normal'),textvariable=v)
code.pack(side=TK.TOP)
def runcode():
    string = code.get()
    exec(string)
    
run = TK.Button(downframe,text=' 运 行 ',font=('宋体',12,'normal'),command=runcode)
run.pack(side=TK.TOP)



screen.mainloop()

