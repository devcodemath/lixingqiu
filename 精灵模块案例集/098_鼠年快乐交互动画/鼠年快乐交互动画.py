"""
   鼠年快乐交互动画,本程序重定义_Root类的__init__,增加了createmenu方法,
   关于Root类,请查看turtle.py文件.
   本程序用Python精灵模块开发,需要先在cmd下用命令:
   pip install sprites进行安装。
   本程序是在分区功能之前制作的,没有用到新版本的屏幕分区功能,
   代码反而把如何进行分区的原理显示出来了。
"""

from sprites import *
from turtle import _Root,ScrolledCanvas
from sprites import _colorlist

# 下面的TK即是tkinter ,从sprites已经导入。分区原理主要是重新定义根类的init方法。
def root__init(self):
    TK.Tk.__init__(self)       # 新建窗口
    # 这个做为背景框架
    self.frame_bg = TK.Frame(self,bg='#e2a2e5',padx=8,pady=8)
    self.frame_bg.pack(expand=1,fill='both')
    
    self.frame_left = TK.Frame(self.frame_bg,bg='#3200f0',padx=8,pady=8)
    self.frame_left.pack(side=TK.LEFT,expand=1,fill='both')
    
    self.frame_right = TK.Frame(self.frame_bg,bg='#00e200',padx=10,pady=10)
    self.frame_right.pack(side=TK.RIGHT,expand=1,fill='both')    
    self.frame_right.rowconfigure(0, pad=10)
    self.frame_right.rowconfigure(1, pad=10)
    self.frame_right.rowconfigure(2, pad=10)
    self.frame_right.rowconfigure(3, pad=10)
    self.frame_right.rowconfigure(4, pad=10)    
    
    self.createmenu()    

def root_createmenu(self):
        
    # 创建一个顶级菜单
    menubar = TK.Menu(self)
     
    # 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
    filemenu = TK.Menu(menubar, tearoff=False)
    filemenu.add_command(label="打开", command=lambda:showinfo('hi',''))
    filemenu.add_command(label="保存", command=lambda:showinfo('hi',''))
    filemenu.add_separator()
    filemenu.add_command(label="关于", command=lambda:showinfo('www.lixingqiu.com','本程序基于Python海龟画图'))
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
screen.setup(400,640)
screen.colormode(255)
root = screen._root
screen.title('鼠年快乐交互动画 by 李兴球  www.lixingqiu.com')

frames = ['res/rat1.png','res/rat2.png']
mouse = Sprite(4)
mouse.saycolor('red')
mouse.saybordercolor('yellow')
mouse.left(90)
mouse.play('步步高古筝.wav')
def alt_costume():
    mouse.nextcostume()    
    screen.ontimer(alt_costume,100)
alt_costume()

def runcode():
    """运行mouse的代码"""
    
    b0.config(state='disabled')
    root.frame_right.pack_forget()
    screen.bgpic('bg.png')
    heng = 'Python'    
    [txt2image(char,f'res/heng_{char}.png',fontsize=30,color=(250,12,33)) for char in heng]
    hengimage = [f'res/heng_{char}.png' for char in heng]   
    mouse.left(45)
    mouse.glide((-100,180),200)
    rat_group = Group('rat')
    for char in hengimage:
        Sprite(shape=char,pos=mouse.pos(),tag='rat')  
        mouse.addx(30)
        mouse.right(15)
        mouse.wait(0.1)
    left = '学编程利国利民'    
    for char in hengimage:
        mouse.addx(-35)
        mouse.addy(-10)
        mouse.left(9)
        mouse.wait(0.1)
    [txt2image(char,f'res/left_{char}.png',fontsize=30,color=(250,212,33)) for char in left]
    leftimage = [f'res/left_{char}.png' for char in left]
    for char in leftimage:
       Sprite(shape=char,pos=mouse.pos(),tag='rat')  
       mouse.addy(-40)
       mouse.wait(0.1)
    for char in leftimage:
       mouse.addy(40)
       mouse.wait(0.1)
    mouse.glide((100,120),200)
    
    right = '写代码走遍天下'    
    [txt2image(char,f'res/right_{char}.png',fontsize=30,color=(50,12,233)) for char in right]
    rightimage = [f'res/right_{char}.png' for char in right]
    for char in rightimage:
       Sprite(shape=char,pos=mouse.pos(),tag='rat')  
       mouse.addy(-40)
       mouse.wait(0.1)
       
    mouse.color('orange')
    mouse.slide((0,-230),1000)
    mouse.write('新年大礼到啦。\n基于Python海龟画图的100个Python创意程序\nsprites版在本人博客免费下载啦',align='center',font=('微软雅黑',12,'normal'))
    mouse.setheading(90)
    mouse.slide((0,0),3000)
    mouse.saycolor('yellow')
    mouse.saybordercolor((166,166,166))
    mouse.say("祝你鼠年快乐",1000,False)
    mouse.wait(2)
    while True:
        for rat in rat_group:
            rat.rt(5)
       
    
    
b0 = TK.Button(root.frame_left,text='\n 运行程序 \n',command=runcode)
b0.pack()

b1 = TK.Button(root.frame_right,text='祝大家鼠年快乐',command=lambda:mouse.say('祝大家鼠年快乐'))
b1.grid(row=0,column=0)

b2 = TK.Button(root.frame_right,text='来年平安,幸福',command=lambda:mouse.say('来年平安,幸福'))
b2.grid(row=1,column=0)

b3 = TK.Button(root.frame_right,text='左转',command=lambda:mouse.left(30))
b3.grid(row=2,column=0)

b4 = TK.Button(root.frame_right,text='右转',command=lambda:mouse.right(30))
b4.grid(row=3,column=0)

b4 = TK.Button(root.frame_right,text='背景颜色',command=lambda:screen.bgcolor(random.choice(_colorlist)))
b4.grid(row=4,column=0)

# 下面的TK是就是tkinter
popup = TK.Menu(screen._root.frame_left, tearoff=0)
popup.add_command(label="大家好",command=lambda:showinfo('hi','这是真的'))
popup.add_command(label="今天很",command=lambda:showinfo('hi','这是真的'))
popup.add_command(label="高兴能",command=lambda:showinfo('hi','这是真的'))
popup.add_command(label="够在网",command=lambda:showinfo('hi','这是真的'))
popup.add_command(label="上直播",command=lambda:showinfo('hi','这是真的'))
popup.add_command(label=",下次",command=lambda:showinfo('hi','这是真的'))
popup.add_command(label="再风",command=lambda:showinfo('hi','这是真的'))
popup.add_command(label="拜拜。",command=lambda:screen.bye())


def do_popup(event):
    """显示弹出菜单"""
    try:
        popup.tk_popup(event.x_root, event.y_root + 10, 0)
    finally:
        # 确保释放按键
        popup.grab_release()

screen.cv.bind("<Button-3>", do_popup)   # 画布绑定鼠标右键

screen.mainloop()
