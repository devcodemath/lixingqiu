"""
   矩形重叠演示程序.py
   本程序演示两个矩形重叠区域，会把它们画出来。
"""
from sprites import *

screen = Screen()
screen.title('矩形重叠演示程序')

bug = Sprite('blue.png')                # 这个角色计划用鼠标指针操作
bug2 = Sprite('blue.png')               # bug2是中间不动的方块
bug2.scale(2)                           # 把bug2的比例增大
bbox2 = bug2.bbox()                     # 获取bug2的绑定盒 

hider = Sprite(visible=False)           #  hider角色用来画相交矩形
hider.color('brown','yellow')           # 角色的画笔和填充颜色（边框和内部颜色)
hider.pensize(2)                        # 角色的画笔粗细

while True:
    bug.goto(mouse_pos())                 
    bbox1= bug.bbox()
    r = rect_overlap(bbox1,bbox2)
    if r:
      hider.clear()
      left,top,right,bottom = r[:-1]
      hider.goto(left,top)
      hider.pendown()
      hider.goto(right,top)
      hider.goto(right,bottom)
      hider.goto(left,bottom)
      hider.goto(left,top)
      hider.up()
      hider.update() 
      time.sleep(0.1)
    screen.update()
