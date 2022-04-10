"""
   星空飞碟大战.py
   由于配音需要混音器,这里用到了pygame的混音器,
   所以本程序需要pygame支持,安装方法为在命令提示符里输入:pip install pygame --user
   
"""
from sprites import *
import pygame.mixer

def star_move():
  """动态星空背景函数"""
  for star in stars:
    star.move(0,-20)
    if star.ycor() < -height//2:
      x = random.randint(-width//2,width//2)
      y = random.randint(10+height//2,height*2)
      star.reborn(x,y)

def spawn_enemy():
  """不定时产生敌机函数"""
  if random.randint(1,10)==1 and len(enemys)<10:
    x = random.randint(-200,200)
    y = random.randint(100,300)
    enemy = Sprite(shape='res/ufo.png',visible=False,pos=(x,y),tag='enemy')
    enemy.rotatemode(1)                    # 旋转模式为左右翻转 
    enemy.scale(0.5)                       # 缩小
    enemy.setheading(random.randint(1,360))# 方向
    enemy.show()                           # 显示

def enemymove():
  """飞碟的移动"""  
  for e in enemys:
    e.fd(3)    
    # 设定一定的机率让ufo朝向player
    if random.randint(10,100) == 10 and \
       abs(e.xcor())<200 and abs(e.ycor()<250):
      e.heading(player)                   # 朝向玩家飞机    
    e.bounce_on_edge()                    # 碰到边缘就反弹
      
def bulletmove():
  """子弹的移动"""  
  for b in list(bullets):
     b.move(0,10)
     if b.collide_edge():b.remove()
     
def player_shoot():
  """玩家射击函数"""
  if player.alive == False : return 
  if m1.down() and framecounter % 5 == 0 : # 按左键发射子弹
     b = Sprite(shape='circle',visible=False,tag='bullet')
     b.scale(0.5)
     b.color('yellow')    
     b.goto(player.pos())        # 移到player坐标
     b.show()                    # 显示子弹
     shoot.play()                # 播放射击声

# 播放背景音乐与生成声效对象
pygame.mixer.init()
pygame.mixer.music.load('audio/FrozenJam.ogg')
pygame.mixer.music.play(-1,0)
explosion = pygame.mixer.Sound('audio/expl3.wav')
shoot = pygame.mixer.Sound('audio/pew.wav')

width,height = 480,640
screen = Screen()               # 新建屏幕
screen.bgcolor('black')         # 屏幕背景色为黑
screen.setup(width,height)
screen.title("星空飞碟大战by李兴球")

screen.addshape('res/fighter.png')
screen.addshape('res/ufo.png')
frames = ['res/explosion0.png','res/explosion1.png']
[screen.addshape(frame) for frame in frames]

# 星星，用来做向下滚动背景,星星的移动也可以通过移动图章实现
# 这样可以有更多的星星。如果用克隆的话有数量限制,根据计算机配置不同而不同。
star = Sprite(shape='circle')
star.color('white')
star.scale(0.1)
stars = [star]
stars.extend([star.clone() for _ in range(20)])
for star in stars:
  x = random.randint(-width//2,width//2)
  y = random.randint(10+height//2,height*2)
  star.goto(x,y)

# 哭脸
cry = Sprite(shape='cry.png',visible=False,pos=(0,100))
#cry.goto(0,100)

# 玩家
player = Sprite(shape='res/fighter.png',pos=(0,-200))
player.scale(0.65)
player.alive = True             # 自定义属性,表示player是活的

m1 = Mouse()                    # 鼠标左键检测实例
clock = Clock()                 # 实钟对象,用来控制fps
framecounter = 0
counter = 0                     # 统计击中的ufo数量
bullets = Group('bullet')       # 子弹组
enemys = Group('enemy')         # ufo敌人组

while counter<100:              # 目标是击毁100架飞碟
  framecounter += 1             # 帧计数器
  spawn_enemy()                 # 不定时产生敌机UFO
  player_shoot()                # 单击鼠标左键,射击子弹
  enemymove()                   # 飞碟们的移动 
  bulletmove()                  # 子弹的移动
  if player.alive:              # 如果玩家操作的飞机没有死  
    player.goto(mousepos())
  else:
    cry.show()                  # 显示哭脸,表示失败
  star_move()                   # 星空滚动背景    
  
  for e in list(enemys):        # 对每架敌机进行碰撞检测
    if e.collide(player,scale=0.6):            
        explode(e.position(),frames)   # 敌机爆炸
        e.remove()
        explode(player.pos(),frames)   # 玩家飞机爆炸
        player.remove()
        player.alive = False
        explosion.play()         # 爆炸声
        break
    # 敌机是否碰到任意一颗子弹
    for b in list(bullets):
      if b.collide(e,scale=0.6): # 如果子弹碰到UFO        
        explode(e.position(),frames)
        e.remove()
        b.remove()
        explosion.play()         # 爆炸声
        counter +=1              # 进行统计         
        break            

  screen.title('星空飞碟大战,当前击毙：' +  str(counter) + " 架UFO")  
  clock.tick(60)
   
[b.remove() for b in list(bullets)] # 闯关成功把子弹删除
for e in list(enemys):              # 每架飞碟都爆炸
  explode(e.position(),frames)
  e.remove()  
  clock.tick(10)
    
t = Turtle(visible=False)           # sprites模块中当然有Turtle类
t.color('yellow')
t.write('成功闯关!',align='center',font=('黑体',32,'normal'))

while True:
  player.goto(mousepos()) 
  star_move()                   # 星空滚动背景  
  clock.tick(60)

