"""
   虫子画图软件,供Python预备班熟悉海龟画图命令,
   本程序用Python精灵模块开发,需要先在cmd下用命令:
   pip install sprites进行安装。
"""

from sprites import *
from tkinter.scrolledtext import ScrolledText

codes = []                        # 装虫子命令的列表
def init_codes():
    global codes
    codes.clear()
    codes.append('from sprites import * ')
    codes.append('screen = Screen()')
    codes.append('screen.delay(10)')
    codes.append('screen.colormode(255)')
    codes.append('bug = Sprite()')
    
init_codes()                       # 初始化这个列表
DISTANCE = 50                      # 每次前进的距离
ANGLE = 90                         # 每次旋转的角度
SPEED = 2                          # 虫子移动的速度 

sc_width,sc_height = 960,600
screen = Screen()
screen.delay(10)
screen.setup(sc_width,sc_height)
screen.resizable()
screen.colormode(255)
screen.title('Python预备班练习软件非编辑版(虫子画图软件)')
screen.listen()

bug = Sprite()                     # 新建虫子

# 下面的TK来自于从sprites模块导入的TK类 
frameup = TK.Frame(screen._root,bg='#f3f3a3',padx=8,pady=8)
frameup.pack(expand=1,fill='both')

frameup.columnconfigure(0, pad=3)
frameup.columnconfigure(1, pad=3)
frameup.columnconfigure(2, pad=3)
frameup.columnconfigure(3, pad=3)
frameup.columnconfigure(4, pad=3)
frameup.columnconfigure(5, pad=3)
frameup.rowconfigure(0, pad=3)
frameup.rowconfigure(1, pad=3)
frameup.rowconfigure(2, pad=3)
frameup.rowconfigure(3, pad=3)
frameup.rowconfigure(4, pad=3)
frameup.rowconfigure(5, pad=3)

def bughome():
    bug.home()
    command = 'bug.home()'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
b0 = TK.Button(frameup,text='home(回家)',command=bughome)
b0.grid(row=0,column=0,sticky=TK.W)

def bugspeed():
    global SPEED
    b = screen.numinput('请输入虫子移动速度','',minval=0,maxval=10,default=2)
    if b == None:return
    SPEED = int(b)
    bug.speed(SPEED)
    command = 'bug.speed(' + str(SPEED) + ')'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
    
b1 = TK.Button(frameup,text='speed(速度)',command=bugspeed)
b1.grid(row=0,column=1,sticky=TK.W)
    
def bugpendown():
    bug.pd()
    command = 'bug.pendown()'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
b1 = TK.Button(frameup,text='pendown(落笔)',command=bugpendown)
b1.grid(row=1,column=0,sticky=TK.W)


def bugforward():
    bug.fd(DISTANCE)
    command = 'bug.forward(' + str(DISTANCE) + ')'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
    
b2 = TK.Button(frameup,text='forward(前进)',command=bugforward)
b2.grid(row=1,column=1,sticky=TK.W)

def bugbackward():
    bug.bk(DISTANCE)
    command = 'bug.backward(' + str(DISTANCE) + ')'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
b4 = TK.Button(frameup,text='backward(倒退)',command=bugbackward)
b4.grid(row=2,column=0,sticky=TK.W)

def bugright():
    bug.right(ANGLE)
    command = 'bug.right(' + str(ANGLE) + ')'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)    
b5 = TK.Button(frameup,text='right(右转)',command=bugright)
b5.grid(row=2,column=1,sticky=TK.W)

def bugbeginfill():
    bug.begin_fill()
    command = 'bug.begin_fill()'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
b7 = TK.Button(frameup,text='begin_fill(开始填充)',command=bugbeginfill)
b7.grid(row=3,column=0,sticky=TK.W)

def bugleft():
    bug.left(ANGLE)
    command = 'bug.left(' + str(ANGLE) + ')'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
b6 = TK.Button(frameup,text='left(左转)',command=bugleft)
b6.grid(row=3,column=1,sticky=TK.W)


