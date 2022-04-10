""" 多彩弹球三.py。 本程序新建Ball类,它继承自Turtle。"""
from glob import glob
from turtle import Screen,Turtle
from random import randint,choice
 
class Ball(Turtle):
    def __init__(self,image):
        """image:已注册的gif图"""
        Turtle.__init__(self,shape=image)
        self.penup()
        self.xspeed = choice(speeds)         # 此处用到了全局变量speeds
        self.yspeed = choice(speeds)
        self.sw = self.screen.window_width()  # 屏幕宽度属性
        self.sh = self.screen.window_height() # 屏幕高度属性

    def move(self):
        """移动小球方法"""
        x = self.xcor() + self.xspeed        # 新的x坐标是原坐标加xspeed
        y = self.ycor() + self.yspeed        # 新的y坐标是原坐标加yspeed
        self.goto(x,y)
        left = x - 45                        # 小球最左边的x坐标
        right = x + 45                       # 小球最右边的x坐标
        top = y + 45                         # 小球最上边的y坐标
        bottom = y - 45                      # 小球最下边的y坐标
        c1 = left <= -self.sw// 2
        c2 = right >= self.sw//2
        if c1 or c2 :                        # 左或右超过边缘
            self.xspeed = -self.xspeed       # x速度取反
            
        c3 = bottom <= -self.sh//2
        c4 = top >= self.sh//2
        if c3 or c4 :                        # 上或下超过边缘
            self.yspeed = -self.yspeed       # y速度取反
        
if __name__ == "__main__":
    
    width,height = 800,600
    gif_images = glob("images/*.gif")
    speeds = [x for x in range(-5,5) if x!=0] # 如果x不是0则加到列表中

    screen = Screen()
    screen.delay(0)                           # 屏幕延时为0毫秒
    screen.bgcolor("black")                   # 设定屏幕背景色
    screen.setup(width,height)                # 设定屏幕宽高
    screen.title("多彩弹球三")
    [screen.addshape(image) for image in gif_images] # 注册所有gif到屏幕

    amounts = 10
    balls = [Ball(choice(gif_images)) for i in range(amounts)]
    running = True
    def setclose(x,y):
        global running                         # 申明为全局变量
        running = False
    screen.onclick(setclose)                   # 单击屏幕关窗口
    index = 0

    while running:
        balls[index].move()                    # 移动小球
        index = index + 1                      # 索引号加1
        index = index % amounts                # 索引对总数量求余
                                    
    screen.bye()                               # 关闭窗口
 

