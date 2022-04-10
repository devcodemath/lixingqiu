"""
  可移动的图章
"""

from sprites import Sprite

b = Sprite(6)                 # 蝴蝶
b.say('我是真的蝴蝶',delay=1000,wait=False)
item = b.stamp()
print("图章编号:",item)

for x in range(2000):              
    b.stampmove(item,0.1,0.1) # 让图章往右上角移动
    b.screen.update()         # 更新屏幕显示
    b.wait(0.01)              # 等待0.01秒
    
