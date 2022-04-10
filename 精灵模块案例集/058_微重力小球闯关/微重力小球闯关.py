"""
   微重力小球闯关，本程序展示了一个基本的多关卡微重力游戏。
"""
from sprites import *         # 从精灵模块导入所有命令

width,height = 600,600        # 定义屏幕宽高
screen = Screen()             # 新建屏幕对象
#screen.bgcolor('black')       # 设定屏幕颜色
screen.setup(width,height)    # 设宽屏幕宽高

ball = Sprite(1)              # 新建小球对象
ball.dx = 0                   # 小球水平速度 
ball.dy = 0                   # 小球垂直速度
ball.saycolor('blue')         # 说话泡泡字体颜色
ball.say("请按上下左右键练习手感,\n然后一直往右。",8,False)

upkey = Key('Up')             # 实例化向上方向箭头
downkey = Key('Down')         # 实例化向下方向箭头
rightkey = Key('Right')       # 实例化向右方向箭头
leftkey = Key('Left')         # 实例化向左方向箭头  

# 定义关卡中每个方块的坐标
level1 = [(200,200),(-200,200),(0,0),(-220,-230),(220,-230)]
level2 = [(-100,0),(100,0),(0,-90),(0,90),(0,200),(0,-200),(260,0),(230,-230)]
level3 = [(-130,0),(-190,-100),(-120,120),(0,0),(150,100),(140,-130),(-100,230),(100,230),(-100,-230),(100,-230)]
levels = [level1,level2,level3]
level_index = 0               # 关卡索引号从0开始
level_amounts = len(levels)   # 关卡数量

squares = Group('square')     # 新建方块组，代表障碍物
def nextlevel(cors):          
    """下一关布局"""
    for x,y in cors:
        sq = Sprite(shape='square',pos=(x,y),visible=False,tag='square')
        sq.scale(4)
        sq.randomcolor()
        sq.show()
    
screen.listen()               # 监听按键
clock = Clock()               # 时钟对象
running = True
while running:
    # 按键检测
    if upkey.down():ball.dy += 0.1     # 如果按了上方向箭头
    if downkey.down():ball.dy -= 0.1   # 如果按了下方向箭头
    if rightkey.down():ball.dx += 0.1  # 如果按了右方向箭头
    if leftkey.down():ball.dx -= 0.1   # 如果按了左方向箭头
    # 移动小球
    ball.move(ball.dx,ball.dy)         # 小球移动
    碰到了 = ball.collide_others('square')  # 如果碰到方块    
    if 碰到了:
        [sq.remove() for sq in list(squares)]   
        running = False
        info = '闯关失败！'
        
    if ball.xcor() > width//2:         # 超过最右边界，下一关        
        [sq.remove() for sq in list(squares)]        
        if level_index < level_amounts:
           nextlevel(levels[level_index]) # 取下一关所有坐标重新生成方块
           level_index += 1                
           ball.setx(-width//2)
        else:
            running = False
            info = '闯关成功'
    clock.tick(60)

ball.remove()
del(ball)
tom = Sprite(2)                       # 用于显示结果的角色
tom.saycolor('blue')                   
tom.saybordercolor('cyan')
tom.say(info,100000,False)            # 异步显示10万秒
screen.mainloop()

