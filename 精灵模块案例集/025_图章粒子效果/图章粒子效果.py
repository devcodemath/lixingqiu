"""
    图章粒子效果，
    海龟画图的图章是静止的，可本程序实现了移动它。
    并且碰到它缘它还会自动消失。
"""

from sprites import *
from random import *

screen = Screen()
screen.tracer(0,0)
screen.bgcolor('black')
screen.setup(600,600)

particle = Sprite(shape='circle',visible=False)
particle.color('white')
particle.scale(0.05)

velocity = [uniform(-5,5) for x in range(50)]
speeds = {}
while 1:    
    dx = choice(velocity)           # 水平速度
    dy = choice(velocity)           # 垂直速度
    dist = (dx*dx + dy*dy)**0.5 /15 # 距离的1/15 
    particle.scale(dist)            # 通过dist缩放particle
    i = particle.stamp()            # 返回图章编号
    speeds[i] = (dx,dy)             # 保存这枚图章的速度到字典中

    for item in particle.stampItems:    # 每个图章
        dx,dy = speeds[item]
        particle.movestamp(item,dx,dy)  # 移动图章
        if particle.collide_edge(item): # 如果item图章碰到边缘，删除它            
            particle.clearstamp(item)
            speeds.pop(item)
    screen.update()
    screen.title('粒子数：' + str(len(particle.stampItems)))
    
