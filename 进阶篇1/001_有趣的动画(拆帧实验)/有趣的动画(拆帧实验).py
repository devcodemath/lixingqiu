"""有趣的动画(拆帧实验).py"""

import os,time
from turtle import Screen
from random import choice
from PIL import Image, ImageSequence
 
def split_gif_image(imagefile):
    """加载gif文件,返回帧列表"""
    basename = os.path.basename(imagefile)
    outputlist = []              # 待返回的每一帧
    ffd = os.getcwd() + os.sep + "frames"    # 输出帧的文件夹
    if not os.path.exists(ffd):os.mkdir(ffd)
    im = Image.open(imagefile)   # 载入图片
    size = im.size
    index = 0
    for frame in ImageSequence.Iterator(im): # 迭代gif图中的每一帧
        filename = ffd + os.sep +  basename +  str(index) + ".png"
        frame.save(filename )
        outputlist.append(filename)
        index += 1
    im.close()                  # 关闭图形对象
    return outputlist, size     # 返回图形列表和宽高

def close(x,y):
    """左键单击屏幕,关闭窗口,从而结束程序"""
    screen.bye()
    
def main():
    """加载gif,拆帧,在海龟屏幕的窗口中不断显示每一帧图"""
    global screen
    path = os.getcwd() + os.sep + "images"
    screen = Screen()    
    screen.delay(0)
    screen.onclick(close)
    while True:
        for gifimage in os.listdir(path):     # path文件夹的每张gif图
            image = path + os.sep + gifimage        
            screen.title(gifimage + "_有趣的动画(拆帧实验)!")       
            imageslist,size = split_gif_image(image)         
            amounts = len(imageslist)
            width,height = int(size[0] * 1.2),int(size[1] * 1.2)
            screen.setup(width,height)         # 重设屏幕宽高        
            for frame in imageslist:           # 遍历每一张图
                screen.bgpic(frame)            # 显示背景 
                screen.update()                # 刷新显示
                time.sleep(0.05)               # 延时0.05秒
    
if __name__ == "__main__":

    main()
    
