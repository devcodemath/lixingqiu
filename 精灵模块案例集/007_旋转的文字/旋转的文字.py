"""
   旋转的文字.py,本程序主要演示如何写斜的字。
   注意在write命令中有名为angle的参数。
   本命令对turtle中的write命令进行了重定义,增加了angle参数。
   它能指定字的倾斜度，这样通过动画原理就能让所写的字旋转了。
"""

from sprites import *

screen = Screen()                       # 新建屏幕
screen.bgcolor('dodger blue')           # 设定背景颜色 
screen.title("旋转的文字")              # 设定标题

t = Sprite(visible=False)               # 新建不可见的角色
t.color('white')                        # 设定角色为白色 

a = 0                                   # a是一个全局变量,这里代表角度
info = '雅典娜'* 4                      # 要旋转的文字 
ft = ('黑体',32,'normal')               # 定义字体样式 
def rotate():                           # 定义rotate函数 
    global a                            # 申明a为全局变量
    t.clear()                           # 清除以前所写内容
    t.write(info,align='center',font=ft,angle=a)
    a = a + 10
    screen.ontimer(rotate,50)
rotate()

screen.mainloop()
