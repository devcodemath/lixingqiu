"""
   五彩缤纷.py
"""

from sprites import Sprite

hg = Sprite(shape='circle')
hg.scale(3) 
hg.screen.bgcolor('black')
hg.screen.title('五彩缤纷')

while 1:
    hg.randomcolor()       # 随机颜色
    hg.randompos()         # 到随机位置
    hg.stamp()             # 盖图章    
    hg.wait(0.3)           # 等待0.3秒
