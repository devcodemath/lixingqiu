"""
   最简平台跳跃游戏
"""
from sprites import *

width,height = 480,360
screen = Screen()    
screen.bgcolor('dodger blue')
screen.setup(width,height)
screen.title("最简平台跳跃游戏")
    
ground1 = Sprite(shape='square',visible=False)
ground1.goto(0,-150)
ground1.color('brown')
ground1.shapesize(2,30)
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

grounds = [ground1,ground2,ground3]

akey = Key('a')
dkey = Key('d')
wkey = Key('w')
images = ['res/cat1.png','res/cat2.png']

sp = Sprite(shape=images)             # 新建小猫
sp.dx = 0                             # 水平速度
sp.dy = 0                             # 垂直速度
sp.da = -0.02                         # 加速度
sp.rotatemode(1)                      # 左右翻转模式
screen.listen()                       # 临听屏幕按键

while 1:  
  if not screen._focus:              # 如果失去焦点
    #print('失去焦点')
    screen.update()
    continue
  
  # 按键检测
  sp.dx = 0
  if akey.down():
    sp.dx = -0.5
    sp.nextcostume()
    sp.setheading(180)
  elif dkey.down():
    sp.dx =0.5
    sp.nextcostume()
    sp.setheading(0)
  
  # 按w键跳跃
  if wkey.down() and sp.isground:
      sp.dy = 2
      sp.addy(sp.dy)
    
  # 坐标更新
  sp.isground = False   # 是否在地面
  sp.addx(sp.dx)
  for g in grounds:
    if sp.collide(g):   # 碰到任意一个地面则把标志为在地面
       sp.isground = True

  if sp.isground :      # 如果在地面,那么垂直速度为0
     sp.dy = 0
  else:
     sp.addy(sp.dy)
     sp.dy = sp.dy + sp.da  
     
  screen.update()






  
