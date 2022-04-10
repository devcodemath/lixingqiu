"""
   小狗射怪兽.py
   本程序演示如何制作滚动卷轴的背景，
   演示如何用reborn方法复用精灵，从而让游戏更加流畅。
"""

from sprites import * 

def shoot():
  """发射子弹函数"""
  b = Sprite(shape='circle',visible=False,tag='bullet')
  b.color('yellow')
  b.goto(dog.pos())
  b.scale(0.5)
  b.play('fire.wav')
  b.show()
  
def spawn_monster():
  """产生一个怪兽"""
  m = Sprite(shape='monster.png',visible=False,tag='monster')
  m.dx = -2
  m.dy = 0
  x = random.randint(480,960)
  y = random.randint(-180,180)
  m.goto(x,y)
  m.scale(max(0.5,random.random()))
  m.show()

# 爆炸图列表
explosionimages = ['res/explosion0.png','res/explosion1.png']
screen = Screen()               # 新建屏幕
screen.setup(480,360)           # 设定屏幕分辨率
screen.bgpic('forest.png')      # 设定背景图 

dog = Sprite(shape='flydog.png')
dog.scale(0.5)
dog.setx(-200)
dog.alive = True

akey = Key('a')                  # 实例化a按键 
dkey = Key('d')                  # 实例化d按键
wkey = Key('w')                  # 实例化w按键 
skey = Key('s')                  # 实例化s按键
fkey = Key('f')                  # 实例化f按键    

[spawn_monster() for x in range(10)] # 产生10只怪兽

monsters = Group("monster")      # 怪兽组
bullets = Group("bullet")        # 子弹组 

screen.listen()                  # 监听键盘按键
clock = Clock()                  # 新建时钟对象
frames = 0
while 1:
  frames += 1
  if dog.alive == True:
    if akey.down(): dog.addx(-4)   # 按左键往左移
    if dkey.down(): dog.addx(4)    # 按右键往右移
    if wkey.down(): dog.addy(4)    # 按上键往上移
    if skey.down(): dog.addy(-4)   # 按下键往下移 
    if fkey.down():                # 按f键发射子弹
      if frames % 10 == 1: shoot()
  else:
    dog.move(0,-10)                # 狗死下坠,0是水平速度,-10是垂直速度

  [m.move(m.dx,m.dy) for m in monsters]
  # 超出边界的怪兽被“重生”，复用了精灵，让游戏更加流畅
  [m.reborn(random.randint(480,960),random.randint(-180,180),-2,0)
    for m in monsters if m.xcor() < -240 or m.ycor()<-180]
    
  for b in list(bullets):        # 由于remove命令会动态改变组所以加list
    b.move(10,0)
    collisions = b.collide_others('monster',scale=0.5)
    if collisions:
      b.remove()
      for m in collisions:
          explode(m,explosionimages)         # 爆炸效果
          m.dx = 0 ; m.dy = -10              # 往下掉 
        
  # 每颗子弹超过边界就移除它 ，注意：子弹并没有复用
  [b.remove() for b in set(bullets) if b.xcor() > 240 ]

  # 狗和怪兽们的碰撞检测
  colls = dog.collide_others(monsters,scale=0.5)
  if colls : dog.alive = False
  for m in colls: m.dx = 0 ; m.dy = -10
    
  # 背景向后移动,配合背景图片宽高为960x360和窗口为480,所以实现滚动背景效果
  screen.move(-10,0)      
  if screen.xcor()<=-240:screen.setx(240)
  
  screen.update()
  screen.title(str(len(screen.turtles())))
  clock.tick(60)
