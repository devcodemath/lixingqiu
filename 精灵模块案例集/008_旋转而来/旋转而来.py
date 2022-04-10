"""
   旋转而来,旋转而去
"""

from sprites import *

s = 0.1
t = Sprite(visible=False)
t.screen.bgcolor('yellow')
t.scale(0.1)

t.show()
for x in range(12):
    s += 1
    t.right(30)
    t.scale(s)
    
for x in range(12,0,-1):
    s -= 1
    t.right(30)
    t.scale(s)

t.screen.mainloop()
