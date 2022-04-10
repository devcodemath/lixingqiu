"""
   跳跃方块爬墙平台游戏核心.py
   
   一个方块，按向上箭头会跳起来或爬墙，当然，不能连跳。
   按左右键头会左右移动，当碰到垂直障碍物会停止，碰到水平障碍物会停下。
   游戏中的平台是画出来的，你可以很容易地把它变成一个更加好玩有趣的游戏,
   如多关卡,接金币,创意都是自己想的,这里提供基础核心代码。
   
   本游戏需要Python精灵模块1.34版本支持。
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sprites   --upgrade  
   安装方法 pip install sprites
   如遇到困难，联系李兴球，微信scratch8,
   网址：www.lixingqiu.com
"""

from sprites import *                  # 从精灵模块导入所有命令

screen = Screen()                      # 新建屏幕
screen.setup(800,600)                  # 设定屏幕宽高
screen.bgpic('background.jpg')         # 设定背景图像

screen.title('跳跃方块爬墙平台游戏核心by李兴球')

square = Sprite(shape='square.png',pos=(-200,400))
square.dx = 0                           # 水平速度
square.dy = 0                           # 垂直速度

jumpkey = Key('Up')                     # 向上方向箭头
leftkey = Key('Left')                   # 向左方向箭头
rightkey = Key('Right')                 # 向右方向箭头
spacekey = Key('space')                 # 空格键
screen.listen()                         # 监听按键

bug = Sprite(visible=False)             # 用于画地板的隐藏虫子
bug.color('white')                      # 虫子所画的平台为白色的
floors = []                             # 地板们

# 下面是画第一个平台的代码
bug.bottomleft()                        # 到左下角
bug.addy(100)                           # 虫子的y坐标增加100
x,y = bug.pos()
coords = [(x+600,y),(x+600,y+10),(x,y+10)]
f1 = bug.polygon(coords)                # 以角色坐标为第一个点,coords为其它点画多边形
floors.append(f1)                       # 把名为f1的平台添加到floors列表

# 下面是画第二个平台的代码
bug.home()                              # 到屏幕原点
bug.addy(-50)
x,y = bug.pos()
coords = [(x+150,y),(x+150,y+10),(x,y+10)]
f2 = bug.polygon(coords)                # 以角色坐标为第一个点,coords为其它点画多边形
floors.append(f2)

# 下面是画第三个平台的代码
bug.goto(0,100)                         # 到坐标点(0,100)
x,y = bug.pos()
coords = [(x+150,y),(x+150,y+10),(x,y+10)]
f3 = bug.polygon(coords)                # 以角色坐标为第一个点,coords为其它点画多边形
floors.append(f3)

# 下面是画第四个平台的代码
bug.goto(-200,-200)                     # 到屏幕原点
x,y = bug.pos()
coords = [(x+10,y),(x+10,y+300),(x,y+300)]
f4 = bug.polygon(coords)                # 以角色坐标为第一个点,coords为其它点画多边形
floors.append(f4)

running = True
clock = Clock()

while running:
    # 处理重力加速度
    if square.dy == 0:  # 如果停止移动了,则让垂直速度为-1,下一帧则会往下移1
       square.dy = -1
    else:
       square.dy -= 0.5 # 方块的垂直速度以0.5减小

    # 左右按键检测
    if leftkey.down():                # 如果按向左方向箭头，y速度减1
        square.dx = -5
    if rightkey.down():
        square.dx = 5    
    square.dx = square.dx * 0.9
    
    square.addx(square.dx)             # 方块在做水平方向的移动的时候    
    items = square.overlap_with(floors)
    if items:                          # 如果有碰到地板
        item = list(items)[0]
        if square.dx > 0 :             # 正在往右移动
            square.setright(square.getleft(item))
            square.dx = -square.dx
        elif square.dx < 0:
            square.setleft(square.getright(item))
            square.dx = -square.dx        
        # 下面这句可以让角色爬墙
        if jumpkey.down():
            square.dy = 5  # 如果按跳跃键，则y速度设为5            
        
    square.addy(square.dy)             # 方块在做垂直方向的移动的时候
    items = square.overlap_with(floors)
    if items:                          # 如果有碰到地板
        item = list(items)[0]
        if square.dy > 0 :             # 正在往上移动
            square.settop(square.getbottom(item))
            square.dy = -square.dy
        elif square.dy < 0:
            square.setbottom(square.gettop(item))
        square.dy = 0
        if jumpkey.down(): square.dy = 15  # 如果按跳跃键，则y速度设为15
   
    screen.update()                 # 更新屏幕显示
    clock.tick(60)                  # 固定fps为60
