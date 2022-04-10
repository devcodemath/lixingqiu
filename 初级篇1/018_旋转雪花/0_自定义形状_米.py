from turtle import *

width,height = 480,360       # 定义宽和高

screen = Screen()            # 新建屏幕
screen.setup(width,height)   # 设定屏幕宽和高

t = Turtle()                 # 新建海龟为t
t.begin_poly()               # 开始记录顶点
for i in range(8):           # 迭代i八次
    t.fd(20)                 # 前进20个单位
    t.bk(20)                 # 倒退20个单位
    t.rt(45)                 # 右转45度
t.end_poly()                 # 结束记录顶点

p = t.get_poly()             # 获取所记录的顶点元组
print(p)
print(screen.getshapes())    # 打印当前所有形状
screen.addshape("mi",p)      # 注册p为的形状为mi
print(screen.getshapes())
t.clear()                    # 清除t所画的
t.shape("mi")                # 把t的形状设为mi
while True:                  # 永远执行
    t.rt(1)                  # 旋转1度
print("这里永远不会打印.")
