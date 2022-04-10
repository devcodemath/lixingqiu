"""
   像素化效果.py
"""
import os
from PIL import Image
from sprites import Sprite,mouse_position 

def pixelate(im,k):
    """像素化图形"""
    k = abs(k)
    if k==0:return im
    k = min(k,99)
    k = max(1,k)    
    width = im.width
    size = int(width * ((100-k)/500))
    size = max(1,size)
    imgSmall = im.resize((size,size),resample=Image.BILINEAR)   
    result = imgSmall.resize(im.size,Image.NEAREST)
    return result

pics = []
im = Image.open('res/thunder.png')
for i in range(100):
    tem = pixelate(im,i)
    fn = f'res/thunder{i}.png'
    pics.append(fn)
    if not os.path.isfile(fn):tem.save(fn)

g = Sprite(pics)

while True:
    mx,my = mouse_position()     #  鼠标指针坐标
    d = 10 * g.distance(mx,my)
    print(d)
    i = int(d) % len(pics)
    g.shape(pics[i])
