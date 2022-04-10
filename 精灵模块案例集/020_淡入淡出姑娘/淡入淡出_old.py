"""
   淡入淡出.py   
   本程序演示了如何设定png图像为海龟的造型,
   及如何用pillow模块的putalpha命令设置透明度。
   在sprites模块中导入了Image类，所以可以直接使用它。
   
"""

from sprites import * 
    
def follow(x,y):
    """跟随鼠标指针"""
    screen.onmousemove(None)
    maid.goto(x,y)
    screen.onmousemove(follow)
    
def setalpha(turtle,alpha):
    """turtle：海龟对象，alpha：透明度"""
    
    im = turtle.rawimage.copy()
    im.putalpha(alpha)     
    name = turtle.rawimagename + str(alpha)
    screen.addshape(name,Shape('image',ImageTk.PhotoImage(im)))
    turtle.shape(name)
    
width,height = 480,360
screen = Screen()
screen.delay(0)
screen.setup(width,height)
screen.bgpic("tree.png")
screen.title("淡入淡出姑娘by李兴球")

filename = '姑娘.png'
rawimage = Image.open(filename)
rawimage = rawimage.convert('RGBA')
screen.addshape(filename)

maid = Turtle(visible=False,shape=filename)
maid.rawimagename = filename             # 自定义属性
maid.rawimage = rawimage
setalpha(maid,0)
screen.onmousemove(follow)
maid.st()

while 1:
    for alpha in range(0,256):
        setalpha(maid,alpha)

    for alpha in range(255,-1,-1):
        setalpha(maid,alpha)

