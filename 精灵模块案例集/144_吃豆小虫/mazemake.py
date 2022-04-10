"""
   迷宫生成器by李兴球@2020/3/9
"""
from sprites import *
from PIL import Image

def make_image(width,height,color=(255,0,0,255),border=2,bordercolor=(0,0,0,255)):
    """本函数用Image生成一个RGBA格式的图像,然后如果border不是0,则加边框。
       width：图像宽度，height：图像高度，color：填充颜色
       border：边框像素量，bordercolor：边框像素的颜色，返回图形对象。
    """
    pic = Image.new('RGBA',(width,height),color=color)
    if border > 0 :
        for x in range(width):
            for h in range(border):
                pic.putpixel((x,h),bordercolor)
                pic.putpixel((x,height-h-1),bordercolor)
        for y in range(height):
            for h in range(border):
                pic.putpixel((h,y),bordercolor) 
                pic.putpixel((width-h-1,y),bordercolor)
    return pic

def make_maze(mazefile,brickfilename):
    """
      mazefile：迷宫文件，是一个文本文件。
      brickfilename：迷宫的砖块文件，是一个图形。
      本函数会根据mazefile描述的信息及用brickfilename图形铺设迷宫。
    """
    im = Image.open(brickfilename)
    imgwidth,imgheight = im.size
                    
    f = open(mazefile)
    c = f.read()
    f.close()

    lines = c.split('\n')
    rows = len(lines)
    cols = len(lines[0])
    width = imgwidth * cols
    height = imgheight * rows

    screen = Screen()
    screen.delay(0)
    screen.setup(width,height)
    screen.addshape(brickfilename,Shape("image", screen._image(brickfilename)))

    square = Turtle(brickfilename,visible=False)
    square.penup()
    square.speed(0)
    square.goto(-width/2+imgwidth/2,height/2 - imgheight/2)
    nullcors = []
    for r in range(rows):
        for c in range(cols):
           if lines[r][c] == '+':
               square.stamp()
           else:
               nullcors.append(square.pos())
           square.fd(imgwidth)
        square.bk(width)
        square.sety(square.ycor()-imgheight)
    # 返回屏幕对象,铺迷宫砖块的角色和所有没有铺砖块的中心点坐标
    return screen,square,nullcors

if __name__ == "__main__":

    pic = make_image(50,50)
    pic.save('c:/a.png')
    screen,square,nullcors = make_maze('maze.txt','c:/a.png')
##    for x,y in nullcors:
##        square.goto(x,y)
##        square.dot(5,'blue')
    screen.mainloop()
