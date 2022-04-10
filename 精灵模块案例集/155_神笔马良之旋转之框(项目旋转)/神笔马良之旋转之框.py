"""
   神笔马良之旋转之框.py
   画一个图形，让它移动或旋转有多种方法，这里提供一个较少见的方法。
   这种方法并不需要擦除原来的图形,再重画,所以效果更好。
   本程序画一个正方形,然后让它旋转起来。
   程序中用到了2D向量操作，并不适合小学生学习,推荐中学以上学生阅读。
   程序中的Vec2D类来自于海龟模块。每个向量都有rotate方法，能让向量旋转。
   通过重新配置item的坐标，所以项目就是旋转了的。
   Vec2D类的详情请打开turtle.py文件查找class Vec2D,找到后阅读源码以更更好理解。
"""
from sprites import *                # 从精灵模块导入所有命令

screen = Screen()                    # 新建屏幕 

bug = Sprite()                       # 新建虫子角色
#bug.goto(100,100)                    # 定位到坐标(100,100)
bug.pensize(20)                      # 画笔尺寸为20
bug.pencolor('red')                  # 画笔颜色为红色

bug.pendown()                        # 落笔
for _ in range(4):                   # 重复4次
    bug.fd(100)                      # 前进150个单位
    bug.wait(0.5)
    bug.rt(90)                       # 右转90度
    bug.wait(0.5)
bug.penup()                          # 抬笔 

center = Vec2D(50,-50)               # 转为2D向量,旋转中心 
frame = bug.items[0]                 # 框的编号(角色移动后形成的项目)
angle = 0                            # 项目旋转的角度
rawpoints = screen._pointlist(frame) # 项目的各个原始坐标列表
while True:    
    points = [Vec2D(*p)- center for p in rawpoints] # 每个点相对于中心点的向量
    points = [p.rotate(angle) for p in points]      # 旋转每个2D向量
    points = [p+center for p in points]             # 恢复每个点的坐标
    angle -= 1                                      # 旋转角度增加1度    
    cl = []                                         # 建空列表cl
    for x, y in points:                             # 每个点
        cl.append(x)
        cl.append(-y)    
    screen.cv.coords(frame, *cl)                    # 重新配置frame各个坐标点
    screen.update()                                 # 更新屏幕显示
    time.sleep(0.01)
