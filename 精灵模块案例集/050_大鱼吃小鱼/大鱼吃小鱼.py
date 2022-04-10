"""
   大鱼吃小鱼.py
   注意程序的mouth对象,它并不是"隐藏"的,虽然它看不见。
   小鱼碰到mouth会被“吃掉”。如果把mouth用hide命令设为隐藏，那么是无法获取到mouth的绑定盒，从而碰撞检测失效。
"""
from sprites import *

def cal_mouse_xy(bigfish):
    """计算大鱼的嘴巴(圆形)中心点坐标
    """    
    x,y = bigfish.position()          # 角色的坐标
    mx,my = mouse_position()          # 鼠标指针的坐标
    heading = 1 if mx > x else -1     # 大鱼的朝向,在右则为1，否则为-1
    left,top,right,bottom = bigfish.bbox()# 获取绑定盒
    w = right-left                    # 大鱼宽度       
    h = top - bottom                  # 大鱼高度
    r = w/8                           # 大鱼嘴半径
    if heading==1:                    # 如果朝向右
        x0 = right -r
    else:
        x0 = left + r
    y0 = top - h/2
    return x0,y0,r    # 返回能描述这个圆的三个关键数

def small_fish_move(bigfish):
    """每条小鱼的游动"""
    x0,y0,r = cal_mouse_xy(bigfish)        # 计算嘴巴中心点的大概坐标
    for fi in fish_group:
        if fi.ishide():continue             # 在可见的情况下才移动
        fi.fd(1)
        fish_to_mouth_dist = fi.distance(x0,y0) # 小鱼到大鱼嘴中心点距离
        # 小鱼碰到嘴巴则被吃掉，大鱼长大
        if fish_to_mouth_dist < r :
            bigfish.fs += 0.1
            bigfish.scale(bigfish.fs)       # 大鱼长大             
            x = random.randint(-200,200)
            y = random.randint(-140,140)
            # 注意这里调用了reborn后，鱼会立即隐藏，3秒后出现
            # 在3秒内碰撞检测无效，所以鱼不能动
            fi.reborn(x,y,delay=3)
            fi.shape(random.choice(fishpics)) # 换个造型           
        fi.bounce_on_edge()         # 碰到边缘就反弹

    
width,height = 480,360                
screen = Screen()                     # 新建宽高
screen.setup(width,height)            # 设置宽高 
screen.bgpic('res/underwater.png')    # 设背景图
screen.title("大鱼吃小鱼_Python Sprites Module")

fish_group = Group(tag='fish')        # 新建组，标签为fish
fishpics = ['res/fish1.png','res/fish2.png','res/fish3.png','res/crab-b.png']
# 由于下面的鱼的标签都是fish,所以会自动加入到fish_group中
for x in range(10):
     x = random.randint(-200,200)
     y = random.randint(-140,140)
     f = Sprite(shape=random.choice(fishpics),tag='fish',pos=(x,y))
     f.scale(0.5)
[fish.randomheading() for fish in fish_group]

bigcostumes = ['res/fish1-a.png','res/fish1-b.png']
bigfish = Sprite('res/fish1-a.png')  # 实例化大鱼
bigfish.rotatemode(1)                # 设定为左右翻转模式 
bigfish.fs= 0.6                      # 描述大鱼大小的数
bigfish.scale(bigfish.fs)

clock = Clock()                      # 新建时钟对象
framecounter = 0
costumeindex = 0
while True:
    small_fish_move(bigfish)         # 每条小鱼的游动
        
    bigfish.heading(mouse_pos())     # 大鱼的方向朝向鼠标指针      
    md =  bigfish.distance(mouse_pos()) # 计算鱼到鼠标指针距离
    if md > 50:bigfish.fd(min(md,4))    # 如果距离大于50则游
    
    # 张嘴与合嘴
    if framecounter % 10 ==0:
        bigfish.shape(bigcostumes[costumeindex])
        costumeindex = 1 - costumeindex
    framecounter += 1
    screen.update()
    clock.tick(60)
