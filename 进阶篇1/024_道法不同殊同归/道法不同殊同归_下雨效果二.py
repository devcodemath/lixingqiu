from turtle import Turtle,Screen
from random import randint 

class Rain(Turtle):                         # 继承自Turtle的Rain类
    def __init__(self):
        Turtle.__init__(self,shape='line',visible=False)
        self.penup()                        # 抬笔以便不留下笔迹
        self.color("gray")                  # 设定颜色为灰色
        self.setheading(-100)               # 设定方向为-100
        self.sw = self.screen.window_width()# 屏幕的宽度
        self.sh = self.screen.window_height()# 屏幕的高度
        self.init_position()                 # 初始化位置        
        
    def init_position(self):
        """初始化位置,把自己移到最上边"""
        self.ht()                            # 隐藏自己
        x = randint(-self.sw//2,self.sw//2)  # 设定x范围
        y = randint(self.sh//2 ,600 + self.sh//2 )# y范围
        self.goto(x,y)                       # 定位到x,y
        self.st()                            # 显示自己
        
    def move(self):
        """移动自己"""
        self.fd(20)                          # 前进20个单位
        if self.ycor() < -self.sh//2:        # 到最底边缘
            self.init_position()             # 移到最上边       

if __name__ == "__main__":
        
    width,height = 800,600                   # 定义全局变量
    screen = Screen()                        # 新建屏幕对象
    screen.bgcolor("black")                  # 设定屏幕为黑
    screen.bgpic("bg.png")                   # 设定屏幕背景
    screen.setup(width,height)               # 设定屏幕宽高
    screen.delay(0)                          # 设定绘画延时
    screen.title("道法不同殊同归_下雨效果二-ontimer")       # 设定屏幕标题
    screen.addshape('line',((0,0),(0,100)))  # 添加line形状
    rains = [Rain() for i in range(50)]      # 生成50个rain

    index = 0
    while True:                              # 当成立的时候
        rains[index].move()                  # 调用移动方法
        index = index + 1                    # 其索引增加一
        index = index % 50                   # 索引对50求余
    

