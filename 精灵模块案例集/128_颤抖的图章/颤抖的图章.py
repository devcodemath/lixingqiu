"""
   颤抖的图章,本程序主要学习角色有一个叫stampItems列表。
   这个列表存储的是角色所盖的所有图章的编号。
   图章也是可以移动的。图章的坐标是可以获取到的。
"""
from sprites import *                # 从精灵模块导入所有命令
from random import choice            # 从随机模块导入choice命令 

screen = Screen()                    # 新建屏幕
screen.bgcolor('black')              # 设定屏幕为黑色
screen.setup(800,600)                # 设定宽高为800x600

speed = [-5,-4,-3,-2,-1,1,2,3,4,5]   # 定义一个叫speed的列表

p = Sprite(shape='dot',visible=False)# 生成不可见角色,造型为dot
p.color('cyan')                      # 设定角色颜色

while True:                          # 当成立的时候
    if len(p.stampItems)<500:        # 如果p的图章数量小于500
       p.stamp()                     # 则盖一个图章
    for i in p.stampItems:           # 对于每一个图章(编号) 
        dx = choice(speed)           # 随机挑选一个数据赋值给dx
        dy = choice(speed)           # 随机挑选一个数据赋值给dy
        p.movestamp(i,dx,dy)         # 在水平和垂直方向上移动编号为i的图章
        x,y = p.stampcors(i)         # 获取图章i的x,y坐标
        if abs(x)>400 or abs(y)>300: # 如果x的绝对值大于400或者y的绝对值大于300
            p.stampgoto(i,0,0)       # 则把图章移到原点
    screen.update()                  # 刷新屏幕显示
    screen.title(len(p.stampItems))  # 在标题栏里显示图章数量
                            
