"""
   雪的梦幻
"""
from sprites import *

# 重定义ScrolledCanvas的初始化方法
def ScrolledCanvas_init(self,master,width=500,height=350,canvwidth=600,canvheight=500):
       """ 把滚动条给去掉了"""
       TK.Frame.__init__(self, master, width=width, height=height)
       self._rootwindow = self.winfo_toplevel()
       self.width, self.height = width, height
       self.canvwidth, self.canvheight = canvwidth, canvheight
       self.bg = "white"
       self._canvas = TK.Canvas(master, width=width, height=height,
                                 bg=self.bg, relief=TK.SUNKEN, borderwidth=2)
       self._canvas.pack(expand=1,fill='both')
       self.reset()
       self._rootwindow.bind('<Configure>', self.onResize)
       
ScrolledCanvas.__init__ = ScrolledCanvas_init

def ScrolledCanvas_reset(self, canvwidth=None, canvheight=None, bg = None):
        """重置画布"""
        if canvwidth:
            self.canvwidth = canvwidth
        if canvheight:
            self.canvheight = canvheight
        if bg:
            self.bg = bg
        self._canvas.config(bg=bg,
                        scrollregion=(-self.canvwidth//2, -self.canvheight//2,
                                       self.canvwidth//2, self.canvheight//2))
        self._canvas.xview_moveto(0.5*(self.canvwidth - self.width + 30) /
                                                               self.canvwidth)
        self._canvas.yview_moveto(0.5*(self.canvheight- self.height + 30) /
                                                              self.canvheight)
ScrolledCanvas.reset = ScrolledCanvas_reset

def ScrolledCanvas_adjustScrolls(self):
        """ 校正画布尺寸
        """
        cwidth = self._canvas.winfo_width()
        cheight = self._canvas.winfo_height()
        self._canvas.xview_moveto(0.5*(self.canvwidth-cwidth)/self.canvwidth)
        self._canvas.yview_moveto(0.5*(self.canvheight-cheight)/self.canvheight)

ScrolledCanvas.adjustScrolls = ScrolledCanvas_adjustScrolls

s = '雪的梦幻'
screen = Screen()
screen.bgcolor('dodger blue')
screen.titlebar(False)
screen.setalpha()

root = screen._root
screen.setup(800,100)
screen.tracer(0,0)
screen.draggable()               # 让窗口可拖动
screen.addpopup()
# 下面的代码按方向箭头则窗口能上下左右移动
screen.onkeypress(lambda:root.move(10),'Right')
screen.onkeypress(lambda:root.move(-10),'Left')
screen.onkeypress(lambda:root.move(0,-10),'Up')
screen.onkeypress(lambda:root.move(0,10),'Down')
screen.listen()

 
ft_context = ('微软雅黑',32,'normal')
t = Sprite(visible=False,pos=(-600,-15))
t.color('red')
clock = Clock()
t.write(s,align='center',font=ft_context)
worditem = t.items[-1]                   # 字的编号
wordbbox = screen.cv.bbox(worditem)      # 字的绑定盒子
wordwidth = wordbbox[-1] - wordbbox[0]   # 字的宽度
def scrolledtext():
    t.clear()
    t.write(s,align='center',font=ft_context)
    t.wait()
    t.fd(2)
    if t.xcor() - wordwidth/2 >300:t.setx(-200-wordwidth/2)
    clock.tick(60)
    if t.xcor()==0:t.wait(1)
    screen.ontimer(scrolledtext,1)
scrolledtext()

# 单击鼠标左键开始往上移
m1 = Mouse()                # 鼠标左键
while not m1.down():screen.update()
for x in range(400):
    root.move(0,-1)
    root.update()
    time.sleep(0.01)
    

print('运行完毕')
    
screen.mainloop() 
