"""
   猴小子冲关.py
"""
import sys
import pygame
from sprites import *

title = '猴小子冲关_Python精灵模块版本'
pygame.mixer.init()
pygame.mixer.music.load('audio/Jetpack Joyride.wav')
pygame.mixer.music.play(-1,0)
dead_sound = pygame.mixer.Sound("audio/死.wav")
collect_sound = pygame.mixer.Sound("audio/collect.wav")

bgi = 0
bgs = [f'bgs/{index}.png' for index in range(12)]  # 12张背景图
width,height = 480,360
screen = Screen()
screen.setup(width,height)
screen.bgpic(bgs[bgi])
screen.title(title)

weapons = ['im/剑.png','im/匕首.png','im/戟.png','im/环.png','im/锤.png',
           'im/盾4.png','im/箭.png','im/菜刀.png','im/血滴子.png','im/cat.png']

_help = Sprite('im/title.png',visible=False)
_help.sety(120)
_help.stamp(3)                     # 3秒后此图章被清除
_help.shape('im/help.png')
_help.sety(60)
_help.stamp(5)                     # 5秒后此图章被清除


# 障碍物weapons
obstacle = Sprite(shape=random.choice(weapons),visible=False)  # 障碍物
x = random.randint(width,width*2)
y = random.randint(-height//2,height//2)
obstacle.goto(x,y)
# obstacle不断地旋转
def auto_rotate():
    obstacle.left(30)
    screen.ontimer(auto_rotate,80)
auto_rotate()

# 金币
coins = [f"im/g{index}.png" for index in range(8)]
c_index = 0
c_amounts = len(coins)
coin = Sprite(shape=coins[0],visible=False)
coin.scale(0.5)
x = random.randint(width,width*2)
y = random.randint(-height//2,height//2)
coin.goto(x,y)
coin.show()
# coin不断地换造型
def coin_rotate():
    global c_index
    c_index += 1
    c_index %= c_amounts
    coin.shape(coins[c_index])
    screen.ontimer(coin_rotate,100)
coin_rotate()

# 猴小子
costumes = ['im/造型1.gif','im/造型2.gif']
index = 0
monkey = Sprite(shape=costumes[index],pos=(-200,0))
monkey.scale(0.5)
monkey.alive = True
monkey.right(90)
monkey.saycolor('cyan')
monkey.saybordercolor('yellow')
monkey.say("冲啊!!",wait=False)
# monkey不断地变换造型
def alt_costume():
    global index
    index = 1 - index
    monkey.shape(costumes[index])
    screen.ontimer(alt_costume,50)
alt_costume()

akey = Key('a')                     # 实例化a按键 
dkey = Key('d')                     # 实例化d按键
wkey = Key('w')                     # 实例化w按键 
skey = Key('s')                     # 实例化s按键
screen.listen()                     # 监听按键 
clock = Clock()
speed = 10                          # 背景移动速度 
distance = 0                        # 路程
counter = 0                         # 接到的金币计数器
while speed>0:    
  if monkey.alive == True:
     if akey.down(): monkey.addx(-4)   # 按左键往左移
     if dkey.down(): monkey.addx(4)    # 按右键往右移
     if wkey.down(): monkey.addy(4)    # 按上键往上移
     if skey.down(): monkey.addy(-4)   # 按下键往下移 
  else:
     monkey.move(0,-5)                 # 猴死下坠
     if monkey.ycor()<-height//2-500:speed = 0
     
  obstacle.move(-4,0)               # 障碍物向左移      
  # 猴子碰到障碍物时惨叫一声并下落
  if monkey.collide(obstacle,scale=0.85) and \
     obstacle.isvisible() and monkey.alive:
      monkey.alive = False
      dead_sound.play()
      explode(monkey,'im/血.png',400) # 延时400毫秒后消失      

  # 障碍物到了最左边时就会又移到最右边的一个坐标
  if obstacle.xcor() < -width//2:
      x = random.randint(width*2,width*4)
      y = random.randint(-height//2,height//2)
      obstacle.reborn(x,y,delay=2)    # 在x,y坐标重新出现
      obstacle.shape(random.choice(weapons))

  coin.move(-1,0)                   # 金币向左移
  if monkey.collide(coin) and coin.isvisible():      
      x = random.randint(width*2,width*4)
      y = random.randint(-height//2,height//2)
      collect_sound.play()
      coin.reborn(x,y,delay=2)        # 2秒后在x,y坐标重新出现
      counter = counter + 1
      screen.title(title + '当前接到金币：' + str(counter))
      
  if coin.xcor() < -width//2:        # 金币到了最左边则确定一个位置重新出现
      x = random.randint(width*2,width*4)
      y = random.randint(-height//2,height//2)
      coin.reborn(x,y,delay=2)      
  
  # 背景向后移动
  screen.move(-speed,0)
  distance = distance + speed       # 统计路程
  if distance % 10000 == 0 :        # 到了10000就换背景
      bgi = bgi + 1
      if bgi < len(bgs):
         screen.bgpic(bgs[bgi])
  if bgi == len(bgs):               
      if speed>1:
          speed = speed - 0.1
      else:
          speed=0
  # 背景到了最左边,则移到最右边去 
  if screen.xcor()<=-width//2:screen.setx(width//2)
  screen.update()
  clock.tick(120)

if monkey.alive:
    [monkey.left(1) for x in range(90)]
else:
    Sprite(shape='im/cry.png')
    
