"""
   最简滚动平台跳跃
"""

from sprites import *

width,height = 480,360
screen = Screen()    
screen.tracer(0,0)

screen.bgcolor('dodger blue')
screen.setup(width,height)
screen.title("滚动平台跳跃")

ground0 = Sprite(shape='square',visible=False)
ground0.goto(-100,20)
ground0.color('brown')
ground0.shapesize(2,2)
ground0.show()

ground1 = Sprite(shape='square',visible=False)
ground1.goto(0,-150)
ground1.color('brown')
ground1.shapesize(2,130)
ground1.show()

ground2 = Sprite(shape='square',visible=False)
ground2.goto(50,-50)
ground2.color('brown')
ground2.shapesize(1,4)
ground2.show()

ground3 = Sprite(shape='square',visible=False)
ground3.goto(150,50)
ground3.color('brown')
ground3.shapesize(1,4)
ground3.show()

ground4 = Sprite(shape='square',visible=False)
ground4.goto(350,0)
ground4.color('brown')
ground4.shapesize(1,4)
ground4.show()

ground5 = Sprite(shape='square',visible=False)
ground5.goto(550,20)
ground5.color('brown')
ground5.shapesize(1,4)
ground5.show()

grounds = [ground0,ground1,ground2,ground3,ground4,ground5]

akey = Key('a')                               # 新建a键实例 
dkey = Key('d')                               # 新建d键实例
wkey = Key('w')                               # 新建w键实例

images = ['res/cat1.png','res/cat2.png']     # 朝右造型表

sp = Sprite(shape=images)             # 新建小猫
sp.dy = 0                             # 垂直速度
sp.da = -0.02                         # 加速度
sp.rotatemode(1)                      # 旋转模式为左右翻转
screen.listen()

ground_dx = 0

while 1:
  
  # 按键检测
  ground_dx = 0
  if akey.down():     # 如果按了a键
    ground_dx = 0.5
    sp.nextcostume()
    sp.setheading(180)
    
  if dkey.down():     # 如果按了d键
    ground_dx = -0.5
    sp.nextcostume()
    sp.setheading(0)
  
  # 按w键跳跃
  if wkey.down() and sp.isground:
      sp.dy = 2
      sp.addy(sp.dy)     
  
  sp.isground = False   # 是否在地面  
  
  for g in grounds:     # 每个地面
    g.addx(ground_dx)   # 都移动
    if sp.collide(g,scale=0.5):   # 碰到任意一个地面则把标志为在地面
       sp.isground = True

  if sp.isground :      # 如果在地面,那么垂直速度为0
     sp.dy = 0
  else:                 # 否则就自由落体 
     sp.addy(sp.dy)
     sp.dy = sp.dy + sp.da  
     
  screen.update()






  
