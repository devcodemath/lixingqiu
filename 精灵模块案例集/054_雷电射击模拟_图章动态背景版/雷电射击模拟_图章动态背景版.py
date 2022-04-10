"""
   雷电射击模拟_图章动态背景版.py
"""

from sprites import *

def player_move_and_shoot(player):
    """玩家飞机移动并且射击"""
    player.goto(mouse_pos())
    player.update()
    if framecounter % 10 == 0 and len(bullets)<10:
        b1 = Sprite('子弹.png',tag='bullet') # 新建标签为bullet的子弹
        b1.setheading(90)                    # 朝向90度的方向
        b1.goto(player.position())           # 子弹到达玩家飞机的坐标  

    for b in bullets:
        b.fd(20)
        b.update()
        if b.ycor()>random.randint(height,2*height):
            b.hide()          # 隐藏                
            b.goto(player.position()) # 子弹到达玩家飞机的坐标
            b.show()          # 显示
            break
        
def enemy_destroyed(bullets,enemy):
    """敌机被摧毁"""
    [b.hide() for b in bullets]       # 碰到的每颗子弹隐藏               
    x = random.randint(-width//2,width//2)
    y = random.randint(height,height*5)            
    explode(e,'res/explosion1.png') # 在e的位置爆炸
    e.reborn(x,y)                   # 让敌机到最上面重新出现 
    e.heading(player)               # 朝向玩家飞机的方向
    screen.update()
    
def perish_together(e,player):            # 同归于尽
    """敌机和玩家飞机被摧毁"""
    player.hide()                         # 玩家飞机隐藏
    e.hide()                              # 敌机隐藏
    explode(e,'res/explosion1.png')
    explode(player,'res/explosion1.png') # 在玩家飞机位置爆炸
    screen.update()            
           
width,height = 480,600
screen = Screen()
screen.tracer(0,0)
screen.bgcolor('black')
screen.setup(width,height)

screen.bgpic('封面.png')                # 显示封面 
screen.title('雷电射击模拟_图章动态背景版')
space = Key('space')                    # 实例化空格键
screen.listen()                         # 监听按键
while not space.down():screen.update()  # 等待按下空格键
screen.bgpic('nopic')                   # 设背景图为空

# 隐藏的角色循环播放背景音乐
Sprite(visible=False).play('Tragedy Flame.wav',loop=True)

# 用图章来做移动的星光背景
dummy = Sprite(visible=False,shape='star') # 用于打星光的
dummy.color('white')
for x in range(20):
    dummy.randomposition()                # 到随机位置
    dummy.scale(min(0.1,random.random()))
    dummy.stamp()

player = Sprite('res/thunder.png')        # 新建玩家操作的飞机
player.scale(0.7)                         # 把飞机缩小点

enemis = Group(tag='enemy')               # 新建敌机组  
for _ in range(20):                       # 建20个敌机
    x = random.randint(-width//2,width//2)# x坐标
    y = random.randint(height,height*5)   # y坐标
    e = Sprite(shape='敌机3.png',pos=(x,y),tag='enemy')
    e.rotatemode(2)                       # 不旋转
    e.setheading(-90)                     # 初始方向为向下
    e.scale(max(0.5,random.random()))     # 设定敌人飞机的初始大小 
    
bullets = Group(tag='bullet')             # 子弹组 

framecounter = 0
clock = Clock()
while True:
    framecounter += 1
    if player.isvisible():
        player_move_and_shoot(player)
    else:
        [b.remove() for b in list(bullets)] # 删除每颗子弹
        
    # 敌机的移动与碰撞检测    
    for e in enemis:                     # 每一架敌机
        e.fd(15)                         # 敌机前进15个单位 
        e.update()
        all_bullets = e.collide_others('bullet')  # 敌机和子弹们的碰撞
        if all_bullets :                          # 返回所碰到的子弹
            enemy_destroyed(all_bullets,e)        # 敌机被摧毁
            
        if e.collide(player) and player.isvisible():
            perish_together(e,player)             # 同归于尽                      
            
        if e.ycor()<-height//2:                   # 敌机到了最下面则从最上面出来
            x = random.randint(-width//2,width//2)
            y = random.randint(height,height*5)
            e.reborn(x,y)
            
    # 每颗星星不断地向下移动,如果到了最下面,则到最上面去  
    for s in dummy.stampItems:             # 每个图章(星星) 
        dummy.movestamp(s,0,-20)           # 向下移动20个单位
        x,y = dummy.stampcors(s)           # 获取星星的x,y坐标
        if y < -height//2 - 20:            # 如果到了最下面,则到最上面去
            dummy.stampgoto(s,x,20+height//2)
    clock.tick(60)
