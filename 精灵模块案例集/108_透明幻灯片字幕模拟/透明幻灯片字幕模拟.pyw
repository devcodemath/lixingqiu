"""
   透明幻灯片字幕模拟
"""
from sprites import *

s = '第一课 树立远大的理想'
screen = Screen()
screen.bgcolor('blue')
screen.titlebar(False)
root = screen._root              # 窗口对象
root.wm_attributes('-alpha',0.7) # 设置窗口为全透明(0到1.0)
screen.setup(800,600)

ft = ('楷体',38,'bold')
t = Sprite(visible=False,pos=(-500,0))
t.color('magenta')
clock = Clock()
for x in range(100):
    t.clear()
    t.write(s,align='center',font=ft)
    t.wait()
    t.fd(5)
    clock.tick(60)

m1 = Mouse()          # 鼠标左键
while not m1.down():screen.update()

for x in range(50):
    t.clear()
    t.write(s,align='center',font=ft)
    t.wait()
    t.fd(10)
    clock.tick(60)


screen.bye()
