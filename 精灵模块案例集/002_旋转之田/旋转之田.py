"""
   旋转之田.py
"""
from sprites import *

width,height = 480,360

screen = Screen()            # 新建屏幕对象 
screen.tracer(0,0)           # 关闭显示刷新
screen.setup(width,height)
screen.title("旋转之田")
screen.bgcolor('#e89e32')

bug = Sprite(visible=False)
bug.pensize(4)
bug.color('dodger blue')
bug.pendown()                # 在sprites模块中角色默认抬笔,所以这里要落笔

while True:
    bug.clear()              # 擦除以前所画图形
    for _ in range(4):       # 这两个for循环画田字
        for _ in range(4):
            bug.fd(100)
            bug.rt(90)
        bug.rt(90)    
    bug.right(1)
    bug.wait(0.01)           # 等待并刷新
