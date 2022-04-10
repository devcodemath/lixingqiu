"""旋转的三角形.py ,本程序设计了继承自海龟的Triangle类。
实例化对象后可以用鼠标指针拖动它,并且它会自动旋转。
在屏幕上单击鼠标右键它能归位。"""

from turtle import *
 
class Triangle(Turtle):
    def __init__(self,color,position):
        Turtle.__init__(self,shape='triangle')
        self.初始坐标 = position       # 记录初始坐标
        self.shapesize(2,2)            # 放大2倍
        self.penup()                   # 抬笔
        self.goto(position)            # 定位
        self.color(color)              # 设定颜色
        self.ondrag(self.goto)         # 拖放到
        self.rotate()                  # 旋转
        
    def rotate(self):
        """不断地让三角形旋转"""
        self.right(2)                  # 右转贰度
        screen.ontimer(self.rotate,10) # 定时执行
        
def reset(x,y):
    """屏幕中每个对象回到初始坐标"""
    [t.goto(t.初始坐标) for t in screen.turtles()]
    
if __name__=="__main__":
     
    width,height=600,600
    colors = ["red","orange","yellow","green"]
    
    screen = Screen()                   # 新建屏幕对象
    screen.setup(width,height)          # 设定屏幕宽高
    screen.delay(0)                     # 设定延时为零
    screen.bgcolor("black")             # 背景颜色为黑
    screen.title("旋转的三角形")        # 设定屏幕标题

    startx = -150
    starty = 150 
    for row in range(4):                # 拟定有4行
        for col in range(4):            # 拟定有4列
            x = startx + col * 100      # 设定x坐标
            y = starty - row * 100      # 设定y坐标
            Triangle(colors[col],(x,y)) # 生成三角形
    screen.onclick(reset,3)             # 单击右键归位
    screen.mainloop()                   # 屏幕主循环
