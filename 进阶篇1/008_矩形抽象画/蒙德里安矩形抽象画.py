"""蒙德里安矩形抽象画.py
20世纪荷兰艺术家蒙德里安用一种简明的色彩矩阵”征服世界”。
这种色彩矩阵是在长方形里不断地画不相等的长方形。
"""
from random import randint
from turtle import Turtle,Screen

def drawRectangle(t,a,b):
    """用海龟t从左上角和右下角坐标画一个随机颜色的矩形.
    参数说明：
    t：海龟对象
    a：左上角坐标
    b：右下角坐标
    """
    x1,y1 = a
    x2,y2 = b
    red, green, blue  = randint(0,255),randint(0,255),randint(0,255) 
    t.color(red, green, blue)     #填充颜色用同一种色彩
    t.up()
    t.goto(x1, y1)
    t.down()
    t.begin_fill()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()

def mondrian(t,a,b,level):
    """用给定的层数画蒙得里安矩形抽象画."""
    if level <= 0: return
    x1,y1 = a
    x2,y2 = b
    drawRectangle(t,a,b)                    # 画矩形    
    hv = randint(1, 2)                      # 是1则垂直分矩形否则水平分
    if hv == 1:                             # 垂直分
       a = (x1,y1) ; b = (x1 + (x2 - x1) /3,y2)
       mondrian(t,a,b,level - 1)            # 在左边(1/3)画一个矩形
       a = (x1 + (x2 - x1)/3,y1);b = x2,y2
       mondrian(t,a,b,level - 1)            # 在右边画一个矩形
    else:                                   # 水平分
       a = (x1,y1) ; b = (x2,y1 - (y1 - y2) / 3)
       mondrian(t,a,b,level - 1)            # 在上边(1/3)画一个矩形
       a = (x1, y1 - (y1 - y2) / 3) ; b = (x2,y2)
       mondrian(t,a,b,level - 1)            # 在下边画一个矩形
    
def main():
    """生成窗口,新建海龟,调用递归函数画图"""
    screen = Screen()                   # 新建屏幕对象
    screen.delay(0)                     # 绘画延时为0
    screen.bgcolor("white")             # 背景白色
    screen.setup(600,480)               # 设定宽高
    screen.colormode(255)               # 颜色模式为255
    screen.title("蒙德里安矩形抽象画")  # 设定标题
    
    t = Turtle(visible=False)           # 新建隐藏的海龟对象
    a = -200,200                        # 左上角坐标
    b = 200,-200                        # 右下角坐标
    mondrian(t,a,b,10)                  # 调用函数画图

    screen.exitonclick()

if __name__=="__main__":

    main()
    
