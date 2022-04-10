import os
from turtle import Screen
from PIL import Image, ImageSequence

def split_gif_image(imagefile):
    """加载gif文件,返回帧列表"""
    outputlist = []              # 待返回的每一帧
    framesfolder = os.getcwd() + os.sep + "frames"
    if not os.path.exists(framesfolder):os.mkdir(framesfolder)
    im = Image.open(imagefile)   # 载入图片
      
    index = 0
    for frame in ImageSequence.Iterator(im): #对于图形中的每一帧
        filename = framesfolder + os.sep + str(index) + ".png"
        frame.save(filename )
        outputlist.append(filename)
        index += 1
    return outputlist,(im.size)

def main():
    """加载gif,拆帧,在海龟屏幕的窗口中不断显示每一帧图"""
    gifimage = "bake.gif"
    imageslist,size = split_gif_image(gifimage)
    amounts = len(imageslist)

    screen = Screen()
    screen.setup(*size)                # size是元组,需要解包
    screen.title("海底小纵队小动画!" + gifimage)

    index=0                            # 索引从0开始轮换
    def changebg():
        nonlocal index                 # 非局部变量申明
        screen.bgpic(imageslist[index])# 显示索引为index的背景
        index=index+1
        index=index % amounts
        screen.ontimer(changebg,100)   # 100豪秒后自动调用 切换背景 函数
        
    changebg()                         # 调用切换背景函数
    print("程序没有运行完毕,背景在不断切换中")
    screen.exitonclick()
    
if __name__ == "__main__":

    main()
    
