"""
   18角星.py
"""
# 从海龟模块导入Turtle,Screen命令
from turtle import Turtle,Screen

s = Screen()                # 新建屏幕
s.bgcolor('light green')    # 设定屏幕背景色
s.title('18角星')           # 设定窗口标题

t = Turtle(shape='turtle')  # 新建造型为turtle的海龟
t.color('blue')             # 设定海龟颜色为蓝色
t.pensize(2)                # 设定画笔尺寸为2

for x in range(18):         # 在范围18内迭代x的值
    t.fd(100)               # 海龟前进100个单位
    t.right(170)            # 海龟右转170度
    t.fd(100)               # 海龟前进100个单位
    t.left(150)             # 海龟左转150度

t.hideturtle()              # 隐藏海龟
s.mainloop()                # 进入主事件循环
