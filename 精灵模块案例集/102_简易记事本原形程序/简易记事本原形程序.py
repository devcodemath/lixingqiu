"""
   简易记事本原形程序(主菜单),本程序不需要重定义Root,直接给窗口添加菜单
"""

from sprites import *
from tkinter.scrolledtext import ScrolledText

screen = Screen()
screen.resizable()
root = screen._root
root._canvas.pack_forget()    # 把屏幕画布给隐藏了
root.config(bg='#00ffff')     # 这是TK窗口的背景颜色了

# 创建一个顶级菜单
menubar = TK.Menu(root)
 
# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = TK.Menu(menubar, tearoff=False)
filemenu.add_command(label="打开", command=lambda:showinfo('hi',''))
filemenu.add_command(label="保存", command=lambda:showinfo('hi',''))
filemenu.add_separator()
filemenu.add_command(label="关于", command=lambda:showinfo('www.lixingqiu.com','本程序基于Python海龟画图'))
filemenu.add_command(label="退出", command=lambda:root.destroy())
menubar.add_cascade(label="文件", menu=filemenu)
 
# 创建另一个下拉菜单“编辑”，然后将它添加到顶级菜单中
editmenu = TK.Menu(menubar, tearoff=False)
editmenu.add_command(label="剪切", command=lambda:showinfo('hi',''))
editmenu.add_command(label="拷贝", command=lambda:showinfo('hi',''))
editmenu.add_command(label="粘贴", command=lambda:showinfo('hi',''))
menubar.add_cascade(label="编辑", menu=editmenu)
 
# 显示菜单
root.config(menu=menubar)

stext2 = ScrolledText(master=root,bg='white',font=('新宋体',12,'normal'))
stext2.tag_configure("sel", background="skyblue")                   # 选择的时候为天蓝色
stext2.configure(undo=True,autoseparators=True, maxundo=-1)         # 让撤销发生作用
stext2.pack(expand=1,fill='both')
stext2.insert(TK.END, '风火轮编程')

# 给stext2加右键菜单
popup_stext2 = TK.Menu(screen._root, tearoff=0)
popup_stext2.add_command(label="撤销 Undo",accelerator="Ctrl+Z",command=lambda: stext2.event_generate("<<Undo>>"))
popup_stext2.add_command(label="重做 Redo",accelerator="Ctrl+Y",command=lambda: stext2.event_generate("<<Redo>>"))
popup_stext2.add_separator()
popup_stext2.add_command(label="复制 Copy",accelerator="Ctrl+C",command=lambda: stext2.event_generate("<<Copy>>"))
popup_stext2.add_command(label="剪切 Cut",accelerator="Ctrl+X",command=lambda: stext2.event_generate("<<Cut>>"))
popup_stext2.add_command(label="粘贴 Paste",accelerator="Ctrl+V",command=lambda: stext2.event_generate("<<Paste>>"))
popup_stext2.add_separator()
popup_stext2.add_command(label="全选 Select All",accelerator="Ctrl+A",command=lambda: stext2.event_generate("<<SelectAll>>"))
popup_stext2.add_command(label="清空",command=lambda: stext2.delete('1.0', TK.END) )
popup_stext2.add_command(label="打开主页",command=lambda:os.system('explorer http://www.lixingqiu.com'))

def do_popup_stext2(event):
    # 显示stext2的右键菜单
    try:
        popup_stext2.tk_popup(event.x_root, event.y_root+10, 0)
    finally:        
        popup_stext2.grab_release()

stext2.bind("<Button-3>", do_popup_stext2)

screen.mainloop()
