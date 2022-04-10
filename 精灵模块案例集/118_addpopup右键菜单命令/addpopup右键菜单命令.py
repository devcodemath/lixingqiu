"""
屏幕对象有一个叫popup的右键菜单，需要用addpopup方法绑定鼠标右键它才能调用。如果要”移除”的话，可以用removepopup方法。这本质上是取消鼠标右键的绑定。

默认的右键菜单只有三大项，即”关于本程序”和”截取本窗口屏幕”以及“退出本程序”。它们的索引号分别是0和1及2。对菜单项目进行添加，删除，修改的话遵循tkinter语法。假设有名为screen的屏幕对象，那么:
㈠ 删除一项菜单：screen.popup.delete( startindex [, endindex ]),参数为起始和结束索引号。

㈡ 修改菜单项目: screen.popup.entryconfig( index, options ),options就是可选项，如可以重新指派新的命令，重新指派label等。

㈢ 增加一个菜单项目：screen.popup.add_command命令，以下是示例:
fun = lambda:os.system('explorer http://www.lixingqiu.com'))
screen.popup.add_command(label=“打开主页”,command=fun)
更详细的说明请打开网址 : http://www.lixingqiu.com/2020/02/26/tkinter_menu/ 

"""
from sprites import *

screen = Screen()         # 新建屏幕
screen.bgcolor('lime')    # 设定背景颜色
screen.titlebar(False)    # 不显示标题栏 
screen.draggable()        # 按中键可拖动窗口
#screen.setalpha()        # 设置窗口为半透明(0到1.0的值)打开后截屏不到!
screen.addpopup()         # 绑定右键菜单

# 给右键菜单添加一项
screen.popup.add_command(label='打开主页',command=lambda:os.system('explorer http://www.lixingqiu.com'))

screen.popup.entryconfig(1,label='单击截本窗口屏幕')  # 配置原有的截屏菜单项目

screen.mainloop()
