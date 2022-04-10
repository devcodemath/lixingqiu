"""
   强大的多边形命令.py
   本命令为精灵模块1.33版支持。
   角色的多边形命令支持按坐标点画多边形，也支持根据边数和边长与角色方向画正多边形。
   本程序运行后，所有多边形会绕原点旋转。
"""
from sprites import *

screen = Screen()
screen.bgcolor('black')

bug = Sprite()                                        
x,y = bug.pos()
# 下面是指定多边形的其它顶点画多边形
cors = [(x+100,y),(x+100,y+100)]
p1 = bug.polygon(cors,10,'red','green') # 第一个顶点是角色的坐标,10是线宽
print('这个多边形项目编号为',p1)

# 下面都是画正多边形
bug.goto(-100,100)
bug.color('red','yellow')               # 设置画笔颜色为红,填充颜色为黄
p2 = bug.polygon(4,100)                 # 画正方形

bug.pensize(10)                         # 画笔粗细
bug.goto(-200,-200)                     # 定位到坐标
bug.color('blue','cyan')
p3 = bug.polygon(5,150)                 # 画正五边形,边长为150

bug.goto(200,-200)                      # 坐标定位到(200,-200)
bug.color('','magenta')                 # 画笔颜色为空,则为透明
p4 = bug.polygon((8,80))                # 所以这个8边形没有边框颜色 

bug.goto(200,200)                       # 坐标定位到(200,-200)
bug.randomcolor()                       # 随机一种颜色
bug.left(45)                            # 左转45度
# 不加参数画边数为3-12,边长为10-50的倾斜度为角色方向的随机正多边形
p5 = bug.polygon()

# 下面的代码是让画的多边形们绕中心点旋转
bug.home()
ps = [p1,p2,p3,p4,p5]
center = Vec2D(0,-0)                   # 转为2D向量,旋转中心 
angle = 0                              # 项目旋转的角度
#各个项目的各个原始坐标列表
rawpoints = [screen._pointlist(p) for p in ps]
while True:
    bug.setheading(angle)
    for index in range(len(ps)):
        points = [Vec2D(*p)- center for p in rawpoints[index]] 
        points = [p.rotate(angle) for p in points]      # 旋转每个2D向量
        points = [p+center for p in points]             # 恢复每个点的坐标
        angle -= 2                                      # 旋转角度增加1度    
        cl = []                                         # 建空列表cl
        for x, y in points:                             # 每个点
            cl.append(x)
            cl.append(-y)    
        screen.cv.coords(ps[index], *cl)                # 重新配置frame各个坐标点
    screen.update()                                     # 更新屏幕显示
    time.sleep(0.1)
