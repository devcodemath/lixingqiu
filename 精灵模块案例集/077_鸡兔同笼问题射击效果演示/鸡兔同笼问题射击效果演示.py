"""
   鸡兔同笼问题射击效果演示,
   本程序并不是尝试解决鸡兔同笼问题,而是以一种效果抛出这个问题。
   它是一个动画。本程序需要sprites模块支持，请打开cmd窗口，输入
   pip install sprites进行安装。
"""
from sprites import *

string = '有若干鸡兔在同一个笼子里,从上面数有35个头,从下面数有94只脚。问笼中各有多少只鸡和兔？'
chars = []
for char in string:
    pic = f'res/{char}.png'           # 图像文件名
    txt2image(char,pic,fontsize=32)   # 文字转图像
    s = Sprite(pic,pos=(0,-200),visible=False)
    s.color('red')
    chars.append(s)                   # 添加到列表

screen = Screen()
screen.bgcolor('yellow')
screen.tracer(0,0)

dummy = Sprite(visible=False)
dummy.sety(200)
dummy.write('鸡兔同笼',align='center',font=('楷体',38,'bold'))
screen.update()
cols = 10                             # 列数
dx = 40                               # 列间距 
dy = 40                               # 行间距
startx = -200                         # 起始x坐标
starty = 100                          # 起始y坐标
screen.tracer(True)
for c in range(len(string)):
    x = startx + (c%cols) * dx       # x坐标  
    y = starty - (c//cols) * dy      # y坐标
    chars[c].show()                  # 显示出来
    chars[c].glide((x,y),100)        # 100豪秒几滑行到x,y坐标
    
screen.mainloop()    
