"""
   跳跃方块避障游戏.py
   一个方块，按向上箭头会跳起来，按向下箭头会加速下落。
   还会有一些障碍物不断地从屏幕右边冒出来。
   游戏的逻辑就是避开这些障碍，谁玩得久，谁就是冠军。
   请修改代码自行调整游戏难度，如可以让多边形障碍从屏幕下方出现的机率更大。
   
   本游戏需要Python精灵模块1.33版本支持。
   安装方法 pip install sprites
   如遇到困难，联系李兴球，微信scratch8,
   网址：www.lixingqiu.com
"""

from sprites import *

def makepolygon():
    """随机产生一个多边形，加入列表"""
    global zais
    bug.randomcolor()            # 设定随机颜色
    bug.goto(400,random.randint(-360,360))
    zais.append(bug.polygon())   # 加到障碍物列表
    
def movepolygon():
    """移动每个多边形"""
    global zais
    [screen.cv.move(p,-5,0) for p in zais]

def removepolygon():
    """移除超出边界的多边形"""
    global zais
    for p in zais:
        pos = screen.cv.coords(p)
        right = max(pos[::2])     # 最右边x坐标
        if right<-480:
            screen.cv.delete(p)   # 从画布中删除这个item
            zais.remove(p)        # 在列表中移除这个item
            
def collidecheck():
    '''和所有多边形的碰撞检测'''
    global zais,running
    if square.overlap_with(zais):
         running = False
         
screen = Screen()
screen.setup(960,720)
screen.bgpic('backdrop1.png')
screen.title('跳跃方块避障游戏by李兴球')

PlaySound('Floating With You.wav',SND_ASYNC|SND_LOOP)

# 这个角色用来画从右往左移动的多边形
bug = Sprite(visible=False,pos=(400,0))

# 这个角色用来显示逝去的时间
w = Sprite(visible=False,pos=(0,250))

square = Sprite('square.png',pos=(-200,0))
square.dy = 0

zais = []                               # 障碍物列表
jumpkey = Key('Up')                     # 向上方向箭头
downkey = Key('Down')                   # 向下方向箭头
spacekey = Key('space')                 # 空格键
screen.listen()                         # 监听按键

while True:
    chance = 110                        # 控制多边形出现概率的整数
    running = True
    clock = Clock()
    start = time.time()                 # 起始时间
    framecounter =0                     # 帧计数器
    while running:
        framecounter +=1                # 统计帧数 
        esctime = time.time() - start   # 逝去的时间
        esctime = round(esctime)        # 四舍五入
        if framecounter % 60 == 0 :
           w.clear()
           w.write(esctime,align='center',font=('',48,'normal'))
        # 随着游戏的进行，机率越来越大了，游戏也就越来越难
        if random.randint(1,50) == 1 and chance > 20:
            chance -= 1

        # 以一定的机率产生一个多边形作为障碍物    
        if random.randint(1,chance) == 1:
            makepolygon()
        movepolygon()                   # 障碍物往左移
        removepolygon()                 # 超过最左边界移除它
        square.addy(square.dy)          # 方块往下移
        if square.ycor()-20 > -300:     # 方块底的y坐标大于-300
            square.dy -= 0.2            # 方块的y速度就减0.2
        else:
            square.dy = 0               # 否则认为到底了
            square.sety(-288)           # 设为y坐标为-288  
        if jumpkey.down():              # 如果按跳跃键，则y速度设为10
            square.dy = 10
            square.addy(1)
        if downkey.down():              # 如果按向下方向箭头，y速度减1
            square.dy -= 1        
            
        collidecheck()                  # 和所有多边形的碰撞检测
        screen.update()                 # 更新屏幕显示
        clock.tick(60)                  # 固定fps为60
    w.clear()
    w.write(esctime,align='center',font=('',48,'normal'))
    w.home()
    w.write(":( 按空格键重新开始",align='center',font=('',32,'normal'))
    while not spacekey.down():screen.update()
    w.goto(0,250)
    [screen.cv.delete(p) for p in zais] # 在屏幕上清除每个障碍物item
    zais = []                           # 障碍物列表
    square.goto(-200,0)
    square.dy = 0