def bugendfill():
    bug.end_fill()
    command = 'bug.end_fill()'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
b8 = TK.Button(frameup,text='end_fill(结束填充)',command=bugendfill)
b8.grid(row=4,column=0,sticky=TK.W)

def bugclear():
    bug.clear()
    command = 'bug.clear()'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
b9 = TK.Button(frameup,text='clear(清空)',command=bugclear)
b9.grid(row=4,column=1,sticky=TK.W)

def bugpenup():
    bug.penup()
    command = 'bug.penup()'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
b3 = TK.Button(frameup,text='penup(抬笔)',command=bugpenup)
b3.grid(row=5,column=0,sticky=TK.W)

def bugsetxy():
    x = screen.numinput('请输入x坐标','',default=bug.xcor())
    if x==None:x = bug.xcor()
    y = screen.numinput('请输入y坐标','',default=bug.xcor())
    if y==None:y = bug.ycor()
    bug.goto(x,y)
    command = 'bug.goto(' + str(x) + ',' + str(y) + ')'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
b3 = TK.Button(frameup,text='goto(定位)',command=bugsetxy)
b3.grid(row=5,column=1,sticky=TK.W)


screen.onkeypress(bugforward,"Up")
screen.onkeypress(bugbackward,"Down")
screen.onkeypress(bugright,"Right")
screen.onkeypress(bugleft,"Left")
screen.onclick(lambda x,y:screen.listen())
options={}
options['filetypes'] = [ ("PNG图像", "*.png"),("JPG图像", "*.jpg"),
                         ("GIF图像", "*.gif"),("所有格式", "*.*") ]
options['defaultextension'] = '.png' if sys.platform == 'darwin' else ''
    
def newpicture():
    """新建"""
    init_codes()
    bug.reset()
    bug.clear()
    screen.bgpic('nopic')
    stext.delete('1.0', TK.END)
    stext.insert(TK.END, "\n".join(codes))
    screen.update()

def backgroundcolor():
    """设定背景颜色"""    
    c = askcolor()
    if c[0]!=None:
        color = list(c[0])
        color1 = [int(c) for c in color]
        color2 = [str(int(c)) for c in color]
        screen.bgcolor(color1)
        command = 'screen.bgcolor(' + ','.join(color2) + ')'
        codes.append(command)
        stext.insert(TK.END, '\n' + command)
    
def openpicture():
    """打开图像(贴背景图)"""
    options['filetypes'] = [ ("PNG图像", "*.png"),("JPG图像", "*.jpg"),
                         ("GIF图像", "*.gif"),("所有格式", "*.*") ]
    options['defaultextension'] = '.png' if sys.platform == 'darwin' else ''
    options['title']='打开图像...'
    filename = askopenfilename(**options)
    #print('filename=',type(filename))
    if filename !="":
        try:
            screen.bgpic(filename)
            screen.title(filename)
        except:
            pass    
    
def savepicture():
    """保存为图像"""
    options['filetypes'] = [ ("PNG图像", "*.png"),("JPG图像", "*.jpg"),
                         ("GIF图像", "*.gif"),("所有格式", "*.*") ]
    options['defaultextension'] = '.png' if sys.platform == 'darwin' else ''
    options['title']='另存为图像...'
    filename = asksaveasfilename(**options)
    if filename=="":return
    for _ in range(10):
        screen.update()
        time.sleep(0.1)
    screen.save(filename)
    command = "screen.save('" + filename + "')"
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
    screen.title(filename)

def savecode():
    """保存代码"""
    string = '\n'.join(codes)    
    options['title']='保存代码...'
    options['filetypes'] = [ ("py源码程序", "*.py"),("txt", "*.txt"),
                             ("pyw源码程序", "*.pyw"),("所有格式", "*.*") ]
    options['defaultextension'] = '.py' if sys.platform == 'darwin' else ''
    filename = asksaveasfilename(**options)
    if filename=="":return
    f = open(filename,mode='w',encoding='utf-8')
    f.write(string)
    f.close()
    screen.title(filename)

