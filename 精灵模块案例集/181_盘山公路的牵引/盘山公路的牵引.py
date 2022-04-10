"""
   盘山公路的牵引.py
   牵引小小卡丁车到达终点的一个小游戏。
   这个程序用到了Python颜色碰撞命令collidecolor，
   它会检测卡丁车和背景的颜色之间的碰撞，一旦碰到了不是公路的颜色，
   卡丁车就会退回到起始点。
"""
from sprites import *
from pygame import mixer

mixer.init()
failsnd = mixer.Sound('fail.wav')
succsnd = mixer.Sound('成功.wav')
mixer.music.load('bgm.mp3')
mixer.music.play(-1,0)
                      
screen = Screen()
screen.setup(960,720)
screen.title('盘山公路的牵引')

background = Sprite('road.png')
background.ondrag(None)

c1 = (163,241,94)
c2 = (255,215,103)
c3 = (99,99,99)
initpos = (-400,300)
cart = Sprite('卡车.png',pos=(-400,300))
running = True

while running:
    cart.heading(mouse_pos())
    if cart.distance(mouse_pos())>50:
       cart.fd(10)
       if cart.collidecolor(c1) or cart.collidecolor(c2):
          cart.goto(initpos)
          failsnd.play()
       if cart.collidecolor(c3):
          running = False 
    screen.update()
mixer.music.stop()
succsnd.play()
screen.title('成功牵引卡丁车到达终点')
screen.mainloop()
