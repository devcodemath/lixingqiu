"""
   奥特曼打怪兽射击游戏,本程序需要pygame的混音器支持,所以需要安装pygame模块才能正常运行。
   游戏操作方法：用鼠标指针牵引奥特曼，单击左键射击，碰到怪兽奥特曼死亡，杀死100个游戏成功结束。
   
   
"""
from sprites import *
from pygame import mixer

width,height = 800,600
screen = Screen()
screen.setup(width,height)
screen.bgcolor('black')
screen.title('奥特曼打怪兽by 李兴球')

mixer.init()
shootsound = mixer.Sound('audio/CANNON3.wav')
deadsound = mixer.Sound('audio/ORCHCYM.wav')
thudsound = mixer.Sound('audio/THUD.wav')

title = "奥特曼打怪兽"
helpinfo = '目标，打死100只怪兽'
txt2image(title,'res/title.png',fontsize=32,color=(0,255,255))
txt2image(helpinfo,'res/target.png',fontsize=20,color=(255,255,10))

game_title = Sprite(shape='res/title.png',pos=(0,260),visible=False)
game_title.stamp(10)                   # 10秒后图章自动消失
game_title.addy(-34)                   # 下移34像素
game_title.shape('res/target.png')
game_title.stamp(10)                   # 10秒后图章自动消失

frames = [f"frames/{i:04d}.png" for i in range(23)]
cover = Sprite(shape=frames)           # 封面角色
cover.addy(-20)
# 循环播放背景音乐
cover.play('纯音乐 - 迪迦奥特曼主题曲.mp3.wav',loop=True)
for _ in frames:
    cover.nextcostume()
    cover.wait(0.15)
for s in range(10,1,-1):
    cover.scale(s/100)
    cover.right(30)
    cover.wait(0.01)
ultraman = cover
ultraman.dead = False                  # 描述奥特曼没死
ultraman.scale(1)
ultraman.shape('res/奥特曼.png')

explosions = ['res/explosion0.png','res/explosion1.png']
costumes = ['res/fantasy7.png','res/ghoul-b.png','res/knight1.png',
            'res/monster1-a.png','res/robot1.png','res/wild1.png','res/witch.png']

monsters = Group('monster')             # 怪物组
[Sprite(shape=random.choice(costumes),tag='monster',visible=False) for _ in range(15)]

def init_monster(m):
    x = random.randint(-1000,1000)
    y = random.randint(-1000,1000)
    while ultraman.distance(x,y) < 400:
        x = random.randint(-1000,1000)
        y = random.randint(-1000,1000)
    m.goto(x,y)
    m.movetimes = 0            
    m.heading(ultraman)
    m.show()
            
[init_monster(m) for m in monsters]
    
bullet = Sprite('res/火png.png',visible=False)
bullet.speed = 0

counter = 0                             # 计数器
leftkey = Mouse(1)                      # 鼠标左键
clock = Clock()
success  = None                         # None,False与True
running = True
while running:
    for m in monsters:
        m.fd(1)
        #  如果撞到奥特曼
        if m.collide(ultraman,scale=0.5) and ultraman.dead == False:
            ultraman.dead = True
            explode(m.pos(),explosions)
            thudsound.play()
            success = False            
            break
            init_monster(m)
        elif m.collide(bullet):         # 如果怪兽碰到子弹
            counter += 1
            screen.title('奥特曼打怪兽，当前已打死：' + str(counter) + " 个")
            explode(m.pos(),explosions)
            thudsound.play()
            if counter == 100 :         # 如果100个怪兽死了
                success = True
                running = False
                break
            init_monster(m)            
        else:            
            m.movetimes += 1
            if m.movetimes > random.randint(60,100):
                m.movetimes = 0
                m.heading(ultraman)
    if ultraman.dead == False:          # 如果奥特曼没有死
        mxy = mouse_pos()               # 鼠标指针的坐标
        if ultraman.distance(mxy) > 50: # 如果到鼠标指针的距离大于50
            ultraman.heading(mxy)       # 朝向鼠标指针
            ultraman.fd(10)             # 移动10个单位
        if leftkey.down() and bullet.speed == 0: # 按左键发射
            shootsound.play()
            bullet.goto(ultraman.pos())
            bullet.setheading(ultraman.heading())
            bullet.speed = 20            # 注意！重定义了speed
            bullet.show()
    else:
        ultraman.move(0,-15)             # 往下掉
        if ultraman.ycor() < -height//2 - 20 : running = False
    bullet.fd(bullet.speed)
    if bullet.collide_edge():
        bullet.hide()
        bullet.speed = 0

    clock.tick(60)
    
if success == True:
    info = "成功击退怪兽们的进攻"
elif success == False:
    info = "生的光荣，死的伟大"

s = Sprite(visible=False)
s.color('yellow')
s.write(info,align='center',font=('楷体',40,'normal'))

# 成功后让每个怪兽自爆
if success == True:
    for m in monsters:
        effect(m.pos(),explosions)      # explode的别名是effect
        m.hide()
        m.wait(0.1)
screen.mainloop()
