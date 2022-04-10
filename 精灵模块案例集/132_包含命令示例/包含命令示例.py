"""
   包含命令示例.py
"""
from sprites import *

screen = Screen()

bug = Sprite()                 # 新建虫子
bug.dot()                      # 虫子打点
bug.goto(100,100)
bug.dot()
bug.goto(110,100)
bug.dot()

while True:
    bug.goto(mouse_pos())
    items = bug.contained()
    print(items)
