"""
   八圆围正方.py
"""
from turtle import Turtle  # 从海龟模块导入Turtle命令


# 新建造型为Turtle的隐藏海龟
tom = Turtle(shape='turtle',visible=False)
tom.screen.delay(30)
tom.pensize(2)
tom.speed(1)
for _ in range(4):
    tom.fd(50)             # 前进50个单位
    tom.circle(20)         # 转了一圈又回来
    tom.fd(50)
    tom.circle(20)         # 画一个半径为20的圆
    tom.fd(50)
    tom.rt(90)             # 右转90度
    
tom.screen.mainloop()
