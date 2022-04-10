"""
   主菜单制作,本程序重定义_Root类的__init__,增加了createmenu方法,
   关于Root类,请查看turtle.py文件.
   本程序用Python精灵模块开发,需要先在cmd下用命令:
   pip install sprites进行安装。
"""

from sprites import *
from turtle import _Root,ScrolledCanvas
from tkinter.scrolledtext import ScrolledText

# 下面的TK即是tkinter ,从sprites已经导入。
def root__init(self):
    TK.Tk.__init__(self)       # 新建窗口
    # 这个做为背景框架
    self.frame_bg = TK.Frame(self,bg='#e2a2e5',padx=8,pady=8)
    self.frame_bg.pack(expand=1,fill='both')
    
    self.frame_left = TK.Frame(self.frame_bg,bg='#3200f0',padx=8,pady=8)
    self.frame_left.pack(side=TK.LEFT,expand=1,fill='both')
    
    self.frame_right = TK.Frame(self.frame_bg,bg='#00e200',padx=8,pady=8)
    self.frame_right.pack(side=TK.RIGHT,expand=1,fill='both')    

    self.createmenu()    

def root_createmenu(self):
        
    # 创建一个顶级菜单
    menubar = TK.Menu(self)
     
    # 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
    filemenu = TK.Menu(menubar, tearoff=False)
    filemenu.add_command(label="打开", command=lambda:showinfo('hi',''))
    filemenu.add_command(label="保存", command=lambda:showinfo('hi',''))
    filemenu.add_separator()
    filemenu.add_command(label="退出", command=lambda:self.destroy())
    menubar.add_cascade(label="文件", menu=filemenu)
     
    # 创建另一个下拉菜单“编辑”，然后将它添加到顶级菜单中
    editmenu = TK.Menu(menubar, tearoff=False)
    editmenu.add_command(label="剪切", command=lambda:showinfo('hi',''))
    editmenu.add_command(label="拷贝", command=lambda:showinfo('hi',''))
    editmenu.add_command(label="粘贴", command=lambda:showinfo('hi',''))
    menubar.add_cascade(label="编辑", menu=editmenu)
     
    # 显示菜单
    self.config(menu=menubar)

def root_setupcanvas(self,width,height,cwidth,cheight):
    """设置画布"""
    self._canvas = ScrolledCanvas(self.frame_left, width, height, cwidth, cheight)
    self._canvas.pack(expand=1, fill="both")

# 重定义_Root类的初始化方法和setupcanvas方法，增加了createmenu方法以便添加菜单
_Root.createmenu = root_createmenu
_Root.__init__ = root__init
_Root.setupcanvas = root_setupcanvas

screen = Screen()
screen.setup(960,640)
root = screen._root
screen.title('主菜单制作 by 李兴球  www.lixingqiu.com')

cat = Sprite(2)

b0 = TK.Button(root.frame_left,text='风火轮编程',command=lambda:cat.bk(10))
b0.pack()

codetext = ScrolledText(master=root.frame_left,bg='white',
                     font=('新宋体',12,'normal'),width=40,height=0)
codetext.tag_configure("sel", background="skyblue")                   # 选择的时候为天蓝色
codetext.configure(undo=True,autoseparators=True, maxundo=-1)         # 让撤销发生作用
codetext.pack(expand=1, fill="both")
codetext.insert(TK.END, 'from turtle import *')

b1 = TK.Button(root.frame_right,text='右测试按钮',command=lambda:cat.fd(10))
b1.pack()

screen.mainloop()
