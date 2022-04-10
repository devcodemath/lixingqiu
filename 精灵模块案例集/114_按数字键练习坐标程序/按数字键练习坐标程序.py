"""

   按数字键练习坐标程序.py
   演示用的一个程序,本程序需要sprites模块支持,如果无法运行,
   请先在cmd窗口下输入 pip install sprites安装这个模块。
   操作方法：按从1到9和a的键让海龟移到相应的坐标。
   鼠标左键可以直接拖动海龟，鼠标右键可以拖动窗体。按空格结束。
"""

from sprites import *

screen = Screen()
screen.setup(480,360)
screen.bgpic('xy-grid.png')
screen.titlebar(False)
root = screen._root
root.wm_attributes('-alpha',0.9) # 设置窗口为全透明(0到1.0)

# 下面的代码让窗口可以拖动.
oldx = 0
oldy = 0
def startmove(event):
    global oldx,oldy
    oldx = event.x
    oldy = event.y
def stopmove(event):
    global oldx,oldy
    oldx = 0
    oldy = 0        
def movewindow(event):
    global oldx,oldy     
    dx = event.x - oldx
    dy = event.y - oldy
    root.move(dx,dy)
screen.cv.bind("<ButtonPress-3>", startmove)
screen.cv.bind("<ButtonRelease-3>", stopmove)
screen.cv.bind("<B3-Motion>",movewindow)

t = Sprite(shape='turtle') # Turtle
t.color('red')

def go1():
    cor = (100,100)
    t.goto(cor)
    screen.title(str(cor))    
screen.onkeypress(go1,'1')

def go2():
    cor = (-100,100)
    t.goto(cor)
    screen.title(str(cor))    
screen.onkeypress(go2,'2')

def go3():
    cor = (-100,-100)
    t.goto(cor)
    screen.title(str(cor))    
screen.onkeypress(go3,'3')

def go4():
    cor = (100,-100)
    t.goto(cor)
    screen.title(str(cor))    
screen.onkeypress(go4,'4')

def go5():
    cor = (200,100)
    t.goto(cor)
    screen.title(str(cor))    
screen.onkeypress(go5,'5')

def go6():
    cor = (-200,100)
    t.goto(cor)
    screen.title(str(cor))    
screen.onkeypress(go6,'6')

def go7():
    cor = (-200,0)
    t.goto(cor)
    screen.title(str(cor))    
screen.onkeypress(go7,'7')

def go8():
    cor = (-200,-100)
    t.goto(cor)
    screen.title(str(cor))    
screen.onkeypress(go8,'8')

def go9():
    cor = (200,-100)
    t.goto(cor)
    screen.title(str(cor))    
screen.onkeypress(go9,'9')

def go10():
    cor = (200,0)
    t.goto(cor)
    screen.title(str(cor))    
screen.onkeypress(go10,'a')
    
screen.onkeypress(lambda:screen.bye(),'space')

screen.listen()
screen.mainloop()
