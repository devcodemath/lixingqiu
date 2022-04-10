"""
   字符画转换器_txt3image使用举例.py
"""
from PIL import Image
from sprites import Sprite,txt3image

#主程序
def image2txt(pic,scale):
    """图像转文本,首先转换成灰度,
       pic:图像文件名,scale:比例
    """
    z = [' ','@']
    z = [' ','.','@','•']
    
    im = Image.open(pic)
    width,height = im.size
    width,height = int(width*scale),int(height*scale)    
    img = im.resize((width, height)).convert('L')
    
    text = ''
    for y in range(height):
        for x in range(width):
            huiduzhi = img.getpixel((x, y))    # 得到gray值
            i = int((256/len(z)))
            text += z[huiduzhi//i] # 转换成charactar
        text += '\n'
    return text

txt = image2txt('res/cat1.png',0.3)  # 图像转文本，返回文本
print(txt)

# 多行文本转图像，保存在'res/testabcd.png'这里
txt3image(txt,'res/testabcd.png',fontfile='simsun.ttc',fontsize=12)              # 又把文本转图像
g = Sprite('res/testabcd.png')

g.screen.mainloop()
