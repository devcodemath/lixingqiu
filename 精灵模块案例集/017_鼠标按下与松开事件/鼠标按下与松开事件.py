"""
   鼠标按下与松开事件.py
   在精灵模块中增加了onscreenrelease事件。
   它是鼠标松开事件，这里演示的是如何使用这个事件。

"""

from sprites import *

width,height = 480,360
screen = Screen()    

screen.bgcolor('dodger blue')
screen.setup(width,height)
screen.title("鼠标指针按下与松开事件")

def anxia(x,y):
  print('按下：',x,y)
  
def songkai(x,y):
  print('松开:',x,y)

screen.onscreenclick(anxia,3)
screen.onscreenrelease(songkai,3)

screen.mainloop()
