"""
   圆圆的笑脸.py
   本程序演示写字命令的angle参数。
"""
from sprites import Sprite

g = Sprite(visible=False)
g.screen.tracer(0,0)
a = 0
while True:
    g.clear()
    a += 0.2
    a %= 360
    g.write(chr(9786),align='center',font=('',100,'normal'),angle=a)
