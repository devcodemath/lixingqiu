"""
    炮弹旋转发射演示。本程序复用了炮弹,所以程序没有越来越慢。
"""
from sprites import *

screen = Screen()                      # 新建屏幕

screen.bgcolor('#82f0f8')              # 屏幕背景色
screen.setup(600,600)                  # 设置宽高
screen.title("炮弹旋转发射演示")       # 设置标题 
screen.tracer(0,0)                     # 关闭自动刷新

pao = Sprite('大炮.png')               # 实例化大炮
pd_group = Group('炮弹')               # 实例化炮弹组

[Sprite('bullet.png',tag='炮弹',visible=False) for x in range(10)]

unfired_list = list(pd_group)          # 待发射的炮弹列表
fired_list = []                        # 已经发射出去的炮弹表

frame_counter = 0                      # 帧计数器
clock = Clock()                        # 新建时钟对象

while True:
    frame_counter += 1
    pao.right(1)
    if frame_counter%10==0 and unfired_list:
        bullet = unfired_list.pop()         # 弹出一颗炮弹
        bullet.goto(pao.pos())         # 到大炮的坐标
        bullet.setheading(pao.heading())# 方向
        bullet.fd(60)                   # 到炮口
        fired_list.append(bullet)       # 添加到发射列表
        bullet.show()                   # 显示出来

    for b in fired_list:                # 每颗发射出去的炮弹
        b.fd(10)                        # 前进10个单位
        if b.collide_edge():            # 如果碰到边缘
            b.hide()                    # 隐藏起来                
            fired_list.remove(b)        # 从发射表中移除
            unfired_list.append(b)      # 添加到待发射列表
            
    screen.title(str(len(unfired_list))) # 显示待发射炮弹的数量
    screen.update()
    clock.tick(120)
 
