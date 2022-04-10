"""
   最简单的拆帧示例程序
"""
import os
from PIL import Image,ImageSequence

fld = "frames"
gif_file = "序幕.gif"
if not os.path.exists(fld):os.mkdir(fld)

gif_image = Image.open("序幕.gif")
index = 0
# 迭代gif图中的每一帧图像
for frame in ImageSequence.Iterator(gif_image):
    image = fld + os.sep + str(index) + ".png"
    frame.save(image)
    index = index + 1

print("done!")
