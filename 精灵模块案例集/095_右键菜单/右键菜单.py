"""
   右键菜单,本程序演示如何使用tkinter的右键菜单,
   本程序用Python精灵模块开发,需要先在cmd下用命令:
   pip install sprites进行安装。
"""

from sprites import *

screen = Screen()
screen.colormode(255)
screen.setup(480,360)
screen.title('右键菜单')

def backgroundcolor():
    """设定背景颜色"""    
    c = askcolor()
    if c[0]!=None:
        color = list(c[0])
        color1 = [int(c) for c in color]
        color2 = [str(int(c)) for c in color]
        screen.bgcolor(color1)
        
# 下面的TK是就是tkinter
popup = TK.Menu(screen._root, tearoff=0)
popup.add_command(label="bgcolor(背景颜色)" ,command=backgroundcolor)
popup.add_separator()
popup.add_command(label="关于本程序",command=lambda:showinfo('关于','本程序由李兴球开发\n\nQQ:406273900\n\nwww.lixingqiu.com'))
popup.add_command(label="打开主页",command=lambda:os.system('explorer http://www.lixingqiu.com'))
popup.add_command(label="退出本程序",command=lambda:screen.bye())

def do_popup(event):
    """显示弹出菜单"""
    try:
        popup.tk_popup(event.x_root, event.y_root + 10, 0)
    finally:
        # 确保释放按键
        popup.grab_release()

screen.cv.bind("<Button-3>", do_popup)   # 画布绑定鼠标右键

screen.mainloop()
