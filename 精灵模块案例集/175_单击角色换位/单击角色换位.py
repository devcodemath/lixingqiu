"""
   单击角色换位,
   本程序展示了单击让角色交换位置的最基本代码,
   
"""
from sprites import Sprite,Screen

def process(b,x,y):
    """处理单击"""
    global clicks,oldpos,oldb
    b.onclick(None)
    clicks += 1                     # clicks是2的时候才交换
    if clicks%2 == 0 :              
        clicks = 0
        if oldb != b :              # 不是同一个角色才换位
           p = b.pos()              # 把坐标记录 
           b.slide(oldb.position()) # 到刚才点的角色的坐标
           oldb.slide(p)            # 刚才点的角色到b角色之前的坐标 
    else:       
        oldb = b        # clicks是1,只是记录一下这个角色
    print(clicks,b)
    b.onclick(lambda x,y: process(b,x,y))

screen = Screen()

b1 = Sprite()
b1.onclick(lambda x,y: process(b1,x,y))
b2 = Sprite(1,pos=(100,0))
b2.onclick(lambda x,y: process(b2,x,y))
b3 = Sprite(2,pos=(100,100))
b3.onclick(lambda x,y: process(b3,x,y))
b4 = Sprite(3,pos=(-100,100))
b4.onclick(lambda x,y: process(b4,x,y))

clicks = 0                      # 统计单数次数
screen.mainloop()
