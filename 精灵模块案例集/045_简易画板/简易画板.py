"""
   简易画板.py
   本程序演示了如何取消可拖动。
   当取消了可拖动功能后，可用sprite.ondrag(sprite.drag)，
   或直接执行sprite.drag(0,0)来恢得角色的可拖动功能。
   
"""
from sprites import *

red = Sprite(shape='square',pos=(-300,100))
red.color('red')
red.ondrag(None)

green = Sprite(shape='square',pos=(-300,50))
green.color('green')
green.ondrag(None)

blue = Sprite(shape='square',pos=(-300,0))
blue.color('blue')
blue.ondrag(None)

pen = Sprite(visible=False)# 新建pen角色表示画笔
pen.color('dodger blue')

pen.pensize(10)            # 画笔线宽

m1 = Mouse(1)              # 鼠标左键
m3 = Mouse(3)              # 鼠标右键

while 1:
    x,y = mouse_pos()      # 获取鼠标指针坐标
    x = max(x,-200)
    pen.goto(x,y)
    
    if m1.down():
        if x > -200 :pen.down()
        if red.collide_mouse(): pen.color('red')
        if green.collide_mouse():pen.color('green')
        if blue.collide_mouse():pen.color('blue')
    else:
        pen.up()
    if m3.down():pen.clear()
    
