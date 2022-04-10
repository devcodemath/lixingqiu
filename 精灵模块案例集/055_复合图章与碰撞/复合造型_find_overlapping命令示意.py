"""
   复合造型_find_overlapping命令示意.py
"""
from sprites import *

width,height = 480,360
screen = Screen()
screen.setup(width,height)
screen.bgpic('res/sky.png')

s = Shape("compound")                       # 新建复合类型的造型
tx = [(-10,10),(10,10),(20,-10),(-20,-10)]  # 第一个多边形
s.addcomponent(tx, "red", "blue")           # 加到造型里，填充为红边为蓝
sq = [(-10,20),(10,20),(10,10),(-10,10)]    # 第二个造型
s.addcomponent(sq,"blue",'brown')           # 填充为蓝边为棕
screen.addshape('poly',s)                   # 注册到造型字典

s = Sprite(shape='poly',visible=False)      # 角色本身是隐藏的
s.left(90)                                  # 左转90度
s.pensize(30)
s.color('blue')
s.pendown()
for _ in range(30):
    s.fd(13)
    s.rt(12)
s.color('green')
s.penup()
s.goto(-100,-100)
s.pendown()
s.circle(100)
s.penup()
s.goto(-100,100)
i = s.stamp()
s.goto(150,150)
s.stamp()
s.color('red')
s.goto(100,100)
s.pensize(15)
s.pendown()
s.fd(25)
s.penup()
s.color('blue')
s.write('风花雪月')
# 找所有可用于碰撞检测的items,背景与说话泡泡不参与碰撞检测
p =  screen._finditems()
bug = Sprite()                              # 新建虫子
while True:
    bug.goto(mouse_pos())
    t =  bug.find_overlapping()             # 查找其它item,有无和bug进行矩形重叠
    if t:print(t)                           # 如果有重叠，则输出这个集合
