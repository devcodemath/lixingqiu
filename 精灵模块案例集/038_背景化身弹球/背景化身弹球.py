"""背景化身弹球"""

from sprites import *        # 从精灵模块导入所有命令

screen = Screen()            # 新建屏幕
screen.setup(480,360)        # 设置分辨率
screen.bgpic('res/ball.png') # 背景图为弹球

dx = 2                       # 水平速度
dy = 2                       # 垂直速度
clock = Clock()              # 新建时钟对象

while 1:
  screen.move(dx,dy)         # 在水平和垂直方向上移动背景
  left,top,right,bottom = screen.bbox() # 获取背景的绑定盒
  if left <= -240 or right >=240:dx = -dx   # 是否到左右边界
  if bottom <= -180 or top >=180:dy = -dy   # 是否到上下边界
  screen.update()            # 更新屏幕显示
  clock.tick(60)             # 固定fps为60左右
