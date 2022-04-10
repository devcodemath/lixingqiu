"""
   本程序实现一个能向前向后跳跃的小猫
"""
from sprites import *

width,height = 480,360       # 定义宽高变量
screen = Screen()            # 新建屏幕对象
screen.tracer(0,0)           # 关闭自动渲染与延时
screen.bgcolor('dodger blue')# 设定屏幕背景
screen.setup(width,height)   # 设定屏幕宽高
screen.title("跳跃的小猫,请按awd键")

# 用来画黑色地面的
t= Turtle(visible=False)     # 新建不可见海龟对象
t.penup()                    # 抬笔  
t.pensize(50)                # 画笔轨迹粗细
t.goto(-240,-150)            # 坐标定位
t.pendown()                  # 落笔
t.goto(240,-150)             # 坐标定位

akey = Key('a')              # a键实例
dkey = Key('d')              # d键实例 
wkey = Key('w')              # w键实例

sp = Sprite('res/cat1.png')  # 新建角色
sp.dx = 0                    # 水平速度
sp.dy = 0                    # 垂直速度
sp.da = -1                   # 加速度
sp.rotatemode(1)              # 左右翻转模式
screen.listen()

clock = Clock()              # 新建时钟对象
while 1:
  
  # 按键检测      
  if akey.down():            # 如果按了小写a键
    sp.dx = -5
    sp.setheading(180)
  elif dkey.down():          # 如果按了小写d键   
    sp.dx = 5
    sp.setheading(0)
  else:sp.dx = 0
  
  # 按w键跳跃
  if wkey.down() and sp.ycor()==-100:
      sp.play('jump.wav')
      sp.dy = 15
      sp.addy(sp.dy)
     
  if sp.ycor() < -100 :
      sp.dy = 0
      sp.sety(-100)
      
  # 坐标更新
  sp.addx(sp.dx)
  if sp.ycor()!= -100:         
     sp.addy(sp.dy)
     sp.dy = sp.dy + sp.da
   
  screen.update()            # 渲染画面显示
  clock.tick(60)
  
