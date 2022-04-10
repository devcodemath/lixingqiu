"""
   朝向鼠标指针移动.py
"""

from sprites import Sprite,mouse_pos

bug = Sprite()
bug.screen.bgcolor('cyan')

while 1:
    mp = mouse_pos()
    bug.heading(mp)
    if bug.distance(mp) > 10:bug.fd(1)
