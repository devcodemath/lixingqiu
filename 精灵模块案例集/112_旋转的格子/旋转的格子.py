"""
   旋转的格子
"""

from sprites import *                   # 从精灵模块导入所有命令

screen = Screen()                       # 新建屏幕对象
screen.tracer(0,0)
t = Sprite(visible=False)               # 新建角色
t.pensize(4)                            # 画笔粗细为4

clock = Clock()
while True:
   t.clear()                            # 清空所画   
   cors = t.draw_grid3(4,4,100,100,True)# 画4x4格子,宽度都为100,且盖图章
   t.update()
   t.right(1)
   clock.tick(60)
