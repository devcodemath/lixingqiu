"""
   模拟3D打印大楼.py
"""
from sprites import Sprite,Key

def build(level):
    """搭建level层"""
    global scale
    for x in range(level):
        sps.append(sp1.clone())
        sp1.addy(1)
        scale -= 0.001
        sp1.scale(scale)

scale = 1                       # 代表角色的缩放值
sp1 = Sprite('造型1.png')       # 新建角色 
screen = sp1.getscreen()        # 获取屏幕对象
sps = [sp1]                     # sps列表存储所有角色
build(3)                        # 建3层
sp1.shape('造型2.png')          # 切换到造型2.png
build(15)                       # 建15层
for x in range(8):              # 在范围8迭代x
    sp1.shape('造型3.png')      # 切换到造型3.png 
    build(10)                   # 建10层
    sp1.shape('造型4.png')      # 切换到造型4.png
    build(5)                    # 建5层
sp1.shape('造型5.png')          # 切换到造型5.png
build(3)                        # 建3层

leftkey = Key("Left")           # 实例化左方向箭头 
rightkey = Key("Right")         # 实例化右方向箭头
screen.listen()                 # 监听屏幕按键检测
while True:                     # 当成立的时候
    if leftkey.down():          # 如果左方向箭头被按下 
        screen.tracer(0)        # 关闭自动刷新
        for p in sps:p.left(5)  # 所有角色向左旋转5度
        screen.update()         # 刷新屏幕显示
    if rightkey.down():         # 如果左方向箭头被按下 
        screen.tracer(0)        # 关闭自动刷新
        for p in sps:p.right(5) # 所有角色向右旋转5度
        screen.update()         # 刷新屏幕显示
    screen.update()            
            
