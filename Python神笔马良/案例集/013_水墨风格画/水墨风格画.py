"""
   水墨风格画.py
"""
import turtle              # 导入海龟模块

turtle.penup()             # 抬笔 
turtle.goto(-200,-200)     # 坐标定位

turtle.pendown()           # 落笔
for s in range(1,20):      # 在范围1,20内更新s
    turtle.pensize(s)
    turtle.fd(s/4)
    turtle.right(1)

for s in range(20,40):     # 在范围20,40内更新s
    turtle.pensize(s)
    turtle.fd(s/4)
    turtle.left(1)
    
for s in range(40,60):     # 在范围40,60内更新s
    turtle.pensize(s)
    turtle.fd(s/4)
    turtle.left(8)

for s in range(60,90):    # 在范围60,90内更新s
    turtle.pensize(s)
    turtle.fd(s/4)
    turtle.rt(8)

turtle.done()             # 进入事件循环
