"""
   自定义十字架造型
   本程序自定义一个叫十字架的造型给角色使用。
"""
from sprites import *

screen = Screen()             # 新建屏幕
sp = screen.getshapes()       # 得到造型列表 
print(sp)                     # 打印造型列表

sq = Sprite(shape='square')   # 新建形状为square的角色
sq.pendown()

sq.begin_poly()               # 开始记录顶点    1
for _ in range(4):
    sq.fd(100)
    sq.bk(100)
    sq.right(90)
sq.end_poly()                 # 结束记录顶点    2
p = sq.get_poly()             # 得到顶点坐标，由坐标组成的元组   3
print(p)
screen.addshape('cross',p)    # 取名为cross,添加造型到形状列表 4
sq.shape('cross')             # 把sp的造型设为cross


