"""
   图像分割鱼.py
   请自行完善把它做成一个大鱼吃小鱼的游戏吧!
   这个是gameturtle版本,在gameturtle模块中导入了tkinter的命令所以能直接用.
"""
from time import sleep
from PIL import Image
from gameturtle import *

im = Image.open('png/Flatfish0.png')
w,h = im.size
costumes = []
# 下面分割图像
x ,y = 0,0
for i in range(5):                # 共5行 
    for j in range(4):            # 有4列
        box = (x,y,x+w/4,y+h/5)
        x = x + w/4
        costumes.append(im.crop(box))
    x = 0
    y = y + h/5
        
root = Tk()
cv = Canvas(width=480,height=360,bg='white')
cv.pack()

fish = Sprite(cv,costumes)
print(costumes)
while True:
    fish.fd(1)
    fish.nextcostume()
    cv.update()
    sleep(0.01)
