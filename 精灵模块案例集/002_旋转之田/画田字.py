"""
   画田字.py
"""

from sprites import *

width,height = 480,360
screen = Screen()
screen.delay(20)
screen.setup(width,height)
screen.title("画田字的虫子")
screen.bgcolor('#e89e32')

bug = Sprite()
bug.speed(7)
bug.pensize(4)
bug.color('dodger blue')
bug.pendown()
for _ in range(4):
    for _ in range(4):
        bug.fd(100)
        bug.rt(90)
    time.sleep(0.1)
    bug.rt(90)
bug.penup()
screen.mainloop()
