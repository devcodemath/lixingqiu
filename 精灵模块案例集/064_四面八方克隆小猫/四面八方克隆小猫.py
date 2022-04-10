"""
   四面八方克隆小猫(remove命令用法)
"""
import random
from sprites import Sprite

cat = Sprite(3)                    # 新建小猫
screen = cat.getscreen()           # 获取屏幕
cats = []                          # 猫列表 

while True:                        # 当成立的时候
    if random.randint(0,20)==0:
        c = cat.clone()
        c.randomheading()
        cats.append(c)
    for c in cats:
       c.fd(10)
       if c.collide_edge():
          c.remove()               # 这是把小猫从屏幕上彻底删除
          cats.remove(c)           # 这是把小猫从cats列表删除
    screen.update()
    screen.title(len(screen.cv.find_all()))
