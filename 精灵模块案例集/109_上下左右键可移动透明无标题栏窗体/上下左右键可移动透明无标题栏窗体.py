"""
   上下左右键可移动透明无标题栏窗体.py
   请按上下左右键移动这个窗体。
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
screen.bgcolor('dodger blue')

root = screen._root
root.wm_attributes('-alpha',0.7) # 设置窗口为全透明(0到1.0)
root.goto(0,0)                   # 定位窗体到左上角
time.sleep(1)

# 不断定位窗体的坐标到(c,c)
for c in range(0,200):
    root.goto(c,c)               # 定位到(c,c)坐标。
    root.update() 
    time.sleep(0.01)
    
bug = Sprite(visible=False)
ft = ('',18,'bold')
bug.write('请按上下左右方向箭头移动窗体',align='center',font=ft)

screen.onkeypress(lambda:root.move(10),'Right')
screen.onkeypress(lambda:root.move(-10),'Left')
screen.onkeypress(lambda:root.move(0,-10),'Up')
screen.onkeypress(lambda:root.move(0,10),'Down')
screen.listen()
screen.mainloop()

