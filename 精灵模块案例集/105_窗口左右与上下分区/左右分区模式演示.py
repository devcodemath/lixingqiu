"""
   左右分区模式演示,
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
screen.title('左右分区模式演示')

bug = Sprite()

root= screen._root

root.rightframe.config(bg='#F0fff0',padx=10,pady=10)     # 配置右框架背景色与间隙
root.bottomframe.config(bg='#f0f0f0',padx=10,pady=10)    # 配置下框架背景色与间隙

b1 = TK.Button(root.bottomframe,text='本按钮在bottomframe中',font=('黑体',13,'normal'))
b1.pack()
b2 = TK.Button(root.rightframe,text='本按钮在rightframe中',font=('黑体',13,'normal'))
b2.pack()

screen.mainloop()

