"""
   读出自己,本程序会把本身内容读出来,显示在屏幕上。
"""
from sprites import *

self = sys.argv[0]
f = open(self,encoding='utf-8')  # py的编码为utf-8
source = f.read()
f.close()

tom = Sprite(visible=False)      # 用于write的角色
tom.goto(-250,250)               # 左上角起始坐标

fnt = ('新宋体',14,'normal')     # 新建字体样式
lines = source.split('\n')
for line in lines:
    for char in line:
        tom.write(char,align='center',font=fnt)
        c = len(bytes(char,'gb2312'))       
        tom.addx(10*c)
    tom.setx(-250)
    tom.addy(-20)
    
tom.screen.mainloop()            # 进入主循环
