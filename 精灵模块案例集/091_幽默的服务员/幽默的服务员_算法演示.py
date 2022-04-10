"""
某宾馆有100个房间,从1到100编了号,第一个服务员来了,他把所有的房门都打开。
第二个服务员来了，他把所有编号是2的倍数作相反处理（即原来关上的打开，原来打开的关上。)
第三个服务员把所有编号是3的倍数的房间也做相反处理。以后，第4、5一直到第100号服务员也
都是把自己编号倍数的房间做相反处理。问第100个服务员走过以后，有哪几扇门是开着的。
"""

from sprites import *

doorsimage = ['close.png','open.png']
rows = 10
cols = 10
length = 50
# 画10x10,长宽各为50的格子图,返回中心点坐标到cors
cors = Sprite(visible=False).draw_grid2(rows,cols,length,length)

doors = []                   # 装每个角色的列表
for rows in cors:
    for cor in rows:
        s = Sprite(shape=doorsimage,pos=cor)
        doors.append(s)
        time.sleep(0.01)

rooms = [ index for index in range(1,101) ]
# 下面的rooms中的键是房间编号,值代表房间开合状态,False代表关,True代表开
rooms = {}.fromkeys(rooms,False)

dummy = Sprite(visible=False)
dummy.addy(260)

ft = ('微软雅黑',22,'bold')
for 服务员 in range(1,101):  # 编号分别为1到100的服务员来
    dummy.clear()
    info = "第" + str(服务员) + "个服务员"
    dummy.write(info,align='center',font=ft)
    for r in range(1,101):   # 走过每个编号为r的房间
        if r % 服务员 == 0 : # 这个服务员只对自己编号的门做相反处理
            rooms[r] = not rooms[r]
            doors[r-1].shape(doorsimage[rooms[r]])
            time.sleep(0.1)

for r in range(1,101):
    if rooms[r]:print(r)

    
