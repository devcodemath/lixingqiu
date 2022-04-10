"""
   draw_grid2演示，本程序会画一个4X4的格子，然后小虫子会在每个格子中心点打蓝点。
"""

from sprites import *               # 从精灵模块导入所有命令 

s = Sprite()                        # 新建一个角色
s.wait(3)
cors = s.draw_grid2(4,4,100,100)    # 画4X4格子，长宽都是100
for rows in cors:                   # 每一行的坐标
    for xy in rows:                # 行中的每一个坐标
        s.goto(xy)                  # 角色达到坐标点
        s.dot(10,'blue')            # 角色打蓝点
        s.wait(0.1)                 # 等待0.1秒
    s.home()                        # 回到中心点

s.screen.mainloop()
