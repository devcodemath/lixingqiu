"""
   自制画板.py

   假设屏幕的名称为screen，屏幕是有右键菜单的，菜单的每个项目都有索引号。
   索引号从0开始。当屏幕新建时，单击右键并不会显示出来。我们可以通过
   screen.addpopup()让右键菜单绑定鼠标右键，这样就能通过单击鼠标右键显示菜单了。
   如果不需要它，可以通过screen.removepopup() 命令可移除。
   
   screen有popup属性,它有add_command命令可以增加菜单项目，
   有entryconfig命令，可根据索引号配置现有的菜单项目。
   有delete命令可以根据索引号删除一个菜单项目。
      
   本程序主要演示如何显示与移除右键菜单项目。
   还要学习如何配置现有的项目项目，以及如何增加新的右键菜单项目。
"""
from sprites import *               # 从精灵模块导入所有命令
    
screen = Screen()                   # 新建屏幕
screen.bgcolor('yellow')            # 背景颜色为黄色
screen.titlebar(False)              # 隐藏标题栏
screen.draggable()                  # 按中键可拖动窗口
screen.addpopup()                   # 绑定右键菜单

t = Sprite()                        # 新建角色

# 配置索引为0的菜单项目
screen.popup.entryconfig(0,label='关于',command=lambda:showinfo('关于','本程序由李兴球开发'))

# 下面是给屏幕新增右键菜单项目
screen.popup.add_command(label='落笔',command=lambda:t.pendown())
screen.popup.add_command(label='抬笔',command=lambda:t.penup())
screen.popup.add_command(label='颜色',command=lambda:t.color(askcolor()[-1]))
screen.popup.add_command(label='擦除',command=lambda:t.clear())

screen.mainloop()
