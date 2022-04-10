"""
  保卫地球收集垃圾.py
  请自行设计游戏逻辑!
  本程序只是演示相关命令的用法,用于抛砖引玉

"""
from sprites import *
from random import randint

wastes = ["坏电视","旧纸盒","塑料瓶","网线","干电池",'破汗衫',
          "坏插座", "指甲油", "药瓶", "玉米棒", "鸡蛋壳", '纸牌',
          "玻璃块","鱼骨头", "旧书", "卫生巾", "快餐盒",'木柴']

# 把文本转换成图像存放在res文件夹中
[txt2image(txt,f'res/{txt}.png') for txt in wastes]

screen = Screen()
screen.setup(800,600)
screen.bgcolor('light cyan')

waste_sprites = [Sprite(f'res/{txt}.png',
pos=(randint(-350,350),randint(300,900))) for txt in wastes]

dummy = Sprite(visible=False)
dummy.goto(-400,-300+100)
dummy.fillcolor('green')
dummy.begin_fill()
for _ in range(4):
    dummy.fd(800)
    dummy.right(90)
    dummy.fd(100)
    dummy.right(90)
dummy.end_fill()

dummy.goto(-100,50)
dummy.left(90)            # 向左转90度
dummy.shape('triangle')   # 切换到三角形造型
dummy.color('green')
for _ in range(5,9):
    dummy.shapesize(_)    # 造型大小
    dummy.stamp()         # 图章
    dummy.bk(40)          # 倒退
dummy.pendown()
dummy.ht()                # 隐藏
dummy.pensize(13)         # 画笔线宽
dummy.fd(-100)


g = Sprite(shape='垃圾桶.png')
g.sety(-200)
 
while True:
    mx,my = mouse_pos()
    g.setx(mx)
    for w in waste_sprites:
        w.addy(-1)
        if w.ycor()<-300 or w.collide(g):
           w.goto(randint(-350,350),randint(300,900))
