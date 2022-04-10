"""
   屏幕分区原理程序,本程序重定义_Root类的__init__,让窗口分为四个区。
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
    
    self.frame_left = TK.Frame(self.frame_bg,bg='#e20000',padx=8,pady=8,height=360,width=480)
    self.frame_left.pack(side=TK.LEFT,expand=1,fill='both')
    
    self.frame_right = TK.Frame(self.frame_bg,bg='#00e200',padx=8,pady=8)
    self.frame_right.pack(side=TK.RIGHT,expand=1,fill='both')
    
    self.frame_centertop = TK.Frame(self.frame_bg,bg='#0000e2',padx=8,pady=8)
    self.frame_centertop.pack(side=TK.TOP,expand=1,fill='both')
    
    self.frame_centerbottom = TK.Frame(self.frame_bg,bg='#433440',padx=8,pady=8)
    self.frame_centerbottom.pack(side=TK.BOTTOM,expand=1,fill='both')
    
def root_setupcanvas(self,width,height,cwidth,cheight):
    self._canvas = ScrolledCanvas(self.frame_left, width, height, cwidth, cheight)
    self._canvas.pack(expand=1, fill="both")

# 重定义_Root类的初始化方法和setupcanvas方法，具体定义请查看turtle.py
_Root.__init__ = root__init
_Root.setupcanvas = root_setupcanvas

screen = Screen()
screen.setup(960,640)
root = screen._root
screen.title('屏幕分区原理程序 by 李兴球  www.lixingqiu.com')

cat = Sprite(2)

b0 = TK.Button(root.frame_left,text='左区测试按钮\n风火轮编程',command=lambda:cat.bk(10))
b0.pack()

codetext = ScrolledText(master=root.frame_left,bg='white',
                     font=('新宋体',12,'normal'),width=28,height=10)
codetext.tag_configure("sel", background="skyblue")                   # 选择的时候为天蓝色
codetext.configure(undo=True,autoseparators=True, maxundo=-1)         # 让撤销发生作用
codetext.pack(expand=1,fill='both')
codetext.insert(TK.END, 'from turtle import *')

b1 = TK.Button(root.frame_right,text='右测试按钮',command=lambda:cat.fd(10))
b1.pack()

b2 = TK.Button(root.frame_centertop,text='中上区测试按钮',command=lambda:showinfo('中上',''))
b2.pack()

b3 = TK.Button(root.frame_centerbottom,text='中下区测试按钮',command=lambda:showinfo('中下',''))
b3.pack()

screen.mainloop()