def hidebug():
    """隐藏虫子"""
    bug.hide()
    command = 'bug.hide()'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)

def showbug():
    """显示虫子"""
    bug.show()
    command = 'bug.show()'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
    
def setpencolor():
    c = askcolor()    
    if c[0]!=None:
        color = list(c[0])
        color1 = [int(c) for c in color]
        color2 = [str(int(c)) for c in color]
        bug.pencolor(color1)
        command = 'bug.pencolor(' + ','.join(color2) + ')'
        codes.append(command)
        stext.insert(TK.END, '\n' + command)

def setfillcolor():
    c = askcolor()
    if c[0]!=None:
        color = list(c[0])
        color1 = [int(c) for c in color]
        color2 = [str(int(c)) for c in color]
        bug.fillcolor(color1)
        command = 'bug.fillcolor(' + ','.join(color2) + ')'
        codes.append(command)
        stext.insert(TK.END, '\n' + command)
        
def setpensize():
    b = screen.numinput('请输入画笔粗细','',minval=1,maxval=500,default=5)
    if b == None:return
    b = int(b)
    bug.pensize(b)
    command = 'bug.pensize(' + str(b) + ')'
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
    
def setdistance():
    global DISTANCE
    b = screen.numinput('请输入虫子每次前进的距离','',minval=1,maxval=500,default=50)
    if b == None:return
    DISTANCE = b
    
def setangle():
    global ANGLE
    b = screen.numinput('请输入虫子每次旋转的角度','',minval=1,maxval=360,default=90)
    if b == None:return
    ANGLE = b
def directrun():
    command = screen.textinput('请输入命令:','')
    exec(command)
    codes.append(command)
    stext.insert(TK.END, '\n' + command)
    
popup = TK.Menu(screen._root, tearoff=0)
popup.add_command(label="New (新建)" ,command=newpicture)
popup.add_command(label="bgcolor(背景颜色)" ,command=backgroundcolor)
popup.add_command(label="Open(贴背景图)" ,command=openpicture)
popup.add_command(label="Save Image(保存图像)",command=savepicture)

popup.add_command(label="Save Code(保存程序)",command=savecode)
popup.add_separator()
popup.add_command(label="画笔颜色",command=setpencolor)
popup.add_command(label="填充颜色",command=setfillcolor)
popup.add_command(label="画笔粗细",command=setpensize)
popup.add_separator()
popup.add_command(label="每次前进的距离",command=setdistance)
popup.add_command(label="每次旋转的角度",command=setangle)
popup.add_separator()
popup.add_command(label="隐藏虫子",command=hidebug)
popup.add_command(label="显示虫子",command=showbug)
popup.add_command(label="输入命令",command=directrun)
popup.add_separator()
popup.add_command(label="关于本程序",command=lambda:showinfo('关于','本程序由李兴球开发\n\nQQ:406273900\n\nwww.lixingqiu.com'))
popup.add_command(label="打开主页",command=lambda:os.system('explorer http://www.lixingqiu.com'))
popup.add_command(label="退出本程序",command=lambda:screen.bye())

def do_popup(event):
    """显示弹出菜单"""
    try:
        popup.tk_popup(event.x_root, event.y_root + 10, 0)
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        popup.grab_release()

screen.cv.bind("<Button-3>", do_popup)

def txtEvent(event):
    """按ctrl+c可以复制,其它键无效"""
    if(event.state==12 and event.keysym=='c' ):
        return
    else:
        return "break"

framedown = TK.Frame(screen._root,bg='#e3f3f3',padx=4,pady=4)
framedown.pack(side=TK.LEFT)

stext = ScrolledText(master=framedown,bg='white',
                     font=('新宋体',12,'normal'),width=40,height=32)
stext.pack(fill=TK.BOTH, side=TK.LEFT, expand=True)
stext.insert(TK.END, "\n".join(codes))
stext.bind("<Key>", lambda e: txtEvent(e))
screen.mainloop()
