"""
   本程序主要演示explode函数的用法。
   它有三个参数，分别是pos、frames、delay。
   含义为爆炸坐标，爆炸序列图，每帧显示时间。
   在sprites1.40版中，pos也可以是一个Sprite对象。
"""
from sprites import  * 

爆炸图表 = [f'exp/{i}.gif' for i in range(6)]

screen = Screen()               # 新建屏幕对象
screen.bgcolor('black')         # 设定背景颜色

tom = Sprite(visible=False)     # 新建不可见的tom

def bang():
    tom.gotorandom()            # 到随机位置
    explode(tom,爆炸图表)       # 在tom的坐标爆炸
    screen.ontimer(bang,500)    # 500毫秒后再调用 
bang()

screen.mainloop()
