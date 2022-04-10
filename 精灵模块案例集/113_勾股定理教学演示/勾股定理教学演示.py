"""
   Python勾股定理粒子演示
"""
from sprites import *

def platlist(cors):
    """扁平化列表"""
    d = []
    for rows in cors:
        for x,y in rows:
            d.append((x,y))
    return d

def placeball(cors):
    stamps = []
    for rows in cors:        
        for x,y in rows:
            t.goto(x,y)
            sid = t.stamp()
            stamps.append(sid)
    return stamps

screen = Screen()

t = Sprite(shape=1,visible=True)
t.scale(0.5)

# 画6X6的格子
t.goto(-240,0)
acors = t.draw_grid2(6,6,20,20)
astamps = placeball(acors)

# 画8X8的格子
t.goto(-60,0)
bcors = t.draw_grid2(8,8,20,20)
bstamps = placeball(bcors)

# 画10X10的格子
t.goto(160,0)
ccors = t.draw_grid2(10,10,20,20)
dests = platlist(ccors)  # 扁平化列表
t.hide()

# 把6x6格子里的小球移到10x10格子
i = 0
for rows in acors:
    for x,y in rows:
        destx,desty = dests[i]
        sid = astamps[i]
        t.stampslide(sid,(destx,desty),200)          
        i = i + 1
        
# 继续把8x8格子里的小球移到10x10格子
j = 0   
for rows in bcors:
    for x,y in rows:
        destx,desty = dests[i]
        sid = bstamps[j]        
        t.stampslide(sid,(destx,desty),200)
        i = i + 1
        j = j + 1



