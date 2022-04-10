"""
   闪闪金光圈_sprites多线程版
"""

from sprites import *
from threading import Thread

def shinning():
    clock = Clock()
    r = Sprite('金光圈.png')
    while True:
       for s in range(1,10):
           r.scale(s)
           clock.tick(30)
        
screen = Screen()

for _ in range(6):
    time.sleep(0.1)
    Thread(target=shinning).start()

screen.mainloop()
    
