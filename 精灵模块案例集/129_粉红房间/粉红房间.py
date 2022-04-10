"""
   粉红房间.py
   本程序主要理解lambda表达式能建立匿名函数
"""
from sprites import *

screen = Screen()                      # 新建屏幕
screen.setup(480,360)                  # 设定屏幕宽高
screen.bgpic('room.png')               # 贴上背景图
screen.draggable()                     # 按中键可拖动窗口
screen.titlebar(False)                 # 去除标题栏
screen.addpopup()                      # 增加右键菜单

PlaySound('动感活力小清新.wav',SND_ASYNC|SND_LOOP)

w = Sprite(visible=False)
w.goto(0,70)
w.color('cyan')
w.write('寻找垃圾,单击它',align='center')

z = Sprite(shape='images/垃圾娄.png')
z.goto(-200,-140)

a = Sprite(shape='images/蛋壳.png')
a.goto(0,-150)
a.onclick(lambda x,y:a.slide((-200,-130)))# 当a角色被单击时调用一个函数

b = Sprite(shape='images/核.png')
b.goto(208,-171)
b.onclick(lambda x,y:b.slide((-210,-160)))

c = Sprite(shape='images/核2.png')
c.goto(188,-94)
c.onclick(lambda x,y:c.slide((-205,-140)))

d = Sprite(shape='images/废纸2.png')
d.goto(-125,-76)
d.onclick(lambda x,y:d.slide((-195,-150)))

screen.mainloop()
