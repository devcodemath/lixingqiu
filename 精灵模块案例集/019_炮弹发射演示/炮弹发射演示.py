"""
    炮弹旋转发射演示。
    本程序会不断地生成炮弹,
    当炮弹碰到边缘后就隐藏并回到大炮的坐标重新开始发射。
"""
from sprites import *

def make_paodan():
    """新建炮弹角色,它的标签就是'炮弹'"""
    if len( Group('炮弹'))<20:
        bullet = Sprite('bullet.png',tag='炮弹',visible=False)
        bullet.goto(pao.pos())
        bullet.setheading(pao.heading())
        bullet.fd(60)
        bullet.show()
        
screen = Screen()
screen.bgcolor('#82f0f8')
screen.setup(600,600)
screen.title("炮弹旋转发射演示")

pao = Sprite('大炮.png')

frames = 0
while 1:
    frames += 1
    pao.right(1)
    if frames % 10 !=0:continue    
    make_paodan()        
    bs = Group('炮弹')   # 收集所有标签为'炮弹'的bullet形成集合
    for b in bs:
        b.fd(20)
        if b.collide_edge():
            b.hide()                     # 隐藏炮弹
            b.goto(pao.pos())            # 到达大炮的坐标
            b.setheading(pao.heading())  # 设定和大炮的方向一致
            b.fd(60)                     # 前进60个单位
            b.show()                     # 显示炮弹
    screen.title(str(len(bs)))
    print(len(screen.cv.find_all()))
 
 
