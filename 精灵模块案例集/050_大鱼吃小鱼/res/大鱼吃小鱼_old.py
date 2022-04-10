"""
   大鱼吃小鱼.py
   注意程序的mouth对象,它并不是"隐藏"的,虽然它看不见。
   小鱼碰到mouth会被“吃掉”。如果把mouth用hide命令设为隐藏，那么是无法获取到mouth的绑定盒，从而碰撞检测失效。
"""
from sprites import *

def small_fish_move():
    """每条小鱼的游动"""
    global fs,ms
    for fi in fish_group:
        if fi.ishide():continue     # 在可见的情况下才移动
        fi.fd(1)
        # 小鱼碰到嘴巴及单击鼠标则被吃掉，大鱼长大
        if fi.collide(mouth,0.5) and m1.down() :
            fs += 0.01
            bigfish.scale(fs)       # 大鱼长大
            ms += 0.01
            mouth.scale(ms)         # 嘴巴跟着加大
            x = random.randint(-200,200)
            y = random.randint(-140,140)
            # 注意这里调用了reborn后，鱼会立即隐藏，3秒后出现
            # 在3秒内碰撞检测无效，所以鱼不能动
            fi.reborn(x,y,delay=3)
            fi.shape(random.choice(fishpics)) # 换个造型           
        fi.bounce_on_edge()
        
def calculate_pos(obj):
    """obj：精灵对象。这个函数计算矩形右下(或左下)角的一个坐标并返回它。
    """    
    x,y = obj.position()              # 角色的坐标
    mx,my = mouse_position()          # 鼠标指针的坐标
    k = 1 if mx > x else -1           # 在右则为1，否则为-1
    left,top,right,bottom = obj.bbox()# 获取绑定盒
    w = right-left                    # 大鱼的宽度
    h = top - bottom                  # 大鱼的高度
    x0 = x + k * w//2.5               # 嘴巴大概的x坐标
    y0 = y - h//12                    # 嘴巴大概的y坐标
    return x0,y0
    
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
 
m1 = Mouse(1)                        # 鼠标左键
bigfish = Sprite('res/fish1-a.png')     # 实例化大鱼
bigfish.rotatemode(1)                   # 左右翻转 
fs= 0.6                              # 描述大鱼大小的数
ms = 0.4                             # 描述大鱼的嘴巴大小的数
bigfish.scale(fs)
mouth = Sprite(shape='circle')       # 实例化嘴巴，用于碰撞检测

mouth.scale(ms)                      # 缩放嘴巴大小
mouth.setalpha(0)                    # 把它设为透明，改为非0它会显示出来
clock = Clock()                      # 新建时钟对象

while True:
    small_fish_move()                # 每条小鱼的游动
        
    bigfish.heading(mouse_pos())     # 大鱼跟随鼠标指针
    x0,y0 = calculate_pos(bigfish)   # 计算嘴巴的大概坐标
    mouth.goto(x0,y0)                # 嘴巴到这个坐标 
    md =  bigfish.distance(mouse_pos()) # 计算鱼到鼠标指针距离
    if md > 50:bigfish.fd(min(md,4))    # 如果距离大于50则游

    # 张嘴与合嘴
    if m1.down():
        bigfish.shape('res/fish1-a.png')
    else:
        bigfish.shape('res/fish1-b.png')
    screen.update()
    clock.tick(60)
