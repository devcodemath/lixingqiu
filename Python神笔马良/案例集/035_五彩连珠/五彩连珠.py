"""
   五彩连珠.py
"""
import turtle

# 定义颜色表叫cs
cs = ['red','orange','yellow','green','cyan']
print(turtle.getscreen().getshapes())
turtle.bgcolor('black')           # 设置背景颜色

turtle.shape('circle')            # 设定造型为圆形
turtle.shapesize(0.4)             # 设置造型比例
turtle.goto(-50,150)              # 坐标定位到(-50,150)

for _ in range(10):              
    for i in range(5):            # 在范围5内迭代i
        turtle.color('gray')      # 设定画笔颜色为灰色
        turtle.fd(20)             # 前进20个单位
        # 从颜色表中取索引为i的颜色，再设为海龟的颜色
        turtle.color(cs[i])       
        turtle.stamp()            # 盖图章
    turtle.rt(36)                 # 右转36度 
    
turtle.done()                     # 事件循环
