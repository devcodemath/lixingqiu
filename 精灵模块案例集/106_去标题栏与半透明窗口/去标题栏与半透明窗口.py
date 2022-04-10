"""
   去标题栏与半透明窗口.py
   本程序演示如何去掉标题栏以及如何获取root,以及窗口为半透明。
   需要sprites的V2.0以上版本才会有titlebar命令。
   
"""
   
from sprites import *

screen = Screen()
screen.titlebar(False)           # 设定标题栏为假(关掉)
screen.setup(480,360)     
screen.bgpic('res/sky.png')

root = screen._root              # 窗口对象
root.wm_attributes('-alpha',0)   # 设置窗口为全透明(0到1.0)
screen.delay(10)                 # 绘画延时为10毫秒

bug = Sprite()
bug.color('red')
bug.pensize(10)
for s in range(1,61):
   root.wm_attributes('-alpha',s/100)
   root.update()
   time.sleep(0.1)       
bug.speed(1)
bug.pendown()    
while True:
  bug.fd(100)
  bug.rt(90)
