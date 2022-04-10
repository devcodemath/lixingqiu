"""拆帧演示程序.py"""
from PIL import Image, ImageSequence

im = Image.open("images/bake.gif")       # 打开gif图形
index = 0
for frame in ImageSequence.Iterator(im): # 对于图形中的每一帧
    filename = str(index) + ".png"
    frame.save(filename )
    index = index + 1
