"""
   可拖动的精灵,请用鼠标去拖动各个角色。
"""

from sprites import *    # 从精灵模块导入所有命令

for  i in range(16):     # 重复16次
    sp = Sprite(i)       # 根据编号i生成精灵
    sp.randomposition()  # 随机坐标
    sp.say(str(i),delay=1000,wait=False)

sp.screen.mainloop()     # 进入主循环
    
