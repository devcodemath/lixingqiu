"""
  宁静的小山村
"""
from pygame import mixer
from sprites import Sprite,Screen

mixer.init()
mixer.music.load('alto0.mp3')
mixer.music.play(-1,0)

screen = Screen()
screen.title('宁静的小山村')

img_blur = Sprite('blur.png',visible=False,pos=(11111,0))
img_blur.set_alpha(0)
img_blur.home()
img_blur.show()
img_blur.ondrag(None) 

for x in range(0,256,5):
    img_blur.set_alpha(x)
    if x > 200:screen.bgpic('crystal.png')

for x in range(255,0,-5):
    img_blur.set_alpha(x)    

screen.mainloop()
