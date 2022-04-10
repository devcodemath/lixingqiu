"""
   猴子吃桃问题演示，本程序并不是解决猴子吃桃问题，
   而是制作一个提出这个问题的动画。
"""
from sprites import *

ft = ('楷体',22,'normal')
words = ['一只猴子看见一堆桃子',
         '第一天它吃了这堆桃子的一半加1个',
         '第二天又吃了剩下的一半加1个',
         '依此类推',
         '到第十天只剩下1个桃子了',
         '请问最初有多少桃子?']
screen = Screen()
screen.bgcolor('dodger blue')
s = Sprite(visible=False)
s.color("white")
s.write("猴子吃桃问题演示",align='center',font=ft)
clock = Clock()                     # 新建时钟对象
s.wait(5)                           # 等 待 5 秒钟
for w in words:                     # 迭代每句话
    s.goto(-200,200)                # 定位到左上角
    dx = 1                          # 这代表字体大小 
    for x in range(36):             # 迭代x叁拾陆次
        ft = ('楷体',dx,'normal')   # 设定字体风格
        s.clear()                   # 清 空 所 画
        s.write(w,align='center',font=ft,angle=(1+x)*10)
        s.move(7,-7)                # 往右下角移动
        clock.tick(30)              # 固定FPS为30
        if x%2 ==0 : dx += 1        # 如果是偶数则加1
    s.wait(2)
    for x in range(36):
        ft = ('楷体',dx,'normal')
        s.clear()
        s.write(w,align='center',font=ft,angle=(-1-x)*10)
        s.move(7,7)
        clock.tick(30)
        if x%2 ==0 : dx -= 1
    s.clear()
    s.wait(1)
