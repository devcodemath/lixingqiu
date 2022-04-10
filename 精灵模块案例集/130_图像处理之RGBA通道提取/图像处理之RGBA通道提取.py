"""

   图像处理之RGBA通道提取。

   python精灵模块能进行图像处理吗?
   这个...，也算是可以吧,不过核心是numpy,这里只是用它的角色显示图形罢了。
   
   在sprites模块中，在新建屏幕的时候可以加布局参数。
   参数的名称叫layout，如果用Screen新建屏幕不写参数或值为1，那么一切还是海龟画图那样的布局。
   如果加了参数值为2，那么会形成左右布局，这个时候会有窗口会一分为二。
   左边的框架叫leftframe，右边的框架叫rightframe。它们的父(master)组件都是root。
   而角色所在的displayframe就在leftframe框架的上面。有一个叫bottomframe的框架
   在leftframe框架的下面。读者可在rightframe和bottomframe这两个框架中放置组件。
   这里需要tkinter知识，在turtle模块中它的缩写为TK。
   
   这个程序也可以通过im.convert('L')把图像变成灰度图。
   还可以通im = 255-im反转二维阵列用来生成负片效果。
   当然，对im进行各种转换，就能进行各种图像处理了。
   
"""
from sprites import *

def extractred():
    """提取红色通道"""
    imcopy = im.copy()
    imcopy[:, :, 1:3] = 0     # 所有绿色和蓝色通道的像素值为0
    redimg = Image.fromarray(imcopy)
    redimg.save('redimg.png')
    girl_red.shape('redimg.png')
    girl_red.show()
    
def extractgreen():
    """提取绿色通道"""
    imcopy = im.copy()
    imcopy[:, :, 0:3:2] = 0    # 所有红色和蓝色通道的像素值为0(步长为2)
    redimg = Image.fromarray(imcopy)
    redimg.save('greenimg.png')
    girl_green.shape('greenimg.png')
    girl_green.show()
    
def extractblue():
    """提取蓝色通道"""
    imcopy = im.copy()
    imcopy[:, :, 0:2] = 0     # 所有红色和绿色通道的像素值为0
    redimg = Image.fromarray(imcopy)
    redimg.save('blueimg.png')
    girl_blue.shape('blueimg.png')
    girl_blue.show()
    
def extractalpha():
    """提取透明通道"""
    imcopy = im.copy()
    imcopy[:, :, 0:3] = 0     # 所有红色和绿色通道的像素值为0
    redimg = Image.fromarray(imcopy)
    redimg.save('alphaimg.png')
    girl_alpha.shape('alphaimg.png')
    girl_alpha.show()
    
screen = Screen(2)                          # 新建左右分区的屏幕对象
screen.setup(800,600)
screen.title('图像处理之RGBA通道提取')
root = screen._root
root.rightframe.config(padx=10,pady=10)

pic = 'maid.png'
im = np.array(Image.open(pic))                # im是一个二维阵列,每个数据是一个4元组像素点

girl = Sprite('maid.png',pos=(-300,0))        # 这是原图形
girl_red = Sprite(visible=False,pos=(-150,0)) # 准备用来显示只有红色通道的图形
girl_green = Sprite(visible=False,pos=(0,0))  # 准备用来显示只有绿色通道的图形
girl_blue= Sprite(visible=False,pos=(150,0))  # 准备用来显示只有蓝色通道的图形
girl_alpha= Sprite(visible=False,pos=(300,0)) # 准备用来显示只有alpha通道的图形

b1 = TK.Button(root.rightframe,text='红色通道',font=('黑体',12,'normal'),command=extractred)
b1.pack()
b2 = TK.Button(root.rightframe,text='绿色通道',font=('黑体',12,'normal'),command=extractgreen)
b2.pack()
b3 = TK.Button(root.rightframe,text='蓝色通道',font=('黑体',12,'normal'),command=extractblue)
b3.pack()
b4 = TK.Button(root.rightframe,text='透明通道',font=('黑体',12,'normal'),command=extractalpha)
b4.pack()

screen.mainloop()

