"""旋转而去的一字.py"""

from turtle import *               # 从海龟画图模块导入所有命令
from time import sleep             # 从时间模块导入sleep

screen = Screen()                  # 新建屏幕对象
screen.title("旋转而去的一字.py")  # 设置标题
 
t = Turtle()                       # 新建海龟对象
t.begin_poly()                     # 开始记录顶点
t.bk(100)                          # 倒退100个单位
t.fd(200)                          # 前进200个单位
t.end_poly()                       # 结束记录顶点
p = t.get_poly()                   # 得到刚才所画新形状的顶点坐标
screen.addshape("line",p)          # 添加新形状名为line
sleep(2)                           # 延时2秒
t.shape("line")                    # 设定海龟的形状为line
t.clear()
t.penup()                          # 抬笔
sleep(2)                           # 延时2秒
while True:                        # 无限循环
    t.setx(t.xcor() + 2)           # 海龟的x坐标加2
    t.rt(10)                       # 右转10度
