'''水波纹模拟二.py 左键单击后生成一个ripple,只有等它画完所有圈单击才有效'''

__author__ = "李兴球"
__date__ = "2019/1/15"

import glob
from turtle import Turtle,Screen      
 
class Ripple(Turtle):
    """定义Ripple涟漪类"""
    def __init__(self,x,y):
        """初始化方法,position为圆心坐标"""
        Turtle.__init__(self,visible=False)
        self.screen.onclick(None)       # 取消绑定
        self.penup()                    # 抬起笔来
        self.position = (x,y)           # 圆心坐标
        self.color(29,153,231)          # 颜色设置
        self.speed(0)                   # 速度设置 
        self.pensize(4)                 # 画笔宽度
        self.radius = 10                # 初始半径
        self.draw()                     # 开始画圈
    def draw(self):
        """调用定时器不断地画"""
        self.goto(self.position)        # 去到圆心
        self.fd(self.radius)            # 前进radius
        self.left(90)                   # 左转90度
        self.pendown()                  # 画笔落下
        self.circle(self.radius)        # 画个圆圈
        self.penup()                    # 抬起笔来
        self.radius = self.radius + 10  # 半径加10
        if self.radius < 500:           # 重新画圆
           self.screen.ontimer(self.draw,50)
        else:                           # 重新绑定
           self.screen.onclick(lambda x,y:Ripple(x,y)) 
        
def animate_screen():
    """不断切换背景图"""
    global bg_index                     # 申明全局变量
    screen.bgpic(waveimages[bg_index])  # 设定背景图片
    bg_index = bg_index + 1             # 图像索引加1
    bg_index = bg_index % bg_amounts    # 索引对数量求余
    screen.ontimer(animate_screen,100)  # 定时运行函数

def clear_draw(x,y):
    for t in screen.turtles():t.clear() # 清除所有笔迹
    
if __name__ == "__main__":              # 如果模块名为__main__

    bg_index = 0                        # 背景索引号   
    waveimages = glob.glob("waves/*.png")
    bg_amounts = len(waveimages)        # 背景数量
    
    screen = Screen()
    screen.title('水波纹模拟_面向对象') # 写上窗口标题
    screen.setup(800,600)               # 设定窗口大小
    screen.bgcolor('black')             # 背景颜色为黑
    screen.delay(0)                     # 屏幕延时为0
    screen.colormode(255)               # 屏幕颜色模式
    
    screen.onclick(lambda x,y:Ripple(x,y))# 单击左键生成涟漪
    screen.onclick(clear_draw,3)          # 单击右键清除涟漪
    animate_screen()                      # 不断切换背景图片
    screen.mainloop()                     # 进入屏幕的主循环

 
