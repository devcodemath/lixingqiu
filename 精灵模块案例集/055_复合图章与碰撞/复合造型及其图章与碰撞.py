"""
   复合造型及其图章与碰撞
"""
from sprites import *

width,height = 480,360
screen = Screen()
screen.setup(width,height)
screen.bgpic('res/sky.png')

def display_mouse_x_y(x,y):
    screen.title(str(x) + "," + str(y))
screen.onmousemove(display_mouse_x_y)

s = Shape("compound")                       # 新建复合类型的造型
tx = [(-10,10),(10,10),(20,-10),(-20,-10)]  # 第一个多边形
s.addcomponent(tx, "red", "blue")           # 加到造型里，填充为红边为蓝
sq = [(-10,20),(10,20),(10,10),(-10,10)]    # 第二个造型
s.addcomponent(sq,"blue",'brown')           # 填充为蓝边为棕

screen.addshape('tx',s)                     # 注册到造型字典

s = Sprite(shape='tx',visible=False)        # 角色本身是隐藏的
s.left(90)                                  # 左转90度
i = s.stamp()                               # 盖图章,编号为i

board = Sprite(shape='square')              # 新建一个矩形做为拦板
board.shapesize(0.6,5)                      # 给它变形
board.sety(-140)                            # 设置它的y坐标
dx = 1                                      # 水平速度
dy = 1                                      # 垂直速度

while True:
  board.setx(mouse_pos()[0])
  s.stampmove(i,dx,dy)                      # 水平与垂直方向移动
  if s.stampcollide(i,board,0.5):           # 如果图章i碰到board
     dy = -dy
 
  left,top,right,bottom = s.stampbbox(i)    # 获取绑定盒子
  if left <= -width//2 or right >= width//2:dx = -dx
  if bottom <= -height//2 or top >= height//2:dy = -dy
  s.wait(0.001)          


