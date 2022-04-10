"""
   命令按钮,本程序演示如何使用tkinter的命令按钮。
   本程序用Python精灵模块开发,需要先在cmd下用命令:
   pip install sprites进行安装。
"""
from sprites import *

screen = Screen()
screen._root._canvas=None
screen.delay(10)
screen.setup(480,360)
screen.title('命令按钮')

bug = Sprite()                     # 新建虫子

# 下面的TK来自于从sprites模块导入的tkinter ，新建框架
frameright = TK.Frame(screen._root,bg='#f3f3a3',padx=8,pady=8)
frameright.pack(expand=1,fill='both')

# 新建按钮
b1 = TK.Button(frameright,text='前进',command=lambda:bug.fd(10))
b1.grid(row=0,column=0,sticky=TK.W)

b2 = TK.Button(frameright,text='倒退',command=lambda:bug.bk(10))
b2.grid(row=1,column=0,sticky=TK.W)

b3 = TK.Button(frameright,text='左转',command=lambda:bug.left(10))
b3.grid(row=2,column=0,sticky=TK.W)

b4 = TK.Button(frameright,text='右转',command=lambda:bug.right(10))
b4.grid(row=3,column=0,sticky=TK.W)

screen.mainloop()
