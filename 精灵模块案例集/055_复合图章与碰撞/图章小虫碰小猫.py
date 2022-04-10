"""
   本程序主要以图章为主碰对象去碰撞小猫
"""
from sprites import *                # 从精灵模块导入所有命令

s = Sprite()                         # 首先角色是小虫子
bug = s.stamp()                      # 盖了个图章是虫子造型
s.shape('res/cat1.png')              # s变身为小猫的造型

while True:                          # 当真
  s.stampgoto(bug,*mouse_pos())      # 用鼠标指针操作虫子移动(图章)
  if s.collidestamp(bug):            # 如果s碰到bug这个图章
     s.screen.title("图章碰到我了")  # 在标题栏里显示文字     
  else:
     s.screen.title("图章并没有碰到我")
  s.screen.update()
     
