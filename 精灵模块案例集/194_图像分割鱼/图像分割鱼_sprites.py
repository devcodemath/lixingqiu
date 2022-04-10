"""
   图像分割鱼.py
   请自行完善把它做成一个大鱼吃小鱼的游戏吧!
"""
from time import sleep
from PIL import Image
from sprites import Sprite

im = Image.open('png/Flatfish0.png')
w,h = im.size
costumes = []
# 下面分割图像,分割的图像存放在res目录里
c = 0
x ,y = 0,0
for i in range(5):                # 共5行 
    for j in range(4):            # 有4列
        box = (x,y,x+w/4,y+h/5)
        x = x + w/4
        filename = f'res/fish_{c}.png'
        c = c + 1 
        im.crop(box).save(filename)
        costumes.append(filename)
    x = 0
    y = y + h/5
        
fish = Sprite(costumes)
fish.rotatemode(1)        # 1是左右翻转,0是360旋转,2是不旋转
print(costumes)
while True:
    fish.fd(1)
    fish.bounce_on_edge()
    fish.nextcostume()
    sleep(0.01)
