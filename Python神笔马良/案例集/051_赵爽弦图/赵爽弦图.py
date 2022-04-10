"""
   赵爽弦图.py
   本程序演录了如何自定义形状，如何把它添加到造型字典。
   赵爽弦图是用来证明勾股定理的一张图。
   在图中，四个三角形的面积加上中间小正方形的面积等于最大正方形的面积。
   由此即可证明勾股定理。
"""
from turtle import Turtle,Screen

a = 300/2                   # 三角形底边(勾)
b = 400/2                   # 三角形垂直边(股)
d = b - a                   # 移动的距离

screen = Screen()
screen.delay(20)            # 绘画延时设为20毫秒

tom = Turtle(shape='blank')
tom.pensize(2)              # 设定画笔粗细
tom.speed(1)                # 移动速度为最慢 
tom.begin_poly()            # 开始记录顶点
tom.goto(-a,0)
tom.goto(0,b)
tom.goto(0,0)
tom.end_poly()              # 结束记录顶点 
p = tom.get_poly()          # 获取各顶点
screen.addshape('sj',p)     # 注册到造型字典

tom.shape('sj')             # 设定造型为sj
tom.color('red','yellow')
tom.left(90)

for _ in range(4):
    tom.stamp()             # 盖图章
    tom.fd(d)               # 前进d
    tom.right(90)           # 右转90度 

tom.speed(0)                # 移动速度为最快 
screen.delay(0)             # 绘画延时为0毫妙
tom.penup()                 # 抬笔
tom.ondrag(tom.goto)        # 设定拖放事件  
screen.mainloop()           # 事件循环
