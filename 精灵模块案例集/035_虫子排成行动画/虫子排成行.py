"""
   虫子排成行.py
"""
from sprites import  * 

width,height = 800,600
screen = Screen()
screen.setup(width,height)

bug = Sprite()          # 新建精灵对象
bug.bk(240)             # 倒退240个单位

for x in range(10):     # 盖10个图章
    bug.stamp()
    bug.fd(50)

while 1:
  # 移动每个图章  
  for item in bug.stampItems:
      bug.movestamp(item,0,1)               # 水平速度为0,垂直速度为1

  # 如果每个图章到了最顶上,则移到最下面
  for item in bug.stampItems:
      x,y = bug.stampcors(item)             # 获取图章中心点的x,y坐标 
      if y>300:
        bug.stampgoto(item,x,-300)          # 定位图章到x,y坐标
  screen.update()
