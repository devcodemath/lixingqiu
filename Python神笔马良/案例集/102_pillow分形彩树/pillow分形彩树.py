"""
    pillow分形彩树.py
    由于图像是左上角为原点，所以y坐标轴向下为正。
    角度方面的话，90度就变成向下了，-90度就变成向上了。
"""
import math, colorsys
from PIL import Image, ImageDraw
 
offset = 17                 # 角度偏移量
width, height = 1000, 800   # 图像分辨率
maxd = 12                   # 最大递归深度
length = 8.0                # 分支长度扩大因子

img = Image.new('RGB', (width, height))  # 新建RGB图像
d = ImageDraw.Draw(img)                  # 生成绘画对象 
print(dir(d))
def draw_tree(x1, y1, angle, depth):
    if depth>= 0:
        # 计算分支的下一个顶点
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * length)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * length)
 
        # 让分支的颜色和调用层次产生关联
        (r, g, b) = colorsys.hsv_to_rgb(float(depth) / maxd, 1.0, 1.0)
        R, G, B = int(255 * r), int(255 * g), int(255 * b)
 
        # 画树支
        d.line([x1, y1, x2, y2], (R, G, B), depth)
 
        # 左右各务两个更短的分支
        draw_tree(x2, y2, angle - offset, depth - 1)
        draw_tree(x2, y2, angle + offset, depth - 1)
 
#  调用递归函数开始绘画
x = width/2
y = height * 0.9
draw_tree(x,y, -90, maxd)
img.show()
img.save("彩树.png")
