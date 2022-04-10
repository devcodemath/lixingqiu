"""
   开始游戏,本程序主要演示如何实例化鼠标左键,
   以及如何检测鼠标左键有没有按下及碰到鼠标指针命令的使用方法。
"""
from sprites import *           # 从精灵库导入所有命令

button = Sprite('button1.png')  # 新建角色
leftkey = Mouse(1)              # 鼠标左键

while not leftkey.down():       # 当没有单击鼠标左键的时候
  if button.collidemouse():     # 如果按钮碰到鼠标指针
    button.shape('button1.png') # 切换到造型button1
  else:    
    button.shape('button2.png')

ft = ('黑体',32,'normal')
button.hide()                   # 隐藏按钮
button.screen.bgcolor("dodger blue")
button.write('游戏开始了',align='center',font=ft)
button.screen.mainloop()
     
