"""
   内接正多边形演示动画
"""
from sprites import *

def draw_poly(obj,points):
    obj.goto(points[0])
    obj.pendown()
    for point in points[1:]:
        obj.goto(point)
    obj.goto(points[0])
    obj.penup()       

radius = 200            # 半径
x0,y0 = 0,0             # 圆心
vertexs = [ ]           # 顶点列表

for n in range(3,11):   # 从三角形到10边形
    vs = []
    angle = 90
    for _ in range(n):        
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        vs.append((x,y))
        angle = angle + 360/n
    vertexs.append(vs)
print(vertexs)
screen = Screen()       # 新建屏幕

s = Sprite()
s.pensize(5)
s.color('red')
s.setheading(90)

while True:

    for vers in vertexs:
        s.clear()
        draw_poly(s,vers)
        s.wait(1)

