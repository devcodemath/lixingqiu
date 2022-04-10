"""
   上下分区模式演示,
   首先,角色所在的框架区为displayframe,它是一个tkinter框架或者就是tk窗口(不分区时)。
   在sprites版本v1.19中，在新建屏幕的时候可以加布局参数。
   参数的名称叫layout，如果用Screen新建屏幕不写参数或值为1，那么一切还是海龟画图那样的布局。
   如果加了参数值为3，那么会形成下下布局，这个时候会有窗口会一分为二。
   上面的区域框架名为topframe,下面的框架名为bottomframe,它们的master都是root。
   
   角色所在的滚动画布的master框架为displayframe，它在topframe框架中的左面。
   rightframe在topframe框架的右面。也就是说rightframe和displayframe的master都是topframe。
   读者可在rightframe和bottomframe中放置组件。
"""
from sprites import *

screen = Screen(3)         # 上下分区模式
screen.title('窗口上下分区模式演示')
bug = Sprite()

root= screen._root
#screen = Screen(2)         # 布局好后,无法修改,这是由于Screen发现已经有了窗口,则不再新建,直接返回
root.rightframe.config(bg='#F0fff0',padx=10,pady=10)
root.bottomframe.config(bg='#f0f0f0',padx=10,pady=10)
b1 = TK.Button(root.bottomframe,text='本按钮在bottomframe中',font=('黑体',13,'normal'))
b1.pack()
b2 = TK.Button(root.rightframe,text='本按钮在rightframe中',font=('黑体',13,'normal'))
b2.pack()

screen.mainloop()

