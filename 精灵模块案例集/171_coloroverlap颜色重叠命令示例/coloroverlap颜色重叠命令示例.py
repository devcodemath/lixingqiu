"""
   coloroverlap颜色重叠命令示例.py
   本程序演示角色的某种颜色和其它角色的某种颜色是否重叠,
   注意,本程序只对其它角色的颜色检测有效,对背景色/背景图/图章/角色所画的图的颜色检测无效。
   
"""
from sprites import *

ft = ('宋体',24,'normal')
screen = Screen()
screen.title('颜色重叠演示程序')

w = Sprite(visible=False,pos=(0,200)) # 用来写字的角色
           
blue = Sprite('blue.png')             # 中间的蓝色方块
r1 = Sprite('p1.png',pos=(100,100))   # 右上角的十字架
r2 = Sprite('p2.png')                 # 随鼠标移动的十字架

c1 = (0,255,255)                      # 代表青色
c2 = (0,0,255)                        # 代表蓝色
clock = Clock()                       # 时钟对象

while 1:   
    r2.goto(mouse_pos())              # r2跟随鼠标移动  
    point = r2.coloroverlap(c1,c2)    # r2的青色和某角色的蓝色重叠
    if point:                         # 如果两色重叠，则显示碰撞点
       w.clear()
       screen.title(point)
       w.write('青色碰到了蓝色' + str(point),align='center',font=ft)
    else:
       screen.title('')               # 否则在屏幕标题栏显示空字符串
       w.clear()
    clock.tick(60)

