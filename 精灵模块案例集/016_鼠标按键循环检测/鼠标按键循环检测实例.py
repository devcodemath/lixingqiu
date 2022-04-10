from sprites import *

width,height = 480,360

screen = Screen()    
screen.bgcolor('dodger blue')
screen.setup(width,height)
screen.title("鼠标按键循环检测实例_请单击鼠标左键")

mleft = Mouse()   # 新建鼠标按键检测实例，默认为左键
while 1:
  while not mleft.down():screen.update()
  while mleft.down():screen.update()
  print('鼠标左键按下并松开') 
