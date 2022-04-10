"""可移动的矩形.py,本程序导入Point类,新建Rect类,
实例化了一个Rect对象,并且让它移动了一定的距离。"""

from point import *
from turtle import *

class Rect:
    def __init__(self, x,y,w,h):
        """x:左上角x坐标,y:左上角y坐标,w:宽度,h:高度"""
        self.x = x                  # 左上角x坐标
        self.y = y                  # 左上角y坐标
        self.width = w              # 矩形的宽度
        self.height  = h            # 矩形的高度
        self.xspeed = 0             # 矩形移动的水平速度
        self.yspeed = 0             # 矩形移动的垂直速度
        self.painter = Turtle(visible=False)# 画师是隐藏的海龟对象
        self.painter.penup()        # 抬笔
        self.painter.speed(0)       # 动作速度最快
        self.painter.screen.delay(0) # 绘画延时为0
        self.draw()                  # 显示自己
    def setspeed(self,dx,dy):
        """设置水平速度和垂直速度"""
        self.xspeed = dx
        self.yspeed = dy
        
    def move(self):
        """让矩形移动"""
        self.x += self.xspeed        # x坐标加上水平速度
        self.y += self.yspeed        # y坐标加上水平速度
        self.draw()                  # 重新显示自己
        
    def collidepoint(self,p):
        """判断一个点是否在矩形范围内"""
        if not isinstance(p,Point):  # 如果p不属于Point类
            print(p,"不是一个点")
            return
        c1 = p.x > self.x                # p点x坐标要大于最左边的x坐标
        c2 = p.x < self.x + self.width   # p点x坐标要小于最右边的x坐标
        c3 = p.y < self.y                # p点y坐标要小于最上边的y坐标
        c4 = p.y > self.y -self.height   # p点y坐标要大于最下边的y坐标
        return c1 and c2 and c3 and c4   # 同时满足4个条件说明它在矩形范围
    def draw(self):
        self.painter.goto(self.x,self.y) # 定位到矩形左上角
        self.painter.clear()             # 清除原先所画的
        self.painter.pendown()           # 落笔
        for i in range(2):               # 迭代i两次
            self.painter.fd(self.width)  # 前进self.width距离
            self.painter.rt(90)          # 右转90度
            self.painter.fd(self.height) # 前进self.height距离
            self.painter.rt(90)          # 右转90度
        self.painter.penup()             # 抬笔
        
def display(x,y):
    """在标题显示鼠标单击结果"""
    dian = Point(x,y)                   # 从鼠标指针的x,y坐标新建Point对象
    screen.title(r.collidepoint(dian))  # 鼠标指针在矩形范围单击则显示1
    
if __name__ == "__main__":

    screen = Screen()                   # 新建屏幕    
    r = Rect(-100,100,100,100)          # 新建矩形
    r.setspeed(1,0)                     # 设置矩形速度
    for i in range(100):                # 迭代i一百次
        r.move()                        # 移动r
    screen.onclick(display)             # 单击鼠标左键调用display函数
    
    screen.mainloop()





    
         
     
 
