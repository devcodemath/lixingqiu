"""
   减速之彩色风车.py
   这是一个单击鼠标的小程序。
   操作方法是单击鼠标左键按住一会儿。那么变量spin的值就会一直增加。
   松开后，风车就会以spin做为“速度”不断地旋转。
   由于spin的值越来越小，所以风车旋转的速度越来越慢。
   
"""
from sprites import *

screen = Screen()
screen.title('减速之彩色风车')
screen.bgpic('movies outside.png')

bug = Sprite(visible=False,pos=(0,200))
bug.write2('请按住鼠标左键一会儿,然后松开')
spin = 0
windmill = Sprite('windmill.png')   # 新建风车角色

mleft = Mouse()                     # 鼠标左键
clock = Clock()                     # 时钟对象
while True:
   # 没有单击鼠标左键的时候下面这个while循环一直运行 
   while not mleft.down():screen.update()
   # 一旦单击鼠标左键，上面的while循环退出，进入下面的spin增加过程
   while mleft.down():
      spin += 0.1
      screen.title(spin)
      screen.update()
      clock.tick(60)
   # 松开后让风车旋转。
   while spin > 0:
        windmill.right(spin )
        spin -= 0.1
        screen.update()
        clock.tick(60)
   screen.update()
   clock.tick(60)
        
