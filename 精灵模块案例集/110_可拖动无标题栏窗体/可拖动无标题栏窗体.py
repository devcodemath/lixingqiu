"""
   可拖动无标题栏窗体.py
   请按下鼠标中键移动这个窗体。
   屏幕的root是tkinter的窗体的一个子类，类名为_Root
   本程序使用重定义了的_Root类。在sprites模块中给它增加了move方法，
   它能让窗体相对移动，定义原形为：move(self,dx,dy)。
   还有goto方法，让窗体定位到桌面上的某个坐标。
   还有position方法，获取窗体在桌面中的坐标。
   注意桌面的坐标系为右下为正。spritesV1.22版本以上适用!
"""
from sprites import *

screen = Screen()
screen.titlebar(0)               # 去除标题栏
screen.setup(480,360)     
screen.bgcolor('lime')

root = screen._root
root.wm_attributes('-alpha',0.7) # 设置窗口为全透明(0到1.0)

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
screen.cv.bind("<ButtonPress-2>", startmove)
screen.cv.bind("<ButtonRelease-2>", stopmove)
screen.cv.bind("<B2-Motion>",movewindow)

bug = Sprite(visible=False)
ft = ('',18,'bold')
bug.write('请按下鼠标中键移动这个窗体',align='center',font=ft)

screen.mainloop()

