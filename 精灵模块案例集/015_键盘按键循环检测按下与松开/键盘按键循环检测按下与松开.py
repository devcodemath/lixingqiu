"""
   键盘按键循环检测按下与松开
"""

from sprites import *

width,height = 480,360

screen = Screen()    
screen.bgcolor('dodger blue')
screen.setup(width,height)
screen.title("键盘按键循环检测按下与松开_ 请按向上方向箭头")

uparrow = Key('Up')   # 新建键盘向上箭头按键实例
screen.listen()       # 监听按键

while 1:
  while not uparrow.down():screen.update()
  while uparrow.down():screen.update()
  print('键盘向上箭头按下并松开') 
