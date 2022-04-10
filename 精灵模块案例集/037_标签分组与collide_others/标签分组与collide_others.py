"""
   利用标签分组与collide_others方法
   本程序运行后能用上下左右键操作虫子，碰到其它虫子时不会穿越过去。
"""

from sprites import *

screen = Screen()
screen.bgcolor('dodger blue')
screen.title('请用awsd键操作虫子')

bug = Sprite()
bug.color('red')

p1 = Sprite(5)         # 默认的标签为sprite
p1.goto(100,100)

p2 = Sprite(6)         # 默认的标签为sprite
p2.goto(-100,100)

p3 = Sprite(8)         # 默认的标签为sprite
p3.goto(-100,-100)

p4 = Sprite(9,tag='abcd') #指定标签为abcd,所以下面会穿越过去
p4.goto(100,-100)

akey = Key('a')       # 实例化a键
dkey = Key('d')       # 实例化d键
wkey = Key('w')       # 实例化w键  
skey = Key('s')       # 实例化s键
screen.listen()
clock = Clock()

while 1:
  # 如果按了a键，则dx为-5，虫子将向左移动  
  if akey.down():dx = -5;dy=0
  elif dkey.down():dx = 5;dy=0
  elif wkey.down():dy = 5;dx=0
  elif skey.down():dy = -5;dx=0
  else:
    dx = 0;dy = 0
    
  bug.move(dx,dy)      # 在水平和垂直方向上移动虫子
  
  # 和tag标签为sprite的精灵进行碰撞检测
  collide_list = bug.collide_others('sprite')
  print(collide_list)
  if collide_list:
    if dx != 0: bug.addx(-dx)   # 碰到了就撤销水平位移
    if dy != 0: bug.addy(-dy)   # 碰到了就撤销垂直位移    
    
  clock.tick(60)      # 设定fps为60
