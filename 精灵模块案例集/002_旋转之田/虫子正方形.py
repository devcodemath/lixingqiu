from sprites import *

bug = Sprite()               # 新建虫子精灵
bug.screen.delay(10)         # 绘画延时为10毫秒
bug.pensize(4)               # 画笔尺寸
bug.color('dodger blue')     # 画笔颜色
bug.pendown()                # 落笔

for _ in range(4):           # 重复4次
    bug.fd(100)              # 前进100
    bug.rt(90)               # 右转90

bug.penup()
